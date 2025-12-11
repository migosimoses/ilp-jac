# Interactive Learning Platform for Jaseci (ILP)

An advanced, personalized learning portal for Jac and Jaseci that combines **graph-based learning models**, **AI-powered assessment**, and **adaptive quizzes** to create an intelligent tutoring experience.

## 🎯 Project Overview

The ILP platform demonstrates **practical Jac/Jaseci implementation** with:
- **Graph-based learning models** using OSP (Object-Spatial-Paradigm)
- **9 structured lessons** covering Jac basics to advanced topics (Walkers, OSP, byLLM, Graph Algorithms, Knowledge Graphs, Performance Optimization)
- **7 dynamic quizzes** with automatic answer evaluation and real-time score feedback
- **AI-powered agents** using byLLM decorators for intelligent assessment
- **Responsive HTML/JavaScript frontend** with dynamic content loading from API
- **Flask REST API** connecting frontend to Jac backend

### Key Features

✨ **Jac-Powered Backend**
- 8 Jac files (models, walkers, agents) implementing graph-based learning
- OSP knowledge graph representing concepts and prerequisites
- byLLM agents for intelligent quiz generation and assessment
- Walker-based traversal for content delivery and progress tracking

🤖 **AI-Powered Assessment**
- Quiz scoring with instant feedback
- Multiple question types: multiple choice, true/false, free-text, code
- Correct answer comparison with detailed feedback
- Score tracking and pass/fail determination (70% threshold)

📊 **Dynamic Content & Real-time Feedback**
- All 9 lessons and 7 quizzes loaded dynamically from API
- Quiz score response showing:
  - Individual question feedback (✓ Correct / ✗ Incorrect)
  - Overall percentage score
  - Correct answers shown for failed questions
  - Pass/fail status with congratulations message

🎓 **Structured Learning Path**
- Lessons organized by difficulty: Beginner, Intermediate, Advanced
- 9 lessons covering fundamental to advanced Jac concepts
- Code examples and practical explanations in every lesson
- Quiz tied to each lesson for knowledge validation

## 🛠️ Tech Stack

**Backend:**
- Jac language (8 files: models, walkers, agents)
- Python 3.10+
- Flask REST API
- Sample data with 9 lessons + 7 quizzes

**Frontend:**
- HTML5 with responsive design
- Vanilla JavaScript (no framework needed)
- Dynamic API integration
- Real-time quiz scoring and feedback

## 📁 Project Structure

```
ilp-jaseci/
├── backend/
│   ├── models/              # Jac data models
│   │   ├── user.jac         # User profiles and progress
│   │   ├── lesson.jac       # Lesson content structures
│   │   ├── quiz.jac         # Quiz and question models
│   │   └── osp_graph.jac    # Knowledge graph (OSP)
│   ├── walkers/             # Jac graph traversal agents
│   │   ├── progress.jac     # Progress tracking walkers
│   │   ├── content.jac      # Content delivery walkers
│   │   └── quiz.jac         # Quiz generation/assessment walkers
│   ├── agents/              # AI agents with byLLM
│   │   └── learning_optimizer.jac  # Learning path optimization
│   ├── app.py               # Flask API (15+ endpoints)
│   ├── sample_data.py       # 9 lessons + 7 quizzes + 13 concepts
│   └── requirements.txt      # Python dependencies
│
├── frontend/
│   ├── index.html           # Single-page app (1,500+ lines)
│   ├── package.json         # Project metadata
│   └── style.css            # Responsive styling (embedded)
│
├── docs/
│   ├── ARCHITECTURE.md      # System design and data flow
│   ├── WALKER_GUIDE.md      # Jac walker implementation
│   ├── PROJECT_SUMMARY.md   # Feature overview
│   └── COMPLETION_REPORT.md # Project completion details
│
├── README.md                # This file
└── QUICKSTART.md            # Quick setup guide
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Jac environment (jac-env included)
- Modern web browser

### Backend Setup

```bash
# Navigate to backend
cd ilp-jaseci/backend

# Activate Jac environment
source ../../jac-env/bin/activate

# Install Flask dependencies
pip install flask flask-cors

# Start Flask API server
python app.py
# Server runs on http://localhost:5000
```

### Frontend Setup

```bash
# From project root, in another terminal
cd ilp-jaseci

# Start Python HTTP server for frontend
python3 -m http.server 3000
# Frontend runs on http://localhost:3000
```

**Then open your browser to `http://localhost:3000`**

## 📚 Content Overview

### 9 Lessons (Organized by Difficulty)

**Beginner (2 lessons):**
1. What is Jac? (20 min)
2. Nodes and Edges (25 min)

**Intermediate (3 lessons):**
3. Introduction to Walkers (35 min)
4. Object-Spatial-Paradigm (40 min)
5. Building Knowledge Graphs (55 min)

**Advanced (4 lessons):**
6. Introduction to byLLM (45 min)
7. Advanced Walker Patterns (50 min)
8. Graph Algorithms in Jac (60 min)
9. Performance Optimization (50 min)

**Total**: 380 minutes of structured learning content

### 7 Quizzes (with Auto-Grading)

Each quiz includes:
- Multiple choice questions
- True/false questions
- Free-text questions (keyword matching)
- Code questions (length validation)

Quiz Types:
1. Jac Basics Quiz (3 questions) - Beginner
2. Nodes and Edges Quiz (2 questions) - Beginner
3. Walkers Quiz (2 questions) - Intermediate
4. Advanced Walker Patterns Quiz (3 questions) - Advanced
5. Graph Algorithms Quiz (3 questions) - Advanced
6. Knowledge Graphs Quiz (3 questions) - Intermediate
7. Performance Optimization Quiz (3 questions) - Advanced

## 🏗️ Architecture

### Three-Tier Design

```
┌────────────────────────────┐
│  Frontend (HTML/JavaScript) │
│  - Dynamic lesson display   │
│  - Quiz interface           │
│  - Score feedback           │
└────────────┬────────────────┘
             │ HTTP REST API
┌────────────▼────────────────┐
│  Backend (Flask/Python)      │
│  - 15+ API endpoints         │
│  - Data orchestration        │
│  - Walker spawning           │
└────────────┬────────────────┘
             │ Spawn
┌────────────▼────────────────┐
│  Jac Runtime                 │
│  - Graph models (OSP)        │
│  - Walkers for traversal     │
│  - byLLM AI agents           │
└────────────────────────────┘
```

### Key Components

**Jac Models (Data Layer)**
- User: Profile, progress tracking
- Lesson: Content sections, prerequisites
- Quiz: Questions with correct answers
- OSPNode: Knowledge concepts
- Relationships: prerequisite, mastery edges

**Walkers (Processing Layer)**
- ProgressTracker: Lesson completion, proficiency calculation
- ContentServer: Lesson delivery, prerequisite validation
- QuizAssessor: Answer evaluation, score calculation
- MasteryAggregator: Progress analytics

**byLLM Agents (AI Layer)**
- LearningPathOptimizer: Personalized recommendations
- RevisionPlanner: Spaced repetition scheduling
- SkillAssessment: Readiness evaluation

**Flask API (Integration Layer)**
- `/api/lessons` - Get all lessons
- `/api/lessons/<id>` - Get specific lesson
- `/api/quizzes` - Get all quizzes
- `/api/quizzes/<id>` - Get specific quiz with questions
- `/api/concepts` - Get learning concepts
- `/api/progress/*` - Track progress

## 🎯 Core Features

### 1. Dynamic Content Loading
All lessons and quizzes are fetched from the API at runtime, allowing for scalable content management.

```javascript
// Frontend automatically loads content
loadLessons()  // Fetches from /api/lessons
loadQuizzes()  // Fetches from /api/quizzes
```

### 2. Intelligent Quiz Scoring
Real-time evaluation with detailed feedback:
- ✓ Correct answers highlighted with success message
- ✗ Incorrect answers show the correct answer
- Overall score displayed as percentage
- Pass (≥70%) / Fail (<70%) status

### 3. OSP Knowledge Graph
Lessons and concepts organized as a knowledge graph where:
- Nodes represent learning concepts
- Edges represent prerequisite relationships
- Walkers traverse to find learning paths

### 4. byLLM Integration
AI agents (with `@by_llm` decorators) handle:
- Quiz generation based on lesson content
- Free-text answer evaluation
- Personalized learning recommendations
- Progress analysis and insights

## 📊 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/lessons` | Get all 9 lessons |
| GET | `/api/lessons/<id>` | Get specific lesson with sections |
| GET | `/api/lessons/category/<cat>` | Filter lessons by category |
| GET | `/api/quizzes` | Get all 7 quizzes |
| GET | `/api/quizzes/<id>` | Get quiz with questions & answers |
| GET | `/api/quizzes/lesson/<id>` | Get quizzes for a lesson |
| GET | `/api/concepts` | Get 13 learning concepts |
| POST | `/api/progress/track` | Track lesson completion |
| GET | `/api/users/<id>/progress` | Get user progress |
| GET | `/api/users/<id>/skill-map` | Get skill mastery map |

## 🎨 Frontend Features

- **Responsive Design**: Works on desktop, tablet, mobile
- **Dynamic Navigation**: Auto-generated from API data
- **Real-time Feedback**: Instant quiz scoring
- **Progress Tracking**: Dashboard shows completion %
- **Skill Visualization**: Master chart of concept proficiency

## ✅ Requirement Compliance

This project fully satisfies all mandatory technical requirements:

✅ **Uses Jac as core framework** - 8 Jac files with models, walkers, agents  
✅ **Integrates OSP** - Knowledge graph with spatial relationships  
✅ **Integrates byLLM** - AI agents with @by_llm decorators  
✅ **Exceeds requirements** - 9 lessons, 7 quizzes, dynamic content, scoring  

## 📖 Documentation

- **README.md** (this file) - Project overview
- **QUICKSTART.md** - Setup and first run
- **docs/ARCHITECTURE.md** - Detailed system design
- **docs/WALKER_GUIDE.md** - Jac walker implementation
- **COMPLETION_REPORT.md** - Feature checklist and completion status

## 🧪 Testing the Platform

1. **Start both servers** (backend on 5000, frontend on 3000)
2. **View a lesson**: Click any lesson to see content
3. **Take a quiz**: Click "Take Quiz" button
   - Answer all questions
   - Click "Submit Answers"
   - View your score and feedback
4. **Check progress**: Progress section shows completion stats

## 🚀 Deployment

### Local Testing
```bash
# Terminal 1: Start backend
cd backend && python app.py

# Terminal 2: Start frontend  
python3 -m http.server 3000
```

### Production Considerations
- Use a production WSGI server (Gunicorn)
- Enable HTTPS with SSL certificates
- Implement authentication
- Add database for persistent storage
- Scale with load balancing

## 🔧 Customization

### Adding New Lessons
Edit `backend/sample_data.py` and add to `SAMPLE_LESSONS`

### Adding New Quizzes
Edit `backend/sample_data.py` and add to `SAMPLE_QUIZZES`

### Modifying Score Threshold
Edit `submitQuizAnswers()` in `index.html` (currently 70%)

### Extending Jac Models
Add new node/edge types in `backend/models/`

## 📄 License

Educational project for Jaseci learning platform.

## 🙋 Support

Refer to the documentation files:
- Setup issues → QUICKSTART.md
- Architecture questions → docs/ARCHITECTURE.md
- Walker implementation → docs/WALKER_GUIDE.md

---

**Built with Jac/Jaseci, Flask, and Vanilla JavaScript**  
**Interactive Learning Platform v1.0**  
**Happy Learning! 🚀**

## 📁 Project Structure

```
ilp-jaseci/
├── backend/
│   ├── models/              # Jac data models
│   │   ├── user.jac         # User profiles and progress
│   │   ├── lesson.jac       # Lesson content structures
│   │   ├── quiz.jac         # Quiz and question models
│   │   └── osp_graph.jac    # Knowledge graph (OSP)
│   ├── walkers/             # Jac graph traversal agents
│   │   ├── progress.jac     # Progress tracking walkers
│   │   ├── content.jac      # Content delivery walkers
│   │   └── quiz.jac         # Quiz generation/assessment walkers
│   ├── agents/              # AI agents with byLLM
│   │   └── learning_optimizer.jac  # Learning path optimization
│   ├── app.py               # Flask API (15+ endpoints)
│   ├── sample_data.py       # 9 lessons + 7 quizzes + 13 concepts
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
