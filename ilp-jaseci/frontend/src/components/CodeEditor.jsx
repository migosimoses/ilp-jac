import React, { useState, useRef } from 'react';
import './CodeEditor.css';

/**
 * CodeEditor Component
 * Monaco-based code editor for exercises with syntax highlighting
 * and live test execution
 */
const CodeEditor = ({ exerciseId, userId, lessonId, onSubmit }) => {
  const [code, setCode] = useState('');
  const [testResults, setTestResults] = useState(null);
  const [isRunning, setIsRunning] = useState(false);
  const [showSolution, setShowSolution] = useState(false);
  const editorRef = useRef(null);

  const handleRunTests = async () => {
    try {
      setIsRunning(true);
      // Call content validator walker
      const response = await fetch('/api/exercises/validate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          exerciseId,
          code,
          userId
        })
      });
      const results = await response.json();
      setTestResults(results);
      setIsRunning(false);
    } catch (error) {
      console.error('Error running tests:', error);
      setIsRunning(false);
    }
  };

  const handleSubmit = async () => {
    if (!testResults || !testResults.allPassed) {
      alert('Please fix the failing tests before submitting.');
      return;
    }

    try {
      // Call progress tracker walker with exercise completion
      await fetch('/api/exercises/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          exerciseId,
          code,
          userId,
          lessonId,
          testsPassed: testResults.passedTests,
          totalTests: testResults.totalTests
        })
      });

      if (onSubmit) {
        onSubmit({ exerciseId, success: true });
      }
    } catch (error) {
      console.error('Error submitting exercise:', error);
    }
  };

  const handleShowSolution = () => {
    setShowSolution(!showSolution);
  };

  return (
    <div className="code-editor-container">
      <div className="editor-header">
        <h3>Exercise: {exerciseId}</h3>
        <div className="editor-actions">
          <button onClick={handleRunTests} disabled={isRunning} className="btn btn-secondary">
            {isRunning ? 'Running...' : 'Run Tests'}
          </button>
          <button onClick={handleSubmit} className="btn btn-primary">
            Submit Solution
          </button>
          <button onClick={handleShowSolution} className="btn btn-outline">
            {showSolution ? 'Hide Solution' : 'Show Solution'}
          </button>
        </div>
      </div>

      <div className="editor-wrapper">
        <textarea
          ref={editorRef}
          value={code}
          onChange={(e) => setCode(e.target.value)}
          className="code-input"
          placeholder="Write your code here..."
          spellCheck="false"
        />
      </div>

      {testResults && (
        <div className={`test-results ${testResults.allPassed ? 'success' : 'failure'}`}>
          <h4>Test Results</h4>
          <div className="results-summary">
            {testResults.passedTests} / {testResults.totalTests} tests passed
          </div>
          {testResults.testDetails && (
            <ul className="test-details">
              {testResults.testDetails.map((test, idx) => (
                <li key={idx} className={test.passed ? 'passed' : 'failed'}>
                  <span className="test-status">{test.passed ? '✓' : '✗'}</span>
                  <span>{test.name}</span>
                  {test.message && <span className="test-message">{test.message}</span>}
                </li>
              ))}
            </ul>
          )}
        </div>
      )}

      {showSolution && (
        <div className="solution-display">
          <h4>Solution</h4>
          <pre><code>{/* Solution code would go here */}</code></pre>
        </div>
      )}
    </div>
  );
};

export default CodeEditor;
