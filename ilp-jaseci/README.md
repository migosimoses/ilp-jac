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

