import React, { useState, useEffect } from 'react';
import './ProgressDashboard.css';

/**
 * ProgressDashboard Component
 * Shows overall learning progress, stats, and recommendations
 * Integrates with MasteryAggregator and LearningPathOptimizer walkers
 */
const ProgressDashboard = ({ userId }) => {
  const [progress, setProgress] = useState(null);
  const [recommendations, setRecommendations] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProgressData();
  }, [userId]);

  const fetchProgressData = async () => {
    try {
      setLoading(true);
      // Call MasteryAggregator and LearningPathOptimizer walkers
      const [progressRes, recRes] = await Promise.all([
        fetch(`/api/users/${userId}/progress`, {
          headers: { 'X-User-ID': userId }
        }),
        fetch(`/api/users/${userId}/recommendations`, {
          headers: { 'X-User-ID': userId }
        })
      ]);

      const progressData = await progressRes.json();
      const recData = await recRes.json();
      
      setProgress(progressData);
      setRecommendations(recData);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching progress data:', error);
      setLoading(false);
    }
  };

  if (loading) return <div className="progress-loading">Loading dashboard...</div>;
  if (!progress) return <div className="progress-error">Unable to load progress</div>;

  return (
    <div className="progress-dashboard">
      <div className="dashboard-header">
        <h1>Learning Progress</h1>
        <button className="refresh-btn" onClick={fetchProgressData}>
          Refresh
        </button>
      </div>

      {/* Statistics Cards */}
      <div className="stats-grid">
        <StatCard
          title="Overall Progress"
          value={`${Math.round(progress.overallProgress)}%`}
          icon="📊"
          color="blue"
        />
        <StatCard
          title="Lessons Completed"
          value={progress.lessonsCompleted}
          subtitle={`of ${progress.totalLessons}`}
          icon="✅"
          color="green"
        />
        <StatCard
          title="Average Quiz Score"
          value={`${Math.round(progress.avgQuizScore)}%`}
          icon="🎯"
          color="orange"
        />
        <StatCard
          title="Learning Streak"
          value={`${progress.currentStreak} days`}
          subtitle="Keep it going!"
          icon="🔥"
          color="red"
        />
      </div>

      {/* Learning Path Section */}
      <div className="learning-path-section">
        <h2>Your Learning Path</h2>
        <div className="lessons-timeline">
          {progress.recentLessons && progress.recentLessons.map((lesson, idx) => (
            <LessonTimelineItem
              key={idx}
              lesson={lesson}
              position={idx}
            />
          ))}
        </div>
      </div>

      {/* Weak Areas Section */}
      {progress.weakAreas && progress.weakAreas.length > 0 && (
        <div className="weak-areas-section">
          <h2>Areas to Improve</h2>
          <div className="weak-areas-list">
            {progress.weakAreas.map((area, idx) => (
              <div key={idx} className="weak-area-card">
                <h3>{area.conceptName}</h3>
                <div className="proficiency-bar">
                  <div
                    className="proficiency-fill"
                    style={{ width: `${area.proficiency * 100}%`, backgroundColor: '#f59e0b' }}
                  />
                </div>
                <p>{Math.round(area.proficiency * 100)}% mastered</p>
                <button className="review-btn">Review Resources →</button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recommendations Section */}
      {recommendations && (
        <div className="recommendations-section">
          <h2>Recommended Next Steps</h2>
          <div className="recommendations-list">
            {recommendations.nextLessons && recommendations.nextLessons.map((lesson, idx) => (
              <RecommendationCard
                key={idx}
                lesson={lesson}
                reason={recommendations.reasons[idx]}
              />
            ))}
          </div>
        </div>
      )}

      {/* Time Statistics */}
      <div className="time-stats">
        <h2>Time Invested</h2>
        <div className="time-grid">
          <TimeCard
            label="This Week"
            value={`${progress.hoursThisWeek}h`}
          />
          <TimeCard
            label="This Month"
            value={`${progress.hoursThisMonth}h`}
          />
          <TimeCard
            label="Total"
            value={`${progress.totalHours}h`}
          />
        </div>
      </div>
    </div>
  );
};

/**
 * StatCard Component
 */
const StatCard = ({ title, value, subtitle, icon, color }) => (
  <div className={`stat-card stat-${color}`}>
    <div className="stat-icon">{icon}</div>
    <div className="stat-content">
      <div className="stat-title">{title}</div>
      <div className="stat-value">{value}</div>
      {subtitle && <div className="stat-subtitle">{subtitle}</div>}
    </div>
  </div>
);

/**
 * LessonTimelineItem Component
 */
const LessonTimelineItem = ({ lesson, position }) => (
  <div className={`timeline-item ${lesson.status}`}>
    <div className="timeline-marker">
      {lesson.status === 'completed' && '✓'}
      {lesson.status === 'in_progress' && '→'}
      {lesson.status === 'not_started' && '○'}
    </div>
    <div className="timeline-content">
      <h3>{lesson.title}</h3>
      <p className="lesson-category">{lesson.category}</p>
      {lesson.status === 'completed' && (
        <p className="completion-date">Completed {lesson.completedDate}</p>
      )}
    </div>
  </div>
);

/**
 * RecommendationCard Component
 */
const RecommendationCard = ({ lesson, reason }) => (
  <div className="recommendation-card">
    <div className="recommendation-header">
      <h3>{lesson.title}</h3>
      <span className="difficulty-badge">{lesson.difficulty}</span>
    </div>
    <p className="recommendation-reason">
      <strong>Why:</strong> {reason}
    </p>
    <div className="recommendation-meta">
      <span className="duration">⏱️ {lesson.durationMinutes} min</span>
      <span className="category">{lesson.category}</span>
    </div>
    <button className="start-lesson-btn">Start Lesson →</button>
  </div>
);

/**
 * TimeCard Component
 */
const TimeCard = ({ label, value }) => (
  <div className="time-card">
    <div className="time-label">{label}</div>
    <div className="time-value">{value}</div>
  </div>
);

export default ProgressDashboard;
