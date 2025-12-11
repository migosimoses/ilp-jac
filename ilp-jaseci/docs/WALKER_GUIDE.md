# Walker Implementation Guide

## Overview

Walkers are the core agents of computation in Jac. They traverse graphs, perform operations, and enable adaptive learning. This guide explains how to implement walkers for the ILP platform.

## Walker Basics

### Walker Definition Structure

```jac
walker WalkerName {
    # State variables
    has variable_name: type = default_value;
    
    # Walker abilities (methods)
    can ability_name {
        # Implementation
    }
    
    @by_llm
    can ai_ability_name {
        # LLM-powered implementation
    }
}
```

## Core Walkers Implementation

### 1. ProgressTracker Walker

**Purpose**: Record lesson completion and calculate proficiency scores

```jac
walker ProgressTracker {
    has user_id: str;
    has lesson_id: str;
    has quiz_id: str = "";
    has score: float = 0.0;
    has time_spent: int = 0;

    can track_lesson_progress {
        """
        Update user's progress for a completed lesson.
        Should be called after user finishes lesson content.
        """
        # 1. Find/create UserProgress node
        # 2. Update status to 'completed'
        # 3. Record completion time
        # 4. Update total lessons completed
        
        print(f"Tracked progress for user {user_id} on lesson {lesson_id}");
    }

    can calculate_proficiency {
        """
        Calculate proficiency level (0.0 - 1.0) based on:
        - Quiz scores (70%)
        - Practice time (30%)
        """
        let proficiency = (score * 0.7) + ((time_spent / 3600) * 0.3);
        if proficiency > 1.0:
            proficiency = 1.0;
        
        return proficiency;
    }

    can update_mastery_score {
        """
        Update user's mastery for concepts tested in quiz.
        Uses OSP graph to find related concepts.
        """
        # 1. Get quiz questions and their concepts
        # 2. Calculate concept-specific mastery
        # 3. Update MasteryNode for each concept
        # 4. Check unlock thresholds
        
        print(f"Updating mastery score for user {user_id}");
    }

    can unlock_next_lesson {
        """
        Check if user meets proficiency threshold to unlock next lesson.
        Prerequisites must be satisfied.
        """
        # 1. Find current lesson's next lesson
        # 2. Check all prerequisites met
        # 3. Check if mastery threshold reached
        # 4. Update is_unlocked flag
        
        print(f"Checking unlock criteria for user {user_id}");
    }
}
```

### 2. ContentServer Walker

**Purpose**: Deliver lesson content with prerequisite validation

```jac
walker ContentServer {
    has user_id: str;
    has lesson_id: str;
    has section_num: int = -1;

    can get_lesson_content {
        """
        Retrieve lesson content for user.
        Check prerequisites before returning.
        """
        # 1. Validate prerequisites
        # 2. Load lesson sections
        # 3. Mark as 'in_progress'
        # 4. Return structured content
        
        print(f"Fetching lesson {lesson_id} for user {user_id}");
    }

    can validate_prerequisites {
        """
        Check if user has completed all prerequisite lessons.
        Return missing prerequisites.
        """
        let missing = [];
        
        # Walk through prerequisite edges
        take -->prerequisite {
            # Check if user completed this prerequisite
            # Add to missing if not completed
        }
        
        return missing;
    }

    can get_next_recommended_lesson {
        """
        Recommend next lesson based on:
        - Completed lessons
        - Prerequisites met
        - Weak areas identified
        """
        # 1. Analyze OSP graph
        # 2. Find unlocked lessons
        # 3. Apply recommendation algorithm
        # 4. Return best match
        
        print(f"Finding next lesson for user {user_id}");
    }
}
```

### 3. QuizGenerator Walker

**Purpose**: Generate context-aware quiz questions using byLLM

```jac
walker QuizGenerator {
    has lesson_id: str;
    has num_questions: int = 5;
    has difficulty: str = "beginner";
    has quiz_type: str = "mixed";

    @by_llm
    can generate_quiz {
        """
        Use LLM to generate quiz questions from lesson content.
        
        LLM Prompt Template:
        "Generate {num_questions} {difficulty} quiz questions about:
        {lesson_content}
        
        Include:
        - Multiple choice questions
        - True/false questions  
        - Free-text questions
        - Code-based questions
        
        Format as JSON with fields:
        - questionText
        - questionType
        - options (for multiple choice)
        - correctAnswer
        - explanation"
        """
        
        # LLM generates questions
        # Parse response into Question nodes
        # Create Quiz node with questions
        
        print(f"Generated {num_questions} questions for lesson {lesson_id}");
    }

    @by_llm
    can generate_question_variants {
        """
        Generate alternative versions of a question.
        Useful for re-attempts and adaptive difficulty.
        """
        
        # LLM creates variant questions
        # Preserve conceptual difficulty
        # Vary wording and examples
        
        print("Generated question variants");
    }
}
```

### 4. QuizAssessor Walker

**Purpose**: Evaluate quiz answers using byLLM

```jac
walker QuizAssessor {
    has quiz_id: str;
    has question_id: str;
    has user_answer: str;
    has question_text: str = "";

    @by_llm
    can evaluate_free_text_answer {
        """
        Evaluate free-text answers for conceptual correctness.
        
        LLM Prompt Template:
        "Evaluate this student answer to the question:
        Question: {question_text}
        Student Answer: {user_answer}
        
        Determine:
        1. Is the answer conceptually correct? (yes/no)
        2. Score (0-100)
        3. What concepts are demonstrated?
        4. What's missing or incorrect?
        5. Constructive feedback for improvement
        
        Focus on conceptual understanding, not exact wording."
        """
        
        # LLM evaluates answer
        # Return: score, feedback, identified_concepts
        
        print(f"Evaluated answer for question {question_id}");
    }

    @by_llm
    can evaluate_code_answer {
        """
        Evaluate code submissions.
        Check: correctness, style, best practices.
        """
        
        # 1. Run code tests
        # 2. LLM reviews code quality
        # 3. Return combined score
        
        print(f"Evaluated code for question {question_id}");
    }

    @by_llm
    can generate_feedback {
        """
        Create personalized feedback for incorrect answers.
        
        LLM Prompt:
        "Student got this wrong: {user_answer}
        Question was: {question_text}
        Correct answer: {correct_answer}
        
        Generate:
        1. Empathetic acknowledgment
        2. Explanation of why answer is wrong
        3. Common misconceptions addressed
        4. Resources or next steps to learn correct concept"
        """
        
        # LLM generates feedback
        # Include recommended resources
        
        print(f"Generated feedback for question {question_id}");
    }

    can score_quiz_attempt {
        """
        Calculate overall quiz score from individual questions.
        Update mastery scores based on results.
        """
        let total_score = 0.0;
        let question_count = 0;
        
        # Sum scores from answered questions
        # Calculate average
        # Update user's mastery
        
        print(f"Scored quiz {quiz_id}");
    }
}
```

### 5. LearningPathOptimizer Walker

**Purpose**: AI-powered adaptive learning recommendations

```jac
walker LearningPathOptimizer {
    has user_id: str;
    has mastery_data: dict = {};
    has completed_lessons: list = [];

    @by_llm
    can analyze_learning_graph {
        """
        Analyze user's knowledge graph to understand proficiency.
        
        LLM Prompt:
        "Analyze this student's learning profile:
        - Completed lessons: {completed_lessons}
        - Mastery scores: {mastery_data}
        - Time invested: {time_data}
        
        Provide:
        1. Overall proficiency assessment
        2. Mastered concepts
        3. Developing concepts
        4. Weak areas needing review
        5. Knowledge gaps to address"
        """
        
        # LLM analyzes OSP graph
        # Return structured analysis
        
        print(f"Analyzed learning graph for user {user_id}");
    }

    @by_llm
    can recommend_next_lesson {
        """
        Recommend best next lesson for student.
        
        LLM Prompt:
        "Based on this student's profile:
        {student_analysis}
        
        Recommend the ONE next lesson that:
        - Builds on mastered concepts
        - Challenges but doesn't overwhelm
        - Fills knowledge gaps
        - Aligns with learning goals
        
        Return: lesson_id, explanation, estimated_time"
        """
        
        # LLM selects optimal lesson
        # Return recommendation with reasoning
        
        print(f"Recommending next lesson for {user_id}");
    }

    @by_llm
    can identify_struggle_areas {
        """
        Find concepts where student struggles.
        Suggest targeted interventions.
        """
        
        # LLM identifies weak concepts
        # Return with recommended actions
        
        print(f"Identifying struggles for {user_id}");
    }
}
```

## byLLM Decorator Deep Dive

### What is @by_llm?

The `@by_llm` decorator transforms a walker ability into an LLM-powered function:

```jac
@by_llm
can my_ai_ability {
    # The body is a prompt template
    # Jac fills in variables
    # Calls LLM with the prompt
    # Returns LLM response
}
```

### LLM Prompt Best Practices

1. **Be Specific**: Tell LLM exactly what you want
```jac
@by_llm
can evaluate_answer {
    # Good: Specific instructions
    print("Evaluate this answer as CORRECT or INCORRECT only.");
    
    # Bad: Vague
    print("What do you think about this answer?");
}
```

2. **Provide Context**: Include all relevant information
```jac
@by_llm
can generate_question {
    # Include lesson content for context
    let context = get_lesson_content();
    print(f"Generate a question about: {context}");
}
```

3. **Structure Output**: Ask for JSON/structured format
```jac
@by_llm
can generate_quiz {
    print("Return JSON with fields: questionText, options, correct_answer");
}
```

4. **Handle Edge Cases**: Guide LLM behavior
```jac
@by_llm
can evaluate_answer {
    print("If unsure, explain your reasoning.");
    print("If impossible, return INVALID.");
}
```

## Testing Your Walkers

### Unit Test Pattern

```jac
with entry {
    # Test ProgressTracker
    let pt = spawn ProgressTracker(
        user_id="test_user",
        lesson_id="lesson_1",
        score=85.0,
        time_spent=1800
    );
    
    let proficiency = pt.calculate_proficiency();
    assert proficiency > 0.7;
    
    # Test QuizGenerator
    let qg = spawn QuizGenerator(
        lesson_id="lesson_1",
        num_questions=5
    );
    
    let quiz = qg.generate_quiz();
    assert len(quiz.questions) == 5;
}
```

### Integration Test Pattern

```python
# In test_walkers.py
def test_full_quiz_flow():
    # Generate quiz
    quiz = spawn('QuizGenerator', {...}).generate_quiz()
    
    # User answers
    answers = {'q1': 'Object-Spatial-Paradigm', 'q2': True}
    
    # Evaluate answers
    results = spawn('QuizAssessor', {
        'answers': answers
    }).score_quiz_attempt()
    
    # Check progression
    assert results['score'] > 70
    assert user['mastery'] > old_mastery
```

## Common Patterns

### Pattern 1: State Accumulation

```jac
walker Collector {
    has collected: list = [];
    
    can collect {
        # Accumulate data as walking
        collected.append(current_value);
        take --> node {
            collect();  # Recursive traversal
        }
    }
}
```

### Pattern 2: Conditional Branching

```jac
walker Router {
    can navigate {
        if user.mastery > 0.8 {
            take --> advanced_lesson;
        } else {
            take --> basic_review;
        }
    }
}
```

### Pattern 3: Graph Modification

```jac
walker Updater {
    can update {
        # Create new edge
        here --> new_edge --> target;
        
        # Update node attribute
        here.attribute = new_value;
    }
}
```

## Debugging Tips

1. **Print statements**: Use `print()` liberally in development
2. **Return values**: Check what walkers return at each step
3. **Graph inspection**: Visualize graph state during execution
4. **LLM logs**: Check what prompts are sent to LLM
5. **Performance**: Profile walker execution time

## Performance Optimization

1. **Batch operations**: Process multiple nodes together
2. **Caching**: Store frequently accessed data
3. **Lazy evaluation**: Only compute what's needed
4. **Index usage**: Use indexed lookups for large graphs
5. **Async**: When possible, parallelize walker spawns

---

For more examples, see `backend/walkers/` directory.
