"""User model for tracking learner information and progress."""

node User {
    has user_id: str;
    has name: str;
    has email: str;
    has created_at: str;
    has total_score: float = 0.0;
    has lessons_completed: int = 0;
    has quizzes_taken: int = 0;
    has avg_quiz_score: float = 0.0;
}

node UserProgress {
    has user_id: str;
    has lesson_id: str;
    has status: str = "not_started";  # not_started, in_progress, completed
    has score: float = 0.0;
    has attempts: int = 0;
    has last_accessed: str;
    has time_spent_seconds: int = 0;
}

edge studied_lesson {
    has proficiency: float;  # 0.0 to 1.0
}

edge completed_quiz {
    has score: float;
    has timestamp: str;
}
