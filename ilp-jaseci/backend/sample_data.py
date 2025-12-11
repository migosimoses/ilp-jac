"""
Sample lessons data for the ILP platform
Pre-populate the system with foundational content
"""

SAMPLE_LESSONS = [
    {
        "lesson_id": "jac-intro-1",
        "title": "What is Jac?",
        "category": "jac_basics",
        "difficulty": "beginner",
        "duration_minutes": 20,
        "description": "Introduction to the Jac language and its key concepts",
        "prerequisites": [],
        "sections": [
            {
                "section_num": 1,
                "section_title": "Introduction",
                "body": """
                <p>Welcome to Jac! Jac is a modern programming language designed around 
                <strong>graph-based computation</strong> and the <strong>Object-Spatial-Paradigm (OSP)</strong>.</p>
                
                <p>Unlike traditional imperative or object-oriented languages, Jac lets you:</p>
                <ul>
                    <li>Define spatial structures as graphs</li>
                    <li>Navigate these graphs with walkers</li>
                    <li>Leverage AI through byLLM agents</li>
                </ul>
                """,
                "code_example": "",
                "key_concepts": ["Graph-based programming", "Spatial paradigm", "OSP"]
            },
            {
                "section_num": 2,
                "section_title": "Why Jac?",
                "body": """
                <p>Jac excels at problems involving:</p>
                <ul>
                    <li><strong>Knowledge graphs</strong> - Representing relationships between concepts</li>
                    <li><strong>Social networks</strong> - Modeling connections between people</li>
                    <li><strong>Recommendation systems</strong> - Finding patterns in connected data</li>
                    <li><strong>AI integration</strong> - Using LLMs to power intelligent agents</li>
                </ul>
                
                <p>Jac makes these tasks intuitive and expressive.</p>
                """,
                "code_example": "",
                "key_concepts": ["Use cases", "Knowledge graphs"]
            },
            {
                "section_num": 3,
                "section_title": "Your First Jac Program",
                "body": """
                <p>Let's start simple:</p>
                """,
                "code_example": """with entry {
    print("Hello from Jac!");
}""",
                "key_concepts": ["Entry point", "print statement"]
            }
        ]
    },
    {
        "lesson_id": "jac-nodes-1",
        "title": "Nodes and Edges",
        "category": "jac_basics",
        "difficulty": "beginner",
        "duration_minutes": 25,
        "description": "Understanding the fundamental building blocks of Jac programs",
        "prerequisites": ["jac-intro-1"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "What are Nodes?",
                "body": """
                <p>In Jac, a <strong>node</strong> is a data structure that represents 
                a vertex in a graph. Each node can hold data (attributes) and be connected 
                to other nodes through edges.</p>
                
                <p>Think of nodes as objects with properties:</p>
                """,
                "code_example": """node Person {
    has name: str;
    has age: int;
    has email: str;
}""",
                "key_concepts": ["Node definition", "Attributes", "Data types"]
            },
            {
                "section_num": 2,
                "section_title": "Understanding Edges",
                "body": """
                <p><strong>Edges</strong> are connections between nodes. They represent 
                relationships and can also have their own attributes.</p>
                
                <p>Edges enable expressing rich relationships:</p>
                """,
                "code_example": """edge friend_of {
    has since_year: int;
    has strength: float;
}

node Person {
    has name: str;
}""",
                "key_concepts": ["Edge definition", "Relationships", "Edge attributes"]
            },
            {
                "section_num": 3,
                "section_title": "Building Your First Graph",
                "body": """
                <p>Combine nodes and edges to build a graph structure:</p>
                """,
                "code_example": """node Person {
    has name: str;
}

edge knows {
    has years: int;
}

with entry {
    let person1 = spawn Person(name="Alice");
    let person2 = spawn Person(name="Bob");
    person1 --> knows(years=5) --> person2;
}""",
                "key_concepts": ["Graph construction", "Spawn", "Edge creation"]
            }
        ]
    },
    {
        "lesson_id": "jac-walkers-1",
        "title": "Introduction to Walkers",
        "category": "walkers",
        "difficulty": "intermediate",
        "duration_minutes": 35,
        "description": "Learn how to traverse and manipulate graphs with walkers",
        "prerequisites": ["jac-nodes-1"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "What are Walkers?",
                "body": """
                <p>A <strong>walker</strong> is a mobile entity that traverses a graph. 
                It's like a cursor moving through your data structure, performing 
                operations at each node.</p>
                
                <p>Walkers are powerful for:</p>
                <ul>
                    <li>Graph traversal and searching</li>
                    <li>Data processing and transformation</li>
                    <li>Pattern matching in complex structures</li>
                    <li>Building algorithms that operate on graphs</li>
                </ul>
                """,
                "code_example": "",
                "key_concepts": ["Walker definition", "Graph traversal"]
            },
            {
                "section_num": 2,
                "section_title": "Basic Walker Example",
                "body": """
                <p>Here's a simple walker that visits each node in a graph:</p>
                """,
                "code_example": """walker Visitor {
    can visit {
        # This code runs at each node
        print("Visiting node");
    }
}

with entry {
    # Walker traverses from the current node
    visit();
}""",
                "key_concepts": ["Walker creation", "Can abilities", "Entry"]
            },
            {
                "section_num": 3,
                "section_title": "Traversing Edges",
                "body": """
                <p>Walkers can traverse edges to move between nodes:</p>
                """,
                "code_example": """walker Explorer {
    can explore {
        print("At node");
        # Move to all connected nodes
        take --> visit;
    }
    
    can visit {
        print("Visiting connected node");
    }
}""",
                "key_concepts": ["Edge traversal", "Take statement", "Backtracking"]
            }
        ]
    },
    {
        "lesson_id": "jac-osp-1",
        "title": "Object-Spatial-Paradigm (OSP)",
        "category": "osp",
        "difficulty": "intermediate",
        "duration_minutes": 40,
        "description": "Master the Object-Spatial-Paradigm that makes Jac unique",
        "prerequisites": ["jac-walkers-1"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "What is OSP?",
                "body": """
                <p>The <strong>Object-Spatial-Paradigm</strong> is the core philosophy of Jac. 
                It combines three concepts:</p>
                
                <ul>
                    <li><strong>Object:</strong> Encapsulation of data and behavior</li>
                    <li><strong>Spatial:</strong> Organization in space (graphs)</li>
                    <li><strong>Paradigm:</strong> A way of thinking about programming</li>
                </ul>
                
                <p>OSP treats computation as navigation through a spatial structure 
                where objects interact through their connections.</p>
                """,
                "code_example": "",
                "key_concepts": ["OSP principles", "Spatial thinking"]
            },
            {
                "section_num": 2,
                "section_title": "Spatial Thinking",
                "body": """
                <p>In OSP, you think about your program in terms of space:</p>
                <ul>
                    <li>Nodes are locations</li>
                    <li>Edges are paths between locations</li>
                    <li>Walkers are agents moving through space</li>
                    <li>Data flows along the graph</li>
                </ul>
                
                <p>This is fundamentally different from traditional sequential programming.</p>
                """,
                "code_example": """# Traditional: linear sequence
x = 1
y = x + 2
z = y * 3

# OSP: spatial navigation
walker Calculator {
    can compute {
        # Start at one node, move through graph
        take --> process --> aggregate;
    }
}""",
                "key_concepts": ["Spatial navigation", "Graph-based computation"]
            },
            {
                "section_num": 3,
                "section_title": "Advanced OSP Patterns",
                "body": """
                <p>Master complex OSP patterns for real-world problems:</p>
                <ul>
                    <li>Multi-hop traversals</li>
                    <li>Parallel walkers</li>
                    <li>Conditional graph navigation</li>
                    <li>Dynamic graph modification</li>
                </ul>
                """,
                "code_example": """walker SmartNavigator {
    has visited: list = [];
    
    can traverse {
        # Complex pattern: visit unvisited neighbors
        for n in -->node {
            if n not in visited {
                visited.append(n);
                take n;
            }
        }
    }
}""",
                "key_concepts": ["Pattern matching", "Conditional traversal"]
            }
        ]
    },
    {
        "lesson_id": "jac-by-llm-1",
        "title": "Introduction to byLLM",
        "category": "by_llm",
        "difficulty": "advanced",
        "duration_minutes": 45,
        "description": "Integrate AI into your Jac programs with byLLM agents",
        "prerequisites": ["jac-osp-1"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "What is byLLM?",
                "body": """
                <p>The <strong>byLLM</strong> decorator lets you leverage Large Language Models 
                directly within your Jac code. It's a powerful way to add AI reasoning 
                to your graph-based applications.</p>
                
                <p>Use byLLM for:</p>
                <ul>
                    <li>Natural language understanding</li>
                    <li>Question answering and reasoning</li>
                    <li>Content generation and summarization</li>
                    <li>Decision making and recommendations</li>
                    <li>Free-text answer evaluation</li>
                </ul>
                """,
                "code_example": "",
                "key_concepts": ["byLLM decorator", "LLM integration"]
            },
            {
                "section_num": 2,
                "section_title": "Using byLLM in Walkers",
                "body": """
                <p>Apply the @by_llm decorator to walker abilities:</p>
                """,
                "code_example": """walker QuizMaster {
    has topic: str;
    
    @by_llm
    can generate_question {
        # LLM generates a question about the topic
        # Prompt context is automatically provided
        return question;
    }
    
    @by_llm
    can evaluate_answer(student_answer: str) {
        # LLM evaluates if answer is correct
        # Returns score and feedback
        return {"score": 85, "feedback": "Good!"};
    }
}""",
                "key_concepts": ["@by_llm decorator", "LLM abilities"]
            },
            {
                "section_num": 3,
                "section_title": "Building an AI Agent",
                "body": """
                <p>Combine OSP with byLLM to create intelligent agents:</p>
                """,
                "code_example": """walker TutorAgent {
    has student_progress: dict = {};
    
    @by_llm
    can recommend_next_lesson {
        # Analyze student progress
        # Recommend next lesson using AI reasoning
        return lesson_recommendation;
    }
    
    @by_llm
    can explain_concept(concept: str) {
        # Generate personalized explanation
        return explanation;
    }
}""",
                "key_concepts": ["AI agents", "Personalization", "Intelligent reasoning"]
            }
        ]
    }
]

SAMPLE_QUIZZES = [
    {
        "quiz_id": "quiz-jac-basics-1",
        "lesson_id": "jac-intro-1",
        "title": "Jac Basics Quiz",
        "difficulty": "beginner",
        "questions": [
            {
                "question_id": "q1",
                "question_text": "What does OSP stand for?",
                "question_type": "multiple_choice",
                "options": [
                    "Object-Spatial-Paradigm",
                    "Object-Structured-Protocol",
                    "Online-Service-Platform",
                    "Open-Source-Project"
                ],
                "correct_answer": "Object-Spatial-Paradigm"
            },
            {
                "question_id": "q2",
                "question_text": "Jac is designed for graph-based computation.",
                "question_type": "true_false",
                "correct_answer": True
            },
            {
                "question_id": "q3",
                "question_text": "List three types of problems that Jac excels at solving.",
                "question_type": "free_text",
                "keywords": ["knowledge graphs", "networks", "recommendation"]
            }
        ]
    },
    {
        "quiz_id": "quiz-nodes-edges-1",
        "lesson_id": "jac-nodes-1",
        "title": "Nodes and Edges Quiz",
        "difficulty": "beginner",
        "questions": [
            {
                "question_id": "q1",
                "question_text": "In Jac, what is a node?",
                "question_type": "multiple_choice",
                "options": [
                    "A vertex in a graph that can hold data",
                    "A function definition",
                    "A loop construct",
                    "A variable declaration"
                ],
                "correct_answer": "A vertex in a graph that can hold data"
            },
            {
                "question_id": "q2",
                "question_text": "Edges can have attributes just like nodes.",
                "question_type": "true_false",
                "correct_answer": True
            }
        ]
    },
    {
        "quiz_id": "quiz-walkers-1",
        "lesson_id": "jac-walkers-1",
        "title": "Walkers Quiz",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_id": "q1",
                "question_text": "What is the primary purpose of a walker?",
                "question_type": "multiple_choice",
                "options": [
                    "To traverse and operate on graphs",
                    "To define node attributes",
                    "To create new edges",
                    "To validate syntax"
                ],
                "correct_answer": "To traverse and operate on graphs"
            },
            {
                "question_id": "q2",
                "question_text": "Write a simple walker that prints a message.",
                "question_type": "code",
                "starter_code": """walker Printer {
    can print_message {
        # Your code here
    }
}"""
            }
        ]
    }
]

SAMPLE_CONCEPTS = [
    {
        "concept_id": "nodes-basics",
        "concept_name": "Node Basics",
        "category": "core",
        "description": "Understanding graph nodes and their attributes in Jac",
        "resources": ["jac-nodes-1"]
    },
    {
        "concept_id": "edges-basics",
        "concept_name": "Edge Basics",
        "category": "core",
        "description": "Understanding edges and relationships between nodes",
        "resources": ["jac-nodes-1"]
    },
    {
        "concept_id": "walkers",
        "concept_name": "Walkers",
        "category": "core",
        "description": "Graph traversal using walkers",
        "resources": ["jac-walkers-1"]
    },
    {
        "concept_id": "osp",
        "concept_name": "Object-Spatial-Paradigm",
        "category": "advanced",
        "description": "The core paradigm that makes Jac unique",
        "resources": ["jac-osp-1"]
    },
    {
        "concept_id": "by-llm",
        "concept_name": "byLLM Agents",
        "category": "advanced",
        "description": "Integrating AI and LLMs into Jac programs",
        "resources": ["jac-by-llm-1"]
    }
]
