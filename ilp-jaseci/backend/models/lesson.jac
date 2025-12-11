"""Lesson and content model."""

node Lesson {
    has lesson_id: str;
    has title: str;
    has description: str;
    has category: str;  # "jac_basics", "walkers", "osp", "by_llm"
    has difficulty: str = "beginner";  # beginner, intermediate, advanced
    has duration_minutes: int;
    has content: str;  # markdown content
    has prerequisites: list[str] = [];
    has created_at: str;
    has updated_at: str;
}

node LessonContent {
    has lesson_id: str;
    has section_num: int;
    has section_title: str;
    has body: str;  # markdown
    has code_example: str = "";
    has key_concepts: list[str];
}

node CodeExercise {
    has exercise_id: str;
    has lesson_id: str;
    has title: str;
    has description: str;
    has starter_code: str;
    has solution_code: str;
    has test_cases: list[str];
    has difficulty: str = "beginner";
}

edge prerequisite {
    has required: bool = true;
}

edge contains_exercise {
}
