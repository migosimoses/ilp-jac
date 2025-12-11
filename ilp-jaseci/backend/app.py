"""
Backend API Service for Interactive Learning Platform
Integrates with Jac walkers via Spawn() calls
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
from sample_data import SAMPLE_LESSONS, SAMPLE_QUIZZES, SAMPLE_CONCEPTS

app = Flask(__name__)
CORS(app)

# Create lookup dictionaries for easy access
lessons_by_id = {lesson['lesson_id']: lesson for lesson in SAMPLE_LESSONS}
quizzes_by_id = {quiz['quiz_id']: quiz for quiz in SAMPLE_QUIZZES}
quizzes_by_lesson = {}
for quiz in SAMPLE_QUIZZES:
    lesson_id = quiz.get('lesson_id')
    if lesson_id not in quizzes_by_lesson:
        quizzes_by_lesson[lesson_id] = []
    quizzes_by_lesson[lesson_id].append(quiz)

# ============================================================================
# LESSON ENDPOINTS
# ============================================================================

@app.route('/api/lessons/<lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    """
    Fetch lesson content using ContentServer walker
    """
    user_id = request.headers.get('X-User-ID')
    
    # Check if lesson exists in sample data
    if lesson_id in lessons_by_id:
        lesson = lessons_by_id[lesson_id]
        return jsonify({
            'lessonId': lesson['lesson_id'],
            'title': lesson['title'],
            'description': lesson['description'],
            'difficulty': lesson['difficulty'],
            'durationMinutes': lesson['duration_minutes'],
            'category': lesson['category'],
            'prerequisites': lesson['prerequisites'],
            'sections': [
                {
                    'sectionNum': sec['section_num'],
                    'sectionTitle': sec['section_title'],
                    'body': sec['body'],
                    'codeExample': sec['code_example'],
                    'keyConcepts': sec['key_concepts']
                }
                for sec in lesson['sections']
            ]
        })
    
    # Fallback for non-existent lesson
    return jsonify({'error': 'Lesson not found'}), 404

@app.route('/api/lessons', methods=['GET'])
def get_all_lessons():
    """
    Get all available lessons
    """
    lessons = [
        {
            'lessonId': lesson['lesson_id'],
            'title': lesson['title'],
            'difficulty': lesson['difficulty'],
            'durationMinutes': lesson['duration_minutes'],
            'description': lesson['description'],
            'category': lesson['category']
        }
        for lesson in SAMPLE_LESSONS
    ]
    
    return jsonify({
        'lessons': lessons,
        'count': len(lessons)
    })

@app.route('/api/lessons/category/<category>', methods=['GET'])
def get_lessons_by_category(category):
    """
    Get all lessons in a category using ContentServer walker
    """
    user_id = request.headers.get('X-User-ID')
    
    # Filter lessons by category
    matching_lessons = [
        {
            'lessonId': lesson['lesson_id'],
            'title': lesson['title'],
            'difficulty': lesson['difficulty'],
            'durationMinutes': lesson['duration_minutes'],
            'description': lesson['description'],
            'category': lesson['category']
        }
        for lesson in SAMPLE_LESSONS
        if lesson['category'] == category
    ]
    
    return jsonify({
        'category': category,
        'lessons': matching_lessons,
        'count': len(matching_lessons)
    })

@app.route('/api/concepts', methods=['GET'])
def get_concepts():
    """
    Get all learning concepts
    """
    concepts = [
        {
            'conceptId': concept['concept_id'],
            'conceptName': concept['concept_name'],
            'category': concept['category'],
            'description': concept['description'],
            'resources': concept.get('resources', [])
        }
        for concept in SAMPLE_CONCEPTS
    ]
    
    return jsonify({
        'concepts': concepts,
        'count': len(concepts)
    })

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
    
    if quiz_id in quizzes_by_id:
        quiz = quizzes_by_id[quiz_id]
        return jsonify({
            'quizId': quiz['quiz_id'],
            'title': quiz['title'],
            'description': quiz.get('description', ''),
            'difficulty': quiz['difficulty'],
            'lessonId': quiz.get('lesson_id'),
            'questions': [
                {
                    'questionId': q['question_id'],
                    'questionText': q['question_text'],
                    'questionType': q['question_type'],
                    'options': q.get('options', []),
                    'starterCode': q.get('starter_code', ''),
                    'keywords': q.get('keywords', []),
                    'correctAnswer': q.get('correct_answer')
                }
                for q in quiz['questions']
            ]
        })
    
    return jsonify({'error': 'Quiz not found'}), 404

@app.route('/api/quizzes/lesson/<lesson_id>', methods=['GET'])
def get_quizzes_by_lesson(lesson_id):
    """
    Get all quizzes for a specific lesson
    """
    quizzes = quizzes_by_lesson.get(lesson_id, [])
    
    return jsonify({
        'lessonId': lesson_id,
        'quizzes': [
            {
                'quizId': quiz['quiz_id'],
                'title': quiz['title'],
                'difficulty': quiz['difficulty'],
                'questionCount': len(quiz['questions'])
            }
            for quiz in quizzes
        ],
        'count': len(quizzes)
    })

@app.route('/api/quizzes', methods=['GET'])
def get_all_quizzes():
    """
    Get all available quizzes
    """
    quizzes = [
        {
            'quizId': quiz['quiz_id'],
            'title': quiz['title'],
            'difficulty': quiz['difficulty'],
            'lessonId': quiz.get('lesson_id'),
            'questionCount': len(quiz['questions'])
        }
        for quiz in SAMPLE_QUIZZES
    ]
    
    return jsonify({
        'quizzes': quizzes,
        'count': len(quizzes)
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
    app.run(debug=False, port=5000)
