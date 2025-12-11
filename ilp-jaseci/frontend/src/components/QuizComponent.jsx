import React, { useState, useEffect } from 'react';
import './QuizComponent.css';

/**
 * QuizComponent
 * Displays quiz questions with adaptive difficulty
 * Integrates with QuizAssessor walker for answer evaluation
 */
const QuizComponent = ({ quizId, userId, onComplete }) => {
  const [quiz, setQuiz] = useState(null);
  const [currentQuestionIdx, setCurrentQuestionIdx] = useState(0);
  const [answers, setAnswers] = useState({});
  const [feedback, setFeedback] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [quizScore, setQuizScore] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchQuiz();
  }, [quizId, userId]);

  const fetchQuiz = async () => {
    try {
      setLoading(true);
      // Call QuizGenerator or fetch cached quiz
      const response = await fetch(`/api/quizzes/${quizId}`, {
        headers: { 'X-User-ID': userId }
      });
      const data = await response.json();
      setQuiz(data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching quiz:', error);
      setLoading(false);
    }
  };

  const handleAnswerChange = (questionId, answer) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: answer
    }));
  };

  const handleSubmitAnswer = async () => {
    const currentQuestion = quiz.questions[currentQuestionIdx];
    const userAnswer = answers[currentQuestion.questionId] || '';

    try {
      setIsSubmitting(true);
      // Call QuizAssessor walker to evaluate answer
      const response = await fetch('/api/quizzes/evaluate-answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          quizId,
          questionId: currentQuestion.questionId,
          userAnswer,
          questionType: currentQuestion.questionType,
          userId
        })
      });
      const result = await response.json();
      
      setFeedback(prev => ({
        ...prev,
        [currentQuestion.questionId]: result.feedback
      }));

      setIsSubmitting(false);

      // Move to next question after short delay
      setTimeout(() => {
        if (currentQuestionIdx < quiz.questions.length - 1) {
          setCurrentQuestionIdx(currentQuestionIdx + 1);
        } else {
          handleQuizComplete();
        }
      }, 2000);
    } catch (error) {
      console.error('Error submitting answer:', error);
      setIsSubmitting(false);
    }
  };

  const handleQuizComplete = async () => {
    try {
      // Score the quiz attempt
      const response = await fetch('/api/quizzes/score', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          quizId,
          userId,
          answers,
          feedback
        })
      });
      const result = await response.json();
      setQuizScore(result);

      if (onComplete) {
        onComplete({ quizId, score: result.score, passed: result.passed });
      }
    } catch (error) {
      console.error('Error completing quiz:', error);
    }
  };

  if (loading) return <div className="quiz-loading">Loading quiz...</div>;
  if (!quiz) return <div className="quiz-error">Quiz not found</div>;
  if (quizScore) return <QuizResults score={quizScore} />;

  const currentQuestion = quiz.questions[currentQuestionIdx];
  const currentFeedback = feedback[currentQuestion.questionId];

  return (
    <div className="quiz-container">
      <div className="quiz-header">
        <h2>{quiz.title}</h2>
        <div className="quiz-progress">
          Question {currentQuestionIdx + 1} of {quiz.questions.length}
        </div>
      </div>

      <div className="question-container">
        <h3>{currentQuestion.questionText}</h3>

        {currentQuestion.questionType === 'multiple_choice' && (
          <MultipleChoiceQuestion
            question={currentQuestion}
            answer={answers[currentQuestion.questionId]}
            onChange={(answer) => handleAnswerChange(currentQuestion.questionId, answer)}
          />
        )}

        {currentQuestion.questionType === 'true_false' && (
          <TrueFalseQuestion
            question={currentQuestion}
            answer={answers[currentQuestion.questionId]}
            onChange={(answer) => handleAnswerChange(currentQuestion.questionId, answer)}
          />
        )}

        {currentQuestion.questionType === 'free_text' && (
          <FreeTextQuestion
            question={currentQuestion}
            answer={answers[currentQuestion.questionId]}
            onChange={(answer) => handleAnswerChange(currentQuestion.questionId, answer)}
          />
        )}

        {currentQuestion.questionType === 'code' && (
          <CodeQuestion
            question={currentQuestion}
            answer={answers[currentQuestion.questionId]}
            onChange={(answer) => handleAnswerChange(currentQuestion.questionId, answer)}
          />
        )}
      </div>

      {currentFeedback && (
        <div className={`feedback ${currentFeedback.correct ? 'correct' : 'incorrect'}`}>
          <p>{currentFeedback.message}</p>
          {currentFeedback.explanation && (
            <p className="explanation">{currentFeedback.explanation}</p>
          )}
        </div>
      )}

      <div className="quiz-actions">
        <button
          onClick={handleSubmitAnswer}
          disabled={isSubmitting || !answers[currentQuestion.questionId]}
          className="btn btn-primary"
        >
          {isSubmitting ? 'Evaluating...' : 'Submit Answer'}
        </button>
      </div>
    </div>
  );
};

// Sub-component for multiple choice questions
const MultipleChoiceQuestion = ({ question, answer, onChange }) => (
  <div className="question-options">
    {question.options.map((option, idx) => (
      <label key={idx} className="option">
        <input
          type="radio"
          name="choice"
          value={option}
          checked={answer === option}
          onChange={(e) => onChange(e.target.value)}
        />
        {option}
      </label>
    ))}
  </div>
);

// Sub-component for true/false questions
const TrueFalseQuestion = ({ question, answer, onChange }) => (
  <div className="question-options">
    <label className="option">
      <input
        type="radio"
        name="tf"
        value="true"
        checked={answer === 'true'}
        onChange={(e) => onChange(e.target.value)}
      />
      True
    </label>
    <label className="option">
      <input
        type="radio"
        name="tf"
        value="false"
        checked={answer === 'false'}
        onChange={(e) => onChange(e.target.value)}
      />
      False
    </label>
  </div>
);

// Sub-component for free text questions
const FreeTextQuestion = ({ question, answer, onChange }) => (
  <textarea
    value={answer || ''}
    onChange={(e) => onChange(e.target.value)}
    placeholder="Enter your answer here..."
    className="free-text-input"
    rows={4}
  />
);

// Sub-component for code questions
const CodeQuestion = ({ question, answer, onChange }) => (
  <textarea
    value={answer || ''}
    onChange={(e) => onChange(e.target.value)}
    placeholder={question.starterCode}
    className="code-input"
    rows={8}
    spellCheck="false"
  />
);

// Results component
const QuizResults = ({ score }) => (
  <div className="quiz-results">
    <h2>Quiz Complete!</h2>
    <div className="score-display">
      <div className="score-percentage">{Math.round(score.score)}%</div>
      <div className="score-status">
        {score.passed ? '✓ Passed' : '✗ Try Again'}
      </div>
    </div>
    <p className="score-detail">You got {score.correctAnswers} out of {score.totalQuestions} correct</p>
  </div>
);

export default QuizComponent;
