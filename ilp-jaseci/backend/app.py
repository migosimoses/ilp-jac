"""
Backend API Service for Interactive Learning Platform
Integrates with Jac walkers via Spawn() calls
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# ============================================================================
# LESSON ENDPOINTS
# ============================================================================

@app.route('/api/lessons/<lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    """
    Fetch lesson content using ContentServer walker
    """
    user_id = request.headers.get('X-User-ID')
    
    # Here you would call the Jac walker:
    # result = spawn('ContentServer', {
    #     'user_id': user_id,
    #     'lesson_id': lesson_id
    # }).get_lesson_content()
    
    # Mock response for demonstration
    return jsonify({
        'lessonId': lesson_id,
        'title': 'Introduction to Jac Basics',
        'description': 'Learn the fundamentals of Jac language',
        'difficulty': 'beginner',
        'durationMinutes': 30,
        'sections': [
            {
                'sectionNum': 1,
                'sectionTitle': 'What is Jac?',
                'body': '<p>Jac is a language designed for graph-based programming...</p>',
                'codeExample': 'node Person {\n    has name: str;\n}',
                'keyConcepts': ['nodes', 'graphs', 'spatial paradigm']
            },
            {
                'sectionNum': 2,
                'sectionTitle': 'Your First Node',
                'body': '<p>Let\'s create our first node...</p>',
                'codeExample': 'node Message {\n    has text: str;\n}',
                'keyConcepts': ['node definition', 'attributes']
            }
        ]
    })

@app.route('/api/lessons/category/<category>', methods=['GET'])
def get_lessons_by_category(category):
    """
    Get all lessons in a category using ContentServer walker
    """
    user_id = request.headers.get('X-User-ID')
    
    # Call ContentServer.get_lesson_by_category()
    
    return jsonify({
        'category': category,
        'lessons': [
            {
                'lessonId': 'jac-basics-1',
                'title': 'Introduction to Jac',
                'difficulty': 'beginner',
                'durationMinutes': 30
            }
        ]
    })

# ============================================================================
# PROGRESS & TRACKING ENDPOINTS
# ============================================================================

@app.route('/api/progress/track', methods=['POST'])
def track_progress():
    """
    Track lesson completion using ProgressTracker walker
    """
    data = request.get_json()
    user_id = data.get('userId')
    lesson_id = data.get('lessonId')
    status = data.get('status')
    time_spent = data.get('timeSpent')
    
    # Call ProgressTracker.track_lesson_progress()
    # Call ProgressTracker.calculate_proficiency()
    # Call ProgressTracker.update_mastery_score()
    
    return jsonify({
        'success': True,
        'message': f'Tracked progress for lesson {lesson_id}',
        'proficiency': 0.85,
        'masteryScore': 0.8
    })

@app.route('/api/users/<user_id>/progress', methods=['GET'])
def get_user_progress(user_id):
    """
    Get overall user progress using MasteryAggregator walker
    """
    
    # Call MasteryAggregator.aggregate_mastery()
    # Call MasteryAggregator.identify_weak_areas()
    
    return jsonify({
        'userId': user_id,
        'overallProgress': 65,
        'lessonsCompleted': 12,
        'totalLessons': 20,
        'avgQuizScore': 78.5,
        'currentStreak': 7,
        'hoursThisWeek': 5.5,
        'hoursThisMonth': 22,
        'totalHours': 45,
        'recentLessons': [
            {
                'title': 'Walkers and Traversal',
                'category': 'walkers',
                'status': 'completed',
                'completedDate': '2 days ago'
            },
            {
                'title': 'Advanced OSP Patterns',
                'category': 'osp',
                'status': 'in_progress'
            }
        ],
        'weakAreas': [
            {
                'conceptName': 'Advanced Walkers',
                'proficiency': 0.45
            },
            {
                'conceptName': 'Edge Mutations',
                'proficiency': 0.55
            }
        ]
    })

@app.route('/api/users/<user_id>/skill-map', methods=['GET'])
def get_skill_map(user_id):
    """
    Get skill map visualization using MasteryAggregator walker
    """
    
    # Call MasteryAggregator.generate_skill_map()
    
    return jsonify({
        'userId': user_id,
        'concepts': [
            {
                'conceptId': 'nodes-basics',
                'conceptName': 'Node Basics',
                'category': 'core',
                'description': 'Understanding graph nodes in Jac',
                'masteryScore': 0.95,
                'isUnlocked': True,
                'unlockThreshold': 0.7,
                'timesPracticed': 15,
                'lastPracticed': '1 day ago',
                'strength': 'mastered'
            },
            {
                'conceptId': 'walkers',
                'conceptName': 'Walkers',
                'category': 'core',
                'description': 'Graph traversal and walker patterns',
                'masteryScore': 0.65,
                'isUnlocked': True,
                'unlockThreshold': 0.7,
                'timesPracticed': 8,
                'lastPracticed': '2 days ago',
                'strength': 'developing'
            },
            {
                'conceptId': 'by-llm',
                'conceptName': 'byLLM Agents',
                'category': 'advanced',
                'description': 'Using LLM decorators for AI integration',
                'masteryScore': 0.35,
                'isUnlocked': False,
                'unlockThreshold': 0.8,
                'timesPracticed': 2,
                'lastPracticed': None,
                'strength': 'weak'
            }
        ]
    })

# ============================================================================
# QUIZ ENDPOINTS
# ============================================================================

@app.route('/api/quizzes/<quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    """
    Fetch or generate quiz using QuizGenerator walker
    """
    user_id = request.headers.get('X-User-ID')
    
    # Call QuizGenerator.generate_quiz() if needed
    
    return jsonify({
        'quizId': quiz_id,
        'title': 'Jac Fundamentals Quiz',
        'description': 'Test your knowledge of Jac basics',
        'difficulty': 'beginner',
        'questions': [
            {
                'questionId': 'q1',
                'questionText': 'What is a node in Jac?',
                'questionType': 'multiple_choice',
                'options': [
                    'A data structure that represents a vertex in a graph',
                    'A function definition',
                    'A type of variable',
                    'A control flow statement'
                ]
            },
            {
                'questionId': 'q2',
                'questionText': 'Walkers are used to traverse graphs.',
                'questionType': 'true_false'
            },
            {
                'questionId': 'q3',
                'questionText': 'Explain the concept of spatial programming.',
                'questionType': 'free_text'
            }
        ]
    })

@app.route('/api/quizzes/evaluate-answer', methods=['POST'])
def evaluate_answer():
    """
    Evaluate quiz answer using QuizAssessor walker
    """
    data = request.get_json()
    question_id = data.get('questionId')
    user_answer = data.get('userAnswer')
    question_type = data.get('questionType')
    
    # Based on question type, call appropriate QuizAssessor method:
    # - evaluate_free_text_answer() for free_text
    # - evaluate_code_answer() for code
    # - evaluate_multiple_choice() for multiple_choice
    
    if question_type == 'free_text':
        # Call QuizAssessor.evaluate_free_text_answer()
        is_correct = len(user_answer) > 10  # Simple heuristic
    elif question_type == 'multiple_choice':
        is_correct = user_answer == 'A data structure that represents a vertex in a graph'
    else:
        is_correct = user_answer == 'true'
    
    return jsonify({
        'correct': is_correct,
        'feedback': {
            'correct': is_correct,
            'message': 'Great job!' if is_correct else 'Not quite right.',
            'explanation': 'Nodes are vertices in a graph that can hold data...'
        }
    })

@app.route('/api/quizzes/score', methods=['POST'])
def score_quiz():
    """
    Calculate quiz score using QuizAssessor walker
    """
    data = request.get_json()
    quiz_id = data.get('quizId')
    user_id = data.get('userId')
    
    # Call QuizAssessor.score_quiz_attempt()
    # Call ProgressTracker.update_mastery_score()
    
    total_questions = len(data.get('answers', {}))
    # Count correct answers from feedback
    correct = sum(1 for f in data.get('feedback', {}).values() if f.get('correct'))
    
    score = (correct / total_questions * 100) if total_questions > 0 else 0
    
    return jsonify({
        'quizId': quiz_id,
        'score': score,
        'correctAnswers': correct,
        'totalQuestions': total_questions,
        'passed': score >= 70
    })

# ============================================================================
# RECOMMENDATIONS ENDPOINTS
# ============================================================================

@app.route('/api/users/<user_id>/recommendations', methods=['GET'])
def get_recommendations(user_id):
    """
    Get learning recommendations using LearningPathOptimizer walker
    """
    
    # Call LearningPathOptimizer.analyze_learning_graph()
    # Call LearningPathOptimizer.recommend_next_lesson()
    # Call LearningPathOptimizer.identify_struggle_areas()
    
    return jsonify({
        'userId': user_id,
        'nextLessons': [
            {
                'lessonId': 'advanced-walkers-1',
                'title': 'Advanced Walker Patterns',
                'difficulty': 'intermediate',
                'durationMinutes': 45,
                'category': 'walkers'
            },
            {
                'lessonId': 'osp-advanced-1',
                'title': 'Complex OSP Structures',
                'difficulty': 'advanced',
                'durationMinutes': 60,
                'category': 'osp'
            }
        ],
        'reasons': [
            'You\'ve mastered walker basics. Time for advanced patterns!',
            'Recommended for deepening your OSP knowledge.'
        ],
        'strugglingConcepts': [
            {
                'conceptName': 'Edge Mutations',
                'recommendation': 'Review the edge mutation tutorial'
            }
        ]
    })

# ============================================================================
# EXERCISE ENDPOINTS
# ============================================================================

@app.route('/api/exercises/validate', methods=['POST'])
def validate_code_exercise():
    """
    Validate code exercise using ContentValidator walker
    """
    data = request.get_json()
    exercise_id = data.get('exerciseId')
    code = data.get('code')
    
    # Call ContentValidator.validate_code_exercise()
    # Run code against test cases
    
    return jsonify({
        'exerciseId': exercise_id,
        'allPassed': True,
        'passedTests': 3,
        'totalTests': 3,
        'testDetails': [
            {'name': 'Test 1: Basic node creation', 'passed': True},
            {'name': 'Test 2: Node attributes', 'passed': True},
            {'name': 'Test 3: Edge creation', 'passed': True}
        ]
    })

@app.route('/api/exercises/submit', methods=['POST'])
def submit_exercise():
    """
    Submit exercise solution using ProgressTracker walker
    """
    data = request.get_json()
    exercise_id = data.get('exerciseId')
    user_id = data.get('userId')
    
    # Call ProgressTracker.track_lesson_progress()
    # Call ProgressTracker.update_mastery_score()
    
    return jsonify({
        'success': True,
        'exerciseId': exercise_id,
        'message': 'Exercise submitted successfully!',
        'pointsEarned': 10
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
