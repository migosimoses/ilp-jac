"""Quiz and assessment model."""

node Quiz {
    has quiz_id: str;
    has lesson_id: str;
    has title: str;
    has description: str;
    has difficulty: str = "beginner";
    has num_questions: int;
    has time_limit_minutes: int = 0;  # 0 = no limit
    has passing_score: float = 70.0;
    has created_at: str;
}

node Question {
    has question_id: str;
    has quiz_id: str;
    has question_text: str;
    has question_type: str;  # "multiple_choice", "true_false", "free_text", "code"
    has difficulty: str = "beginner";
    has points: int = 1;
}

node MultipleChoiceQuestion {
    has question_id: str;
    has options: list[str];
    has correct_answer: str;
    has explanation: str = "";
}

node TrueeFalseQuestion {
    has question_id: str;
    has correct_answer: bool;
    has explanation: str = "";
}

node FreeTextQuestion {
    has question_id: str;
    has expected_answer: str;
    has keywords: list[str];  # keywords that should appear in answer
    has explanation: str = "";
}

node CodeQuestion {
    has question_id: str;
    has starter_code: str;
    has test_code: str;
    has explanation: str = "";
}

node QuizAttempt {
    has attempt_id: str;
    has user_id: str;
    has quiz_id: str;
    has start_time: str;
    has end_time: str;
    has score: float;
    has passed: bool;
    has answers: dict[str, str];  # question_id -> user_answer
}

edge contains_question {
    has question_order: int;
}

edge answered_question {
    has user_answer: str;
    has is_correct: bool;
    has points_earned: int;
}
