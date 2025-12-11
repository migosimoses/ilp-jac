import React, { useState, useEffect } from 'react';
import './SkillMap.css';

/**
 * SkillMap Component
 * Visual representation of mastery across concepts using OSP graph
 * Shows strengths, weaknesses, and learning progress
 */
const SkillMap = ({ userId }) => {
  const [skillData, setSkillData] = useState(null);
  const [selectedConcept, setSelectedConcept] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSkillMap();
  }, [userId]);

  const fetchSkillMap = async () => {
    try {
      setLoading(true);
      // Call MasteryAggregator walker
      const response = await fetch(`/api/users/${userId}/skill-map`, {
        headers: { 'X-User-ID': userId }
      });
      const data = await response.json();
      setSkillData(data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching skill map:', error);
      setLoading(false);
    }
  };

  if (loading) return <div className="skill-map-loading">Loading skill map...</div>;
  if (!skillData) return <div className="skill-map-error">Unable to load skill map</div>;

  const categories = ['core', 'advanced', 'practical'];
  const masteryCss = (score) => {
    if (score >= 0.8) return 'mastered';
    if (score >= 0.6) return 'strong';
    if (score >= 0.4) return 'developing';
    return 'weak';
  };

  return (
    <div className="skill-map-container">
      <div className="skill-map-header">
        <h2>Your Skill Map</h2>
        <p>Visual representation of your mastery across Jac & Jaseci concepts</p>
      </div>

      <div className="skill-categories">
        {categories.map(category => (
          <div key={category} className="category-section">
            <h3>{category.charAt(0).toUpperCase() + category.slice(1)} Concepts</h3>
            
            <div className="concept-grid">
              {skillData.concepts
                .filter(c => c.category === category)
                .map(concept => (
                  <div
                    key={concept.conceptId}
                    className={`concept-node ${masteryCss(concept.masteryScore)}`}
                    onClick={() => setSelectedConcept(concept)}
                    style={{
                      opacity: concept.isUnlocked ? 1 : 0.5,
                      cursor: 'pointer'
                    }}
                  >
                    <div className="concept-name">{concept.conceptName}</div>
                    <div className="mastery-bar">
                      <div
                        className="mastery-fill"
                        style={{ width: `${concept.masteryScore * 100}%` }}
                      />
                    </div>
                    <div className="mastery-text">
                      {Math.round(concept.masteryScore * 100)}%
                    </div>
                    {!concept.isUnlocked && (
                      <div className="locked-badge">🔒</div>
                    )}
                  </div>
                ))}
            </div>
          </div>
        ))}
      </div>

      {selectedConcept && (
        <ConceptDetail
          concept={selectedConcept}
          onClose={() => setSelectedConcept(null)}
        />
      )}

      <div className="skill-map-legend">
        <h4>Mastery Levels</h4>
        <div className="legend-items">
          <div className="legend-item"><span className="weak-box"></span> Weak (0-40%)</div>
          <div className="legend-item"><span className="developing-box"></span> Developing (40-60%)</div>
          <div className="legend-item"><span className="strong-box"></span> Strong (60-80%)</div>
          <div className="legend-item"><span className="mastered-box"></span> Mastered (80%+)</div>
        </div>
      </div>
    </div>
  );
};

/**
 * ConceptDetail Modal
 * Shows detailed information about a selected concept
 */
const ConceptDetail = ({ concept, onClose }) => (
  <div className="concept-detail-modal" onClick={onClose}>
    <div className="concept-detail-content" onClick={(e) => e.stopPropagation()}>
      <button className="close-btn" onClick={onClose}>×</button>
      
      <h2>{concept.conceptName}</h2>
      
      <div className="concept-info">
        <div className="info-row">
          <label>Category:</label>
          <span>{concept.category}</span>
        </div>
        
        <div className="info-row">
          <label>Mastery Score:</label>
          <span>{Math.round(concept.masteryScore * 100)}%</span>
        </div>
        
        <div className="info-row">
          <label>Times Practiced:</label>
          <span>{concept.timesPracticed}</span>
        </div>
        
        <div className="info-row">
          <label>Last Practiced:</label>
          <span>{concept.lastPracticed || 'Never'}</span>
        </div>

        <div className="info-row">
          <label>Status:</label>
          <span className={`status-badge ${concept.strength}`}>
            {concept.strength}
          </span>
        </div>
      </div>

      <div className="concept-description">
        <h3>Description</h3>
        <p>{concept.description}</p>
      </div>

      {concept.resources && concept.resources.length > 0 && (
        <div className="concept-resources">
          <h3>Related Resources</h3>
          <ul>
            {concept.resources.map((resource, idx) => (
              <li key={idx}>
                <a href={`/lessons/${resource.lessonId}`}>
                  {resource.lessonTitle}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}

      {!concept.isUnlocked && (
        <div className="unlock-info">
          <p>🔒 Unlock at {Math.round(concept.unlockThreshold * 100)}% mastery</p>
          <p>Current: {Math.round(concept.masteryScore * 100)}%</p>
        </div>
      )}
    </div>
  </div>
);

export default SkillMap;
