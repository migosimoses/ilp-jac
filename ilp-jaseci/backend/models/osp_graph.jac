"""Object-Spatial-Paradigm (OSP) knowledge graph model."""

node OSPNode {
    has concept_id: str;
    has concept_name: str;
    has category: str;  # "core", "advanced", "practical"
    has description: str;
    has proficiency_level: float = 0.0;  # 0.0 to 1.0
    has is_unlocked: bool = false;
    has unlock_threshold: float = 0.7;  # proficiency needed to unlock next
    has resources: list[str];  # lesson_ids and tutorial links
}

node MasteryNode {
    has user_id: str;
    has concept_id: str;
    has mastery_score: float = 0.0;  # 0.0 to 1.0
    has times_practiced: int = 0;
    has last_practiced: str;
    has strength: str = "weak";  # weak, developing, strong, mastered
}

edge prerequisite_concept {
    has strength: float = 1.0;  # how strongly required (0-1)
}

edge related_concept {
    has similarity: float;  # relatedness score
}

edge unlocks_lesson {
    has threshold: float;  # mastery threshold to unlock
}

# Graph representing Jac/Jaseci learning path
edge jac_path {
    has sequence: int;
    has progress: float = 0.0;
}
