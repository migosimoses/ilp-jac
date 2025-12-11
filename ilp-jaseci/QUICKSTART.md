# Quick Start Guide

## 🚀 Get Up and Running in 5 Minutes

### Step 1: Setup Backend

```bash
# Navigate to backend directory
cd ilp-jaseci/backend

# Install dependencies
pip install -r requirements.txt

# Start the Flask API server
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 2: Setup Frontend

In a **new terminal**:

```bash
# Navigate to frontend directory
cd ilp-jaseci/frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

Your browser should open to `http://localhost:3000`

### Step 3: Try It Out

1. **View a Lesson**:
   - Click "Lessons" in the sidebar
   - Select "Jac Basics"
   - Navigate through sections

2. **Take a Quiz**:
   - Click "Quizzes" in the sidebar
   - Start "Jac Basics Quiz"
   - Answer questions (evaluates in real-time)

3. **Check Progress**:
   - Click "Progress Dashboard"
   - View stats, weak areas, recommendations

4. **Visualize Skills**:
   - Click "Skill Map"
   - See mastery levels for each concept

## 📝 Sample User Journey

### As a Beginner Learning Jac:

1. **Day 1**: Complete "What is Jac?" lesson
   - Read about OSP, graphs, walkers
   - 5 minutes → Quiz generated → Score 80%
   - Mastery for "OSP" updated to 0.8

2. **Day 2**: Complete "Nodes and Edges" lesson
   - Code examples and exercises
   - 10 minutes → Code exercise graded
   - Unlock intermediate content

3. **Day 3**: System recommends "Walker Basics"
   - Based on proficiency, identifies as ready
   - 15 minutes → Quiz with 3 adaptive questions
   - Score leads to "Advanced Walkers" unlock

4. **Week 1**: Progress Dashboard shows
   - 5 lessons completed (25%)
   - Average quiz score: 82%
   - Weak area: Edge mutations (recommend review)
   - Next: Advanced OSP Patterns

## 🔌 API Examples

### Get Lesson Content
```bash
curl http://localhost:5000/api/lessons/jac-basics-1 \
  -H "X-User-ID: user123"
```

### Submit Quiz Answer
```bash
curl -X POST http://localhost:5000/api/quizzes/evaluate-answer \
  -H "Content-Type: application/json" \
  -d '{
    "quizId": "quiz-1",
    "questionId": "q1",
    "userAnswer": "Object-Spatial-Paradigm",
    "questionType": "multiple_choice"
  }'
```

### Get User Recommendations
```bash
curl http://localhost:5000/api/users/user123/recommendations \
  -H "X-User-ID: user123"
```

## 📂 Key Files to Explore

### Backend (Jac)
- `backend/models/` - Data structure definitions
- `backend/walkers/` - Graph traversal and processing logic
- `backend/agents/` - AI-powered learning agents

### Frontend (React)
- `frontend/src/components/LessonViewer.jsx` - Lesson display
- `frontend/src/components/QuizComponent.jsx` - Quiz interface
- `frontend/src/components/ProgressDashboard.jsx` - Analytics
- `frontend/src/components/SkillMap.jsx` - Mastery visualization

### Configuration
- `backend/app.py` - Flask API routes
- `backend/sample_data.py` - Example lessons and quizzes
- `frontend/package.json` - Frontend dependencies

## 🛠️ Common Tasks

### Add a New Lesson

1. **Add lesson data** to `backend/sample_data.py`:
```python
{
    "lesson_id": "my-lesson",
    "title": "My Lesson",
    "category": "jac_basics",
    "sections": [...]
}
```

2. **Create lesson node** in `backend/models/lesson.jac` if needed

3. **Link from recommendations** in `LearningPathOptimizer` walker

### Create a New Quiz

1. **Add quiz data** to `backend/sample_data.py`:
```python
{
    "quiz_id": "my-quiz",
    "lesson_id": "my-lesson",
    "questions": [...]
}
```

2. **Update API endpoint** in `backend/app.py`:
```python
@app.route('/api/quizzes/my-quiz')
def get_my_quiz():
    # Return quiz data
```

### Add a New Walker Ability

1. **Implement in** `backend/walkers/`:
```jac
can new_ability {
    # Your logic here
}
```

2. **Call from Flask** in `backend/app.py`:
```python
result = spawn('WalkerName', {...}).new_ability()
```

3. **Expose via API** endpoint

## 🧪 Testing

### Test a Walker Locally

```bash
cd ilp-jaseci
jac -m backend.walkers.progress
```

### Test an API Endpoint

```bash
curl http://localhost:5000/api/lessons/jac-basics-1 -H "X-User-ID: test"
```

### Test React Component

```bash
cd frontend
npm test -- LessonViewer
```

## 📚 Next Steps

1. **Customize lessons** - Add your own content
2. **Train byLLM agents** - Improve quiz generation
3. **Build advanced features** - Collaboration, certificates, etc.
4. **Deploy** - See DEPLOYMENT.md for production setup

## 🤔 Troubleshooting

### "Port 5000 already in use"
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use different port
python app.py --port 8000
```

### "Cannot find module"
```bash
# Make sure you installed dependencies
pip install -r backend/requirements.txt
npm install  # in frontend directory
```

### "Walker not found"
```bash
# Check walker is defined in backend/walkers/
# Check Flask route calls correct walker name
# Verify Jac syntax in walker definition
```

## 📞 Support

- See `README.md` for overview
- See `docs/ARCHITECTURE.md` for system design
- See `docs/WALKER_GUIDE.md` for implementation details
- See `docs/API_REFERENCE.md` for API documentation

---

**You're ready to go!** 🎉

Start building your adaptive learning platform with Jac & Jaseci.
