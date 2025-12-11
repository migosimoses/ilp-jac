import React, { useState, useEffect } from 'react';
import './LessonViewer.css';

/**
 * LessonViewer Component
 * Displays lesson content with sections, code examples, and exercises
 */
const LessonViewer = ({ lessonId, userId }) => {
  const [lesson, setLesson] = useState(null);
  const [currentSection, setCurrentSection] = useState(0);
  const [isCompleted, setIsCompleted] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLessonContent();
  }, [lessonId, userId]);

  const fetchLessonContent = async () => {
    try {
      setLoading(true);
      // Call backend walker via spawn
      const response = await fetch('/api/lessons/' + lessonId, {
        method: 'GET',
        headers: { 'X-User-ID': userId }
      });
      const data = await response.json();
      setLesson(data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching lesson:', error);
      setLoading(false);
    }
  };

  const handleSectionNext = () => {
    if (currentSection < lesson.sections.length - 1) {
      setCurrentSection(currentSection + 1);
    }
  };

  const handleSectionPrev = () => {
    if (currentSection > 0) {
      setCurrentSection(currentSection - 1);
    }
  };

  const handleLessonComplete = async () => {
    try {
      // Call progress tracker walker
      await fetch('/api/progress/track', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          userId,
          lessonId,
          status: 'completed',
          timeSpent: calculateTimeSpent()
        })
      });
      setIsCompleted(true);
    } catch (error) {
      console.error('Error marking lesson complete:', error);
    }
  };

  const calculateTimeSpent = () => {
    // Calculate time spent on lesson
    return 0; // TODO: implement
  };

  if (loading) return <div className="lesson-viewer-loading">Loading lesson...</div>;
  if (!lesson) return <div className="lesson-viewer-error">Lesson not found</div>;

  const section = lesson.sections[currentSection];

  return (
    <div className="lesson-viewer">
      <div className="lesson-header">
        <h1>{lesson.title}</h1>
        <div className="lesson-meta">
          <span className="difficulty">{lesson.difficulty}</span>
          <span className="duration">{lesson.durationMinutes} min</span>
        </div>
      </div>

      <div className="lesson-content">
        <div className="section-counter">
          Section {currentSection + 1} of {lesson.sections.length}
        </div>

        <h2>{section.sectionTitle}</h2>
        <div className="section-body" dangerouslySetInnerHTML={{ __html: section.body }} />

        {section.codeExample && (
          <div className="code-example">
            <h3>Code Example</h3>
            <pre><code>{section.codeExample}</code></pre>
          </div>
        )}

        {section.keyConcepts && (
          <div className="key-concepts">
            <h3>Key Concepts</h3>
            <ul>
              {section.keyConcepts.map((concept, idx) => (
                <li key={idx}>{concept}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      <div className="lesson-navigation">
        <button
          onClick={handleSectionPrev}
          disabled={currentSection === 0}
          className="btn btn-secondary"
        >
          Previous
        </button>

        {currentSection === lesson.sections.length - 1 ? (
          <button
            onClick={handleLessonComplete}
            className="btn btn-primary"
            disabled={isCompleted}
          >
            {isCompleted ? 'Completed ✓' : 'Complete Lesson'}
          </button>
        ) : (
          <button onClick={handleSectionNext} className="btn btn-primary">
            Next
          </button>
        )}
      </div>

      {isCompleted && (
        <div className="completion-message">
          Great job! You've completed this lesson.
        </div>
      )}
    </div>
  );
};

export default LessonViewer;
