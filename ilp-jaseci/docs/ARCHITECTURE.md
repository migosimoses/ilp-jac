# Architecture Overview

## System Design

The Interactive Learning Platform (ILP) uses a three-tier architecture:

```
┌─────────────────────────────────────┐
│  Frontend (React/JavaScript)         │
│  - Components for UI/UX              │
│  - State management                  │
│  - REST API communication            │
└────────────┬────────────────────────┘
             │ HTTP/REST
┌────────────▼────────────────────────┐
│  Backend API (Flask/Python)          │
│  - REST endpoints                    │
│  - Business logic orchestration      │
│  - Spawn/call Jac walkers            │
└────────────┬────────────────────────┘
             │ Spawn/RPC
┌────────────▼────────────────────────┐
│  Jac Runtime & Walkers               │
│  - Data models (nodes/edges)         │
│  - Graph traversal walkers           │
│  - byLLM AI agents                   │
│  - OSP computation                   │
└─────────────────────────────────────┘
```

## Component Architecture

### Frontend Components Hierarchy

```
App
├── Navigation
├── AuthGuard
│   ├── LoginPage
│   └── RegisterPage
└── DashboardLayout
    ├── Sidebar
    │   ├── LessonList
    │   ├── QuizList
    │   └── Progress
    └── MainContent
        ├── LessonViewer
        │   ├── SectionNavigation
        │   └── CodeExample
        ├── CodeEditor
        │   ├── Editor
        │   └── TestResults
        ├── QuizComponent
        │   ├── QuestionDisplay
        │   ├── AnswerInput
        │   └── Feedback
        ├── ProgressDashboard
        │   ├── Statistics
        │   ├── Timeline
        │   └── Recommendations
        └── SkillMap
            ├── ConceptNodes
            └── ConceptDetail
```

### Backend Component Architecture

```
Flask Application
├── Authentication Routes
│   ├── POST /auth/login
│   ├── POST /auth/register
│   └── POST /auth/logout
├── Lesson Routes
│   ├── GET /lessons/{id}
│   ├── GET /lessons/category/{cat}
│   └── POST /lessons/complete
├── Quiz Routes
│   ├── GET /quizzes/{id}
│   ├── POST /quizzes/evaluate-answer
│   └── POST /quizzes/score
├── Progress Routes
│   ├── POST /progress/track
│   ├── GET /users/{id}/progress
│   └── GET /users/{id}/skill-map
├── Recommendation Routes
│   ├── GET /users/{id}/recommendations
│   └── GET /users/{id}/next-lesson
└── Exercise Routes
    ├── POST /exercises/validate
    └── POST /exercises/submit
```

### Jac Model Architecture

```
OSPGraph (Knowledge Structure)
├── Nodes
│   ├── User (Profile data)
│   ├── Lesson (Content structure)
│   ├── Quiz (Assessments)
│   ├── OSPNode (Concepts)
│   ├── UserProgress (Tracking)
│   ├── MasteryNode (Proficiency)
│   ├── QuizAttempt (Results)
│   └── CodeExercise (Exercises)
└── Edges
    ├── studied_lesson (User → Lesson)
    ├── completed_quiz (User → Quiz)
    ├── prerequisite (Lesson → Lesson)
    ├── prerequisite_concept (OSPNode → OSPNode)
    └── unlocks_lesson (OSPNode → Lesson)
```

### Walker Architecture

**Content & Progress Walkers** (Deterministic)
```
ContentServer
├── get_lesson_content()
├── get_next_recommended_lesson()
├── validate_prerequisites()
└── get_code_exercises()

ProgressTracker
├── track_lesson_progress()
├── update_mastery_score()
├── calculate_proficiency()
└── unlock_next_lesson()

MasteryAggregator
├── aggregate_mastery()
├── identify_weak_areas()
└── generate_skill_map()
```

**Assessment Walkers** (byLLM-powered)
```
QuizGenerator
├── @by_llm: generate_quiz()
└── @by_llm: generate_question_variants()

QuizAssessor
├── @by_llm: evaluate_free_text_answer()
├── @by_llm: evaluate_code_answer()
├── @by_llm: generate_feedback()
└── score_quiz_attempt()

ContentValidator
├── validate_code_exercise()
└── check_code_quality()
```

**Adaptive Intelligence Walkers** (byLLM-powered)
```
LearningPathOptimizer
├── @by_llm: analyze_learning_graph()
├── @by_llm: recommend_next_lesson()
├── @by_llm: generate_personalized_path()
└── @by_llm: identify_struggle_areas()

RevisionPlanner
├── @by_llm: plan_revision_schedule()
├── @by_llm: select_revision_material()
└── @by_llm: generate_revision_quiz()

SkillAssessment
├── @by_llm: assess_readiness_for_advanced()
├── @by_llm: evaluate_learning_consistency()
└── @by_llm: predict_success_on_topic()
```

## Data Flow Patterns

### Learning Flow
```
User Starts Lesson
    ↓
ContentServer.get_lesson_content()
    ↓
Frontend renders LessonViewer
    ↓
User completes sections
    ↓
User clicks "Complete Lesson"
    ↓
ProgressTracker.track_lesson_progress()
ProgressTracker.calculate_proficiency()
ProgressTracker.update_mastery_score()
    ↓
Frontend shows completion and next recommendation
```

### Quiz Flow
```
User Starts Quiz
    ↓
(If new) QuizGenerator.generate_quiz()
    ↓
Frontend renders QuizComponent
    ↓
User answers each question
    ↓
QuizAssessor.evaluate_{type}_answer() [byLLM]
    ↓
Frontend shows feedback
    ↓
After all questions: QuizAssessor.score_quiz_attempt()
    ↓
ProgressTracker.update_mastery_score()
    ↓
Frontend shows results
```

### Recommendation Flow
```
User views Progress Dashboard
    ↓
LearningPathOptimizer.analyze_learning_graph() [byLLM]
    ↓
LearningPathOptimizer.identify_struggle_areas() [byLLM]
    ↓
RevisionPlanner.plan_revision_schedule() [byLLM]
    ↓
LearningPathOptimizer.recommend_next_lesson() [byLLM]
    ↓
Frontend displays recommendations
```

## State Management

### Frontend State (React)
- **Local Component State**: Question answers, UI toggles
- **API State**: User progress, lesson data, quiz results
- **Cache**: Lesson content, quiz questions (to reduce API calls)

### Backend State (Flask)
- **Session Data**: User authentication, temporary processing
- **Database**: All persistent data (via Jac graph)
- **Cache**: Frequently accessed walkers results

### Jac Graph State
- **Nodes**: User profiles, lessons, quizzes, concepts
- **Edges**: Relationships (studied, completed, unlocked)
- **Walkers**: Stateful traversals during computation

## API Contract Examples

### LessonViewer → ContentServer
```javascript
// Frontend request
GET /api/lessons/jac-basics-1
Headers: X-User-ID: user123

// Flask route
@app.route('/api/lessons/<lesson_id>')
def get_lesson(lesson_id):
    result = spawn('ContentServer', {
        'user_id': user_id,
        'lesson_id': lesson_id
    }).get_lesson_content()
    return jsonify(result)
```

### QuizComponent → QuizAssessor
```javascript
// Frontend request
POST /api/quizzes/evaluate-answer
{
    "quizId": "quiz-1",
    "questionId": "q1",
    "userAnswer": "Object-Spatial-Paradigm",
    "questionType": "multiple_choice"
}

// Flask route spawns walker
result = spawn('QuizAssessor', {
    'quiz_id': quiz_id,
    'question_id': question_id,
    'user_answer': user_answer
}).evaluate_free_text_answer()
```

### ProgressDashboard → LearningPathOptimizer
```javascript
// Frontend request
GET /api/users/user123/recommendations
Headers: X-User-ID: user123

// Flask route spawns walker
result = spawn('LearningPathOptimizer', {
    'user_id': user_id,
    'mastery_data': mastery_data
}).recommend_next_lesson()
```

## Scalability Considerations

### Frontend
- Code splitting by route for faster initial load
- Lazy loading of lesson content
- Virtual scrolling for long lists

### Backend
- Worker pool for concurrent walker spawning
- Caching of frequently accessed data
- Rate limiting per user

### Jac
- Graph indexing for fast lookups
- Batch operations for bulk updates
- Horizontal scaling through sharding

## Security Considerations

- **Authentication**: JWT tokens for user sessions
- **Authorization**: Check user owns their data before returning
- **Input Validation**: Sanitize all user inputs in Flask routes
- **Code Safety**: Sandbox code exercise execution
- **CORS**: Restrict API access to frontend domain

## Deployment Architecture

```
Docker Container
├── Flask API Service
│   └── gunicorn/WSGI server
├── Jac Runtime
│   ├── Walkers
│   └── Graph Database
└── Static Assets
    └── React Frontend (build/)
```

## Testing Strategy

- **Unit Tests**: Walker logic, API endpoints, React components
- **Integration Tests**: Walker → API → Frontend flows
- **E2E Tests**: Full learning journeys
- **Performance Tests**: Walker spawn time, API response time

---

See API_REFERENCE.md for detailed endpoint documentation.
