# Interactive Learning Platform for Jaseci - Navigation Guide

Welcome to the ILP project! This guide helps you find what you need quickly.

## 🎯 Start Here

**New to the project?**
1. Read [`README.md`](README.md) - 10 minute overview
2. Follow [`QUICKSTART.md`](QUICKSTART.md) - Get running in 5 minutes
3. Review [`VISUAL_GUIDE.md`](VISUAL_GUIDE.md) - See system diagrams
4. Check [`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md) - Complete overview

## 📚 Documentation

### Overview & Setup
- **[README.md](README.md)** - Project features, architecture overview, requirements
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup, sample journeys, common tasks
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - What was built, components, scale
- **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - Architecture diagrams, data flows, visualizations

### Technical Deep-Dives
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System design, component hierarchy, API contracts
- **[docs/WALKER_GUIDE.md](docs/WALKER_GUIDE.md)** - How to implement walkers, byLLM patterns, examples
- **[docs/API_REFERENCE.md](docs/API_REFERENCE.md)** - Complete API documentation (TBD)
- **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Production deployment guide (TBD)

## 🗂️ Code Organization

### Backend (Jac)

**Data Models** (`backend/models/`)
- `user.jac` - User, UserProgress, studied_lesson edge
- `lesson.jac` - Lesson, LessonContent, CodeExercise
- `quiz.jac` - Quiz, Question (4 types), QuizAttempt
- `osp_graph.jac` - OSPNode, MasteryNode, knowledge edges

**Walkers** (`backend/walkers/`)
- `progress.jac` - ProgressTracker, MasteryAggregator
  - Track lesson completion
  - Calculate proficiency scores
  - Identify weak areas
  
- `content.jac` - ContentServer, ContentValidator
  - Deliver lesson content
  - Validate prerequisites
  - Grade exercises
  
- `quiz.jac` - QuizGenerator, QuizAssessor, AdaptiveQuizEngine
  - Generate quizzes (byLLM)
  - Evaluate answers (byLLM)
  - Adjust difficulty dynamically

**Adaptive Agents** (`backend/agents/`)
- `learning_optimizer.jac` - LearningPathOptimizer, RevisionPlanner, SkillAssessment
  - Analyze learning graphs (byLLM)
  - Recommend lessons (byLLM)
  - Plan spaced repetition (byLLM)

**API Service** (`backend/`)
- `app.py` - Flask API with 15+ endpoints
- `sample_data.py` - Pre-built lessons, quizzes, concepts
- `requirements.txt` - Python dependencies

### Frontend (React)

**Components** (`frontend/src/components/`)
- `LessonViewer.jsx` (250 lines) - Display lesson sections, track completion
- `CodeEditor.jsx` (220 lines) - Edit and test code exercises
- `QuizComponent.jsx` (350 lines) - Quiz interface with adaptive feedback
- `ProgressDashboard.jsx` (280 lines) - Learning analytics and recommendations
- `SkillMap.jsx` (240 lines) - Visual mastery representation

**Services** (`frontend/src/services/`)
- `walkerService.js` - Utilities for calling backend walkers

**Configuration**
- `package.json` - Dependencies and scripts
- `src/index.js` - Entry point

### Shared
- `shared/constants.js` - Shared enums and type definitions

## 🔍 Finding Specific Features

### Learning a Lesson
1. **User interface**: `frontend/src/components/LessonViewer.jsx`
2. **Backend logic**: `backend/walkers/content.jac` (ContentServer)
3. **Data model**: `backend/models/lesson.jac`
4. **API endpoint**: `backend/app.py` - `GET /api/lessons/{id}`

### Taking a Quiz
1. **User interface**: `frontend/src/components/QuizComponent.jsx`
2. **Question generation**: `backend/walkers/quiz.jac` (QuizGenerator with @by_llm)
3. **Answer evaluation**: `backend/walkers/quiz.jac` (QuizAssessor with @by_llm)
4. **Progress update**: `backend/walkers/progress.jac` (ProgressTracker)
5. **API endpoints**: `backend/app.py` - Multiple quiz routes

### Viewing Progress
1. **User interface**: `frontend/src/components/ProgressDashboard.jsx`
2. **Data aggregation**: `backend/walkers/progress.jac` (MasteryAggregator)
3. **Recommendations**: `backend/agents/learning_optimizer.jac` (byLLM)
4. **API endpoints**: `backend/app.py` - `/api/users/{id}/progress`, `/api/recommendations`

### Visualizing Skills
1. **User interface**: `frontend/src/components/SkillMap.jsx`
2. **Data generation**: `backend/walkers/progress.jac` (MasteryAggregator.generate_skill_map)
3. **Data model**: `backend/models/osp_graph.jac` (OSPNode, MasteryNode)
4. **API endpoint**: `backend/app.py` - `GET /api/users/{id}/skill-map`

### Exercising Code
1. **User interface**: `frontend/src/components/CodeEditor.jsx`
2. **Validation logic**: `backend/walkers/content.jac` (ContentValidator)
3. **Progress tracking**: `backend/walkers/progress.jac` (ProgressTracker)
4. **API endpoints**: `backend/app.py` - `/api/exercises/validate`, `/api/exercises/submit`

## 🚀 Development Workflows

### Running Locally
```bash
# See QUICKSTART.md for detailed steps
# Backend: python backend/app.py
# Frontend: npm start (in frontend/)
```

### Adding New Lessons
1. Define lesson in `backend/sample_data.py`
2. Reference in `backend/models/lesson.jac` (if new lesson type)
3. Add quiz in `backend/sample_data.py`
4. Update recommendations in `learning_optimizer.jac`

### Creating New Walkers
1. Follow patterns in `docs/WALKER_GUIDE.md`
2. Define in appropriate file: `backend/walkers/` or `backend/agents/`
3. Add Flask route in `backend/app.py` to expose
4. Update frontend components to call if needed

### Building New Components
1. Create in `frontend/src/components/`
2. Import API calls from Flask
3. Use existing walkers or create new ones
4. Add CSS styling in same directory

## 📊 Data Flow Paths

### Complete Learning Path
```
LessonViewer → ContentServer → Update UserProgress → 
Show completion → Trigger quiz → QuizGenerator → 
QuizComponent → Answer questions → QuizAssessor → 
Score quiz → Update MasteryNode → Update Dashboard →
LearningPathOptimizer → Show recommendations
```

### Adaptive Learning Path
```
View ProgressDashboard → MasteryAggregator (aggregate) →
LearningPathOptimizer (analyze) → Identify weak areas →
RevisionPlanner (schedule) → Get recommendations → 
Suggest specific lessons & review material
```

### Code Exercise Path
```
CodeEditor → Submit code → ContentValidator → 
Run tests → Return results → Show feedback → 
ProgressTracker (update) → Update mastery
```

## 🧠 Key Concepts

### Walkers
Mobile agents that traverse graphs. See `docs/WALKER_GUIDE.md` for:
- How to implement walkers
- byLLM decorator usage
- Common patterns
- Testing approaches

### byLLM
Decorator for LLM-powered abilities. Used in:
- `QuizGenerator` - Create questions
- `QuizAssessor` - Evaluate answers
- `LearningPathOptimizer` - Recommend lessons
- `RevisionPlanner` - Schedule reviews
- `SkillAssessment` - Assess readiness

### OSP (Object-Spatial-Paradigm)
Jac's core approach to computation:
- Nodes = entities
- Edges = relationships
- Walkers = traversal
- Mastery = proficiency scores

See `backend/models/osp_graph.jac` for implementation.

### Adaptive Learning Algorithm
```
Mastery = (Quiz Performance × 0.7) + (Practice Time × 0.3)
Difficulty adjusts based on: correct streaks, wrong streaks
Spaced repetition schedules reviews by: time + mastery
```

See `backend/walkers/progress.jac` for details.

## 🔗 Quick Links

### Files to Start With
1. [`README.md`](README.md) - Overview
2. [`QUICKSTART.md`](QUICKSTART.md) - Setup
3. [`backend/sample_data.py`](backend/sample_data.py) - Sample content
4. [`backend/app.py`](backend/app.py) - API endpoints
5. [`frontend/src/components/LessonViewer.jsx`](frontend/src/components/LessonViewer.jsx) - Main component

### Understanding the Architecture
1. [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) - System design
2. [`VISUAL_GUIDE.md`](VISUAL_GUIDE.md) - Diagrams
3. [`docs/WALKER_GUIDE.md`](docs/WALKER_GUIDE.md) - Walker patterns

### Implementing Features
1. [`docs/WALKER_GUIDE.md`](docs/WALKER_GUIDE.md) - New walkers
2. [`backend/walkers/`](backend/walkers/) - Example walkers
3. [`frontend/src/components/`](frontend/src/components/) - Example components

## 📈 Learning Path

### For Students
1. Read [`README.md`](README.md) - Understand what you're learning
2. Follow [`QUICKSTART.md`](QUICKSTART.md) - Get platform running
3. Explore lessons and quizzes
4. Check progress dashboard
5. View skill map to track mastery

### For Developers
1. Read [`README.md`](README.md) - Understand platform
2. Follow [`QUICKSTART.md`](QUICKSTART.md) - Get running
3. Study [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) - System design
4. Review [`backend/models/`](backend/models/) - Data structures
5. Study [`backend/walkers/`](backend/walkers/) - Core logic
6. Explore [`docs/WALKER_GUIDE.md`](docs/WALKER_GUIDE.md) - Implementation patterns
7. Check [`frontend/src/components/`](frontend/src/components/) - UI patterns
8. Start building!

### For Instructors
1. Read [`README.md`](README.md) - Platform capabilities
2. Check [`backend/sample_data.py`](backend/sample_data.py) - Existing content
3. Review [`docs/WALKER_GUIDE.md`](docs/WALKER_GUIDE.md) - How content is processed
4. Add new lessons (edit sample_data.py)
5. Monitor student progress (ProgressDashboard)
6. Customize learning paths (LearningPathOptimizer)

## 🆘 Troubleshooting

**Port already in use?**
→ See QUICKSTART.md, "Port 5000 already in use"

**Import errors?**
→ Install dependencies:
```bash
pip install -r backend/requirements.txt  # Backend
npm install  # Frontend (in frontend/)
```

**Walker not working?**
→ Check:
1. Syntax in `backend/walkers/` file
2. Flask route calls correct walker
3. Parameters match walker definition
4. See `docs/WALKER_GUIDE.md` for patterns

**Component issues?**
→ Check:
1. API endpoint exists in `backend/app.py`
2. Endpoint calls correct walker
3. Response format matches component expectations

## 📞 Support

- **Setup issues**: [`QUICKSTART.md`](QUICKSTART.md)
- **Architecture questions**: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- **Implementation help**: [`docs/WALKER_GUIDE.md`](docs/WALKER_GUIDE.md)
- **API details**: [`backend/app.py`](backend/app.py) (inline comments)
- **Component examples**: [`frontend/src/components/`](frontend/src/components/)

---

## 📋 File Map

```
README.md ─────────────┐
QUICKSTART.md ────────┐│
VISUAL_GUIDE.md ──────┼┼─→ Start here for overview
PROJECT_SUMMARY.md ───┼│
docs/ARCHITECTURE.md ─┤│
docs/WALKER_GUIDE.md ─┤└─→ Study for deep understanding
docs/API_REFERENCE.md ┤
docs/DEPLOYMENT.md ───┤

backend/models/ ──────┐
backend/walkers/ ─────┼─→ Read for implementation
backend/agents/ ──────┤
backend/app.py ───────┴

frontend/src/components/ ──────┐
frontend/src/services/ ────────┼─→ Read for UI patterns
shared/constants.js ───────────┴
```

---

**Navigate using this guide to find exactly what you need!**

Questions? Check the relevant section above or review the source code directly.
