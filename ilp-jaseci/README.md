# Interactive Learning Platform for Jaseci (ILP)

An advanced, personalized learning portal for Jac and Jaseci that combines adaptive learning algorithms, AI-powered assessment, and spatial graph visualization to create a tutoring experience.

## 🎯 Project Overview

The ILP platform enables learners to:
- **Progress through structured lessons** covering Jac basics, walkers, OSP (Object-Spatial-Paradigm), and byLLM agents
- **Take adaptive quizzes** that adjust difficulty based on performance
- **Practice with interactive code exercises** with instant validation
- **Visualize their learning journey** through a dynamic skill map
- **Receive personalized recommendations** based on mastery analysis

### Key Features

✨ **Adaptive Learning**
- OSP graph models each user's mastery over concepts
- Prerequisites and proficiency thresholds unlock new content
- Spaced repetition for optimal retention

🤖 **AI-Powered Assessment**
- byLLM agents generate contextual quiz questions
- Free-text and code answers evaluated intelligently
- Personalized feedback and explanations

📊 **Visual Progress Tracking**
- Skill map shows strengths and weak areas
- Progress dashboard with detailed analytics
- Learning timeline and streak tracking

🎓 **Structured Content**
- Lessons organized by category and difficulty
- Code examples and interactive exercises
- Prerequisite management and unlocking system

## 📁 Project Structure

```
ilp-jaseci/
├── backend/                 # Jac backend service
│   ├── models/
│   │   ├── user.jac           # User and progress models
│   │   ├── lesson.jac          # Lesson and content models
│   │   ├── quiz.jac            # Quiz and assessment models
│   │   └── osp_graph.jac       # Knowledge graph model
│   ├── walkers/
│   │   ├── progress.jac        # Progress tracking walkers
│   │   ├── content.jac         # Content serving walkers
│   │   └── quiz.jac            # Quiz generation/assessment walkers
│   ├── agents/
│   │   └── learning_optimizer.jac  # byLLM learning intelligence
│   ├── app.py               # Flask API service
│   └── requirements.txt      # Python dependencies
│
├── frontend/                # React frontend application
│   ├── src/
│   │   ├── components/
│   │   │   ├── LessonViewer.jsx         # Lesson display
│   │   │   ├── CodeEditor.jsx           # Exercise editor
│   │   │   ├── QuizComponent.jsx        # Quiz interface
│   │   │   ├── SkillMap.jsx             # Mastery visualization
│   │   │   ├── ProgressDashboard.jsx    # Learning analytics
│   │   │   ├── LessonViewer.css
│   │   │   ├── CodeEditor.css
│   │   │   ├── QuizComponent.css
│   │   │   ├── SkillMap.css
│   │   │   └── ProgressDashboard.css
│   │   ├── services/
│   │   │   └── walkerService.js        # Walker call utilities
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   └── README.md
│
├── shared/                  # Shared utilities and types
│   └── constants.js         # Constants and enums
│
├── docs/
│   ├── ARCHITECTURE.md      # System design
│   ├── API_REFERENCE.md     # API endpoints
│   ├── WALKER_GUIDE.md      # Walker implementation guide
│   └── DEPLOYMENT.md        # Deployment instructions
│
├── README.md               # This file
└── requirements.txt        # Project dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 16+
- Jac language environment (from jac-env)
- npm or yarn

### Backend Setup

```bash
# Navigate to project root
cd ilp-jaseci

# Install Python dependencies
pip install -r requirements.txt

# Start the Flask API server
python backend/app.py
```

The backend API will run on `http://localhost:5000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The frontend will run on `http://localhost:3000`

## 🏗️ Architecture

### Backend (Jac)

#### Data Models
- **User**: User profile, metadata, aggregate scores
- **Lesson**: Structured learning content with sections
- **Quiz**: Questions and assessments
- **OSPNode**: Knowledge concepts in the learning graph
- **MasteryNode**: User's mastery per concept

#### Walkers (Graph Traversal)
1. **ProgressTracker**: Records lesson completion, calculates proficiency
2. **MasteryAggregator**: Aggregates performance data, identifies weak areas
3. **ContentServer**: Delivers lessons, checks prerequisites
4. **QuizGenerator**: Creates quizzes using LLM (byLLM decorator)
5. **QuizAssessor**: Grades answers intelligently (byLLM decorator)
6. **ContentValidator**: Validates code submissions

#### byLLM Agents (AI Intelligence)
1. **LearningPathOptimizer**: 
   - Analyzes OSP graph
   - Recommends next lessons
   - Identifies struggle areas

2. **RevisionPlanner**:
   - Schedules spaced repetition
   - Selects targeted review material

3. **SkillAssessment**:
   - Assesses readiness for advanced topics
   - Evaluates learning consistency
   - Predicts success probability

### Frontend (React)

#### Components
- **LessonViewer**: Displays lesson sections with navigation
- **CodeEditor**: Textarea-based code editor with test validation
- **QuizComponent**: Quiz interface with adaptive difficulty
- **SkillMap**: Visual graph of mastered concepts
- **ProgressDashboard**: Overall learning analytics

#### State Management
Uses React hooks for local state and API calls for server-side data.

### API Layer (Flask)

RESTful endpoints bridging frontend and Jac walkers:
- `/api/lessons/*` - Lesson management
- `/api/quizzes/*` - Quiz operations
- `/api/progress/*` - Progress tracking
- `/api/users/<id>/*` - User data and recommendations
- `/api/exercises/*` - Exercise validation

## 📊 Data Flow

```
User Action (Frontend)
    ↓
React Component (e.g., QuizComponent)
    ↓
API Call to Flask (e.g., POST /api/quizzes/evaluate-answer)
    ↓
Flask Route Handler
    ↓
Spawn Jac Walker (e.g., spawn('QuizAssessor', {...}).evaluate_free_text_answer())
    ↓
Walker Processes (w/ @by_llm decoration)
    ↓
Returns Result to Flask
    ↓
JSON Response to Frontend
    ↓
Update React State & UI
```

## 🧠 Adaptive Learning Algorithm

### Mastery Scoring
```
Mastery Score = (Quiz Performance × 0.7) + (Practice Time × 0.3)
Range: 0.0 (novice) to 1.0 (mastered)
```

### Proficiency Thresholds
- **0.0 - 0.4**: Weak (review needed)
- **0.4 - 0.6**: Developing (practice more)
- **0.6 - 0.8**: Strong (approaching mastery)
- **0.8 - 1.0**: Mastered (ready for advanced topics)

### Dynamic Difficulty
Quizzes adjust based on correct answer streak:
- 3 correct in a row → increase difficulty
- 2 incorrect in a row → decrease difficulty

### Spaced Repetition
RevisionPlanner schedules reviews based on:
- Time since last practice
- Current mastery score
- Concept importance

## 📝 Sample Lessons

The platform includes pre-built lessons for:
1. **Jac Basics** (beginner)
   - What is Jac?
   - Nodes and edges
   - Basic syntax

2. **Walkers** (intermediate)
   - Walker definition and traversal
   - Pattern matching
   - Complex traversals

3. **OSP** (intermediate/advanced)
   - Object-Spatial-Paradigm concepts
   - Graph structures
   - Advanced patterns

4. **byLLM** (advanced)
   - LLM integration
   - Agent creation
   - Practical applications

## 🔌 Integration with Jaseci

### Spawning Walkers from Frontend

Example from React component:
```javascript
// Call a walker from the frontend
const response = await fetch('/api/quizzes/evaluate-answer', {
  method: 'POST',
  body: JSON.stringify({
    quizId,
    questionId,
    userAnswer,
    questionType
  })
});
```

The Flask backend then calls the Jac walker:
```python
# In Flask route handler
result = spawn('QuizAssessor', {
    'quiz_id': quiz_id,
    'question_id': question_id,
    'user_answer': user_answer,
    'question_type': question_type
}).evaluate_free_text_answer()
```

## 🎨 Customization

### Adding New Lessons
1. Create lesson content in markdown
2. Define in `backend/models/lesson.jac`
3. Add to database
4. Reference in recommendations

### Adding New Question Types
1. Create question node in `backend/models/quiz.jac`
2. Implement evaluation logic in `QuizAssessor` walker
3. Add corresponding React component
4. Update API validation endpoint

### Tuning Mastery Weights
Edit calculation in `ProgressTracker.calculate_proficiency()`:
```jac
let proficiency = (score * 0.7) + (time_spent * 0.3);
```

## 📚 Documentation

See the `docs/` folder for:
- **ARCHITECTURE.md**: Detailed system design
- **API_REFERENCE.md**: Complete API documentation
- **WALKER_GUIDE.md**: How to implement walkers
- **DEPLOYMENT.md**: Production deployment

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🚢 Deployment

### Production Build (Frontend)
```bash
cd frontend
npm run build
```

### Docker Support
```bash
docker-compose up --build
```

See `DEPLOYMENT.md` for cloud deployment options.

## 🤝 Contributing

To extend the platform:
1. Add new walkers for specialized features
2. Create additional components for new functionality
3. Enhance byLLM agents with better prompts
4. Contribute sample lessons for new topics

## 📄 License

This project is part of the Jaseci educational initiative.

## 🙋 Support

For questions or issues:
1. Check `WALKER_GUIDE.md` for walker implementation
2. Review API examples in `backend/app.py`
3. Examine component implementations in `frontend/src/components/`

---

**Built with Jac/Jaseci & React**
Happy Learning! 🚀
# ILP-JAC.
