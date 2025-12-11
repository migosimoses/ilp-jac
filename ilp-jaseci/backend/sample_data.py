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
    },
    {
        "lesson_id": "jac-advanced-walkers-2",
        "title": "Advanced Walker Patterns",
        "category": "walkers",
        "difficulty": "advanced",
        "duration_minutes": 50,
        "description": "Master complex walker patterns and multi-agent systems",
        "prerequisites": ["jac-walkers-1"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "State Management in Walkers",
                "body": """
                <p>Walkers can maintain state as they traverse graphs. This enables 
                sophisticated algorithms and stateful graph processing.</p>
                
                <p>Key state patterns:</p>
                <ul>
                    <li>Tracking visited nodes</li>
                    <li>Accumulating results</li>
                    <li>Conditional branching based on state</li>
                    <li>Stack-based processing</li>
                </ul>
                """,
                "code_example": """walker StatefulWalker {
    has visited: set = set();
    has result: dict = {};
    has depth: int = 0;
    
    can traverse {
        visited.add(here.id);
        depth += 1;
        
        if depth < 5 {
            for n in --> {
                if n.id not in visited {
                    take n;
                }
            }
        }
    }
}""",
                "key_concepts": ["Walker state", "Depth tracking", "Memoization"]
            },
            {
                "section_num": 2,
                "section_title": "Multi-Walker Coordination",
                "body": """
                <p>Multiple walkers can work together on the same graph, enabling 
                parallel and distributed processing patterns.</p>
                """,
                "code_example": """walker Producer {
    can generate_data {
        # Process and produce data
        here.data = compute_result();
        take --> spread_data;
    }
}

walker Consumer {
    can consume_data {
        # Read and aggregate data
        aggregate(here.data);
        take --> next;
    }
}""",
                "key_concepts": ["Multi-walker systems", "Coordination", "Data flow"]
            },
            {
                "section_num": 3,
                "section_title": "Error Handling in Walkers",
                "body": """
                <p>Build robust walkers with proper error handling:</p>
                """,
                "code_example": """walker SafeWalker {
    can process {
        try {
            # Risky operation
            process_node(here);
        } except {
            # Handle gracefully
            log_error(here.id);
            take --> safe_path;
        }
    }
}""",
                "key_concepts": ["Exception handling", "Graceful degradation"]
            }
        ]
    },
    {
        "lesson_id": "jac-graph-algorithms-3",
        "title": "Graph Algorithms in Jac",
        "category": "algorithms",
        "difficulty": "advanced",
        "duration_minutes": 60,
        "description": "Implement classic graph algorithms using Jac walkers",
        "prerequisites": ["jac-advanced-walkers-2"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "Breadth-First Search (BFS)",
                "body": """
                <p>BFS explores a graph level by level. It's useful for finding 
                shortest paths and nearest neighbors.</p>
                """,
                "code_example": """walker BFS {
    has queue: list = [];
    has visited: set = set();
    
    can search {
        if here.id not in visited {
            visited.add(here.id);
            queue.append(here);
            
            for neighbor in --> {
                if neighbor.id not in visited {
                    queue.append(neighbor);
                }
            }
        }
    }
    
    can process_queue {
        while queue {
            node = queue.pop(0);
            take node via search;
        }
    }
}""",
                "key_concepts": ["BFS", "Queue-based traversal", "Level-order search"]
            },
            {
                "section_num": 2,
                "section_title": "Depth-First Search (DFS)",
                "body": """
                <p>DFS explores as far as possible along each branch. Great for 
                topological sorting and cycle detection.</p>
                """,
                "code_example": """walker DFS {
    has visited: set = set();
    has stack: list = [];
    
    can search {
        stack.append(here);
        
        while stack {
            node = stack.pop();
            if node.id not in visited {
                visited.add(node.id);
                process(node);
                
                for neighbor in node --> {
                    if neighbor.id not in visited {
                        stack.append(neighbor);
                    }
                }
            }
        }
    }
}""",
                "key_concepts": ["DFS", "Stack-based traversal", "Backtracking"]
            },
            {
                "section_num": 3,
                "section_title": "PageRank and Centrality",
                "body": """
                <p>Calculate node importance using PageRank and centrality measures:</p>
                """,
                "code_example": """walker Centrality {
    has scores: dict = {};
    has iterations: int = 10;
    
    can calculate_rank {
        for iteration in range(iterations) {
            for node in all_nodes {
                # Iterative rank calculation
                rank = 0.15;  # Base score
                for parent in <-- node {
                    rank += 0.85 * (parent.score / parent.outlinks);
                }
                scores[node.id] = rank;
            }
        }
    }
}""",
                "key_concepts": ["PageRank", "Centrality measures", "Network analysis"]
            }
        ]
    },
    {
        "lesson_id": "jac-knowledge-graphs-4",
        "title": "Building Knowledge Graphs",
        "category": "applications",
        "difficulty": "intermediate",
        "duration_minutes": 55,
        "description": "Design and implement knowledge graphs for real-world applications",
        "prerequisites": ["jac-nodes-1", "jac-osp-1"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "Knowledge Graph Fundamentals",
                "body": """
                <p>A knowledge graph represents entities and relationships in a domain. 
                It's perfect for:</p>
                <ul>
                    <li>Semantic search and question answering</li>
                    <li>Recommendation engines</li>
                    <li>Ontology representation</li>
                    <li>Linked data and knowledge bases</li>
                </ul>
                
                <p>Jac's graph-based nature makes it ideal for knowledge graph work.</p>
                """,
                "code_example": "",
                "key_concepts": ["Knowledge graphs", "Ontologies", "Semantic relationships"]
            },
            {
                "section_num": 2,
                "section_title": "Designing Knowledge Graph Schemas",
                "body": """
                <p>Structure your knowledge graph with proper node and edge types:</p>
                """,
                "code_example": """node Entity {
    has name: str;
    has type: str;
    has properties: dict;
}

node Concept {
    has term: str;
    has definition: str;
}

edge has_property {
    has confidence: float;
}

edge related_to {
    has relationship_type: str;
    has strength: float;
}

edge is_a {
    has inherited: bool;
}""",
                "key_concepts": ["Schema design", "Entity-relationship modeling", "Type systems"]
            },
            {
                "section_num": 3,
                "section_title": "Querying and Reasoning",
                "body": """
                <p>Use walkers to query and reason over your knowledge graph:</p>
                """,
                "code_example": """walker ReasoningEngine {
    has results: list = [];
    
    @by_llm
    can answer_question(question: str) {
        # Use LLM to understand question
        # Walk the knowledge graph
        # Compile and rank results
        return reasoning_results;
    }
    
    can traverse_relationships {
        # Find related entities
        for related in -->has_property {
            results.append(related);
            take related;
        }
    }
}""",
                "key_concepts": ["Graph queries", "Reasoning engines", "Semantic search"]
            }
        ]
    },
    {
        "lesson_id": "jac-performance-optimization-5",
        "title": "Performance Optimization",
        "category": "advanced_topics",
        "difficulty": "advanced",
        "duration_minutes": 50,
        "description": "Optimize Jac programs for performance and scalability",
        "prerequisites": ["jac-advanced-walkers-2"],
        "sections": [
            {
                "section_num": 1,
                "section_title": "Profiling and Analysis",
                "body": """
                <p>Identify bottlenecks in your Jac programs:</p>
                <ul>
                    <li>Graph traversal complexity</li>
                    <li>Memory usage patterns</li>
                    <li>LLM call frequency and cost</li>
                    <li>State accumulation</li>
                </ul>
                
                <p>Use metrics to guide optimization decisions.</p>
                """,
                "code_example": """import time

walker ProfiledWalker {
    has start_time: float;
    has node_count: int = 0;
    
    can traverse {
        start_time = time.time();
        self.traverse_graph();
        elapsed = time.time() - start_time;
        
        print(f"Visited {node_count} nodes in {elapsed}s");
        print(f"Rate: {node_count/elapsed} nodes/sec");
    }
}""",
                "key_concepts": ["Profiling", "Benchmarking", "Performance metrics"]
            },
            {
                "section_num": 2,
                "section_title": "Graph Optimization Techniques",
                "body": """
                <p>Optimize graph structure and traversal:</p>
                <ul>
                    <li>Pruning unnecessary edges</li>
                    <li>Caching traversal results</li>
                    <li>Batch processing</li>
                    <li>Lazy evaluation</li>
                </ul>
                """,
                "code_example": """walker OptimizedWalker {
    has cache: dict = {};
    
    can traverse_cached {
        if here.id in cache {
            # Return cached result
            return cache[here.id];
        }
        
        result = compute_expensive_operation();
        cache[here.id] = result;
        return result;
    }
    
    can batch_process {
        # Process multiple nodes together
        nodes_batch = collect_nearby_nodes(5);
        process_batch(nodes_batch);
    }
}""",
                "key_concepts": ["Caching", "Batch processing", "Lazy evaluation"]
            },
            {
                "section_num": 3,
                "section_title": "Scaling Jac Applications",
                "body": """
                <p>Build Jac applications that scale:</p>
                <ul>
                    <li>Distribute graph across nodes</li>
                    <li>Parallel walker execution</li>
                    <li>Efficient LLM usage and caching</li>
                    <li>Connection pooling and resource management</li>
                </ul>
                """,
                "code_example": """walker DistributedWalker {
    has partition_id: int;
    has num_partitions: int;
    
    can process_partition {
        # Process only nodes for this partition
        for node in get_partition_nodes(partition_id) {
            if node.id % num_partitions == partition_id {
                process(node);
            }
        }
    }
}""",
                "key_concepts": ["Distributed processing", "Partitioning", "Scalability"]
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
    },
    {
        "quiz_id": "quiz-advanced-walkers-2",
        "lesson_id": "jac-advanced-walkers-2",
        "title": "Advanced Walker Patterns Quiz",
        "difficulty": "advanced",
        "questions": [
            {
                "question_id": "q1",
                "question_text": "Which of the following is NOT a state management pattern in walkers?",
                "question_type": "multiple_choice",
                "options": [
                    "Tracking visited nodes",
                    "Accumulating results",
                    "Defining node attributes",
                    "Stack-based processing"
                ],
                "correct_answer": "Defining node attributes"
            },
            {
                "question_id": "q2",
                "question_text": "Multiple walkers can coordinate on the same graph to enable parallel processing.",
                "question_type": "true_false",
                "correct_answer": True
            },
            {
                "question_id": "q3",
                "question_text": "Explain how you would implement cycle detection in a walker.",
                "question_type": "free_text",
                "keywords": ["visited", "tracking", "set", "path"]
            }
        ]
    },
    {
        "quiz_id": "quiz-graph-algorithms-3",
        "lesson_id": "jac-graph-algorithms-3",
        "title": "Graph Algorithms Quiz",
        "difficulty": "advanced",
        "questions": [
            {
                "question_id": "q1",
                "question_text": "Which algorithm uses a queue for level-by-level exploration?",
                "question_type": "multiple_choice",
                "options": [
                    "Breadth-First Search (BFS)",
                    "Depth-First Search (DFS)",
                    "PageRank",
                    "Dijkstra's Algorithm"
                ],
                "correct_answer": "Breadth-First Search (BFS)"
            },
            {
                "question_id": "q2",
                "question_text": "DFS is commonly used for topological sorting and cycle detection.",
                "question_type": "true_false",
                "correct_answer": True
            },
            {
                "question_id": "q3",
                "question_text": "Implement a BFS walker that finds the shortest path between two nodes.",
                "question_type": "code",
                "starter_code": """walker ShortestPath {
    has target_id: str;
    
    can find_path {
        # Your implementation here
    }
}"""
            }
        ]
    },
    {
        "quiz_id": "quiz-knowledge-graphs-4",
        "lesson_id": "jac-knowledge-graphs-4",
        "title": "Knowledge Graphs Quiz",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_id": "q1",
                "question_text": "What is NOT a typical use case for knowledge graphs?",
                "question_type": "multiple_choice",
                "options": [
                    "Image processing",
                    "Semantic search",
                    "Recommendation engines",
                    "Question answering"
                ],
                "correct_answer": "Image processing"
            },
            {
                "question_id": "q2",
                "question_text": "In a knowledge graph, entities are nodes and relationships are edges.",
                "question_type": "true_false",
                "correct_answer": True
            },
            {
                "question_id": "q3",
                "question_text": "Design a small knowledge graph for a movie recommendation system with at least 3 entity types and 2 relationship types.",
                "question_type": "free_text",
                "keywords": ["Movie", "Actor", "Genre", "Director", "starred_in", "has_genre"]
            }
        ]
    },
    {
        "quiz_id": "quiz-performance-5",
        "lesson_id": "jac-performance-optimization-5",
        "title": "Performance Optimization Quiz",
        "difficulty": "advanced",
        "questions": [
            {
                "question_id": "q1",
                "question_text": "Which technique reduces redundant computation by storing previous results?",
                "question_type": "multiple_choice",
                "options": [
                    "Caching",
                    "Batch processing",
                    "Pruning",
                    "Profiling"
                ],
                "correct_answer": "Caching"
            },
            {
                "question_id": "q2",
                "question_text": "Lazy evaluation is a technique to defer computation until results are actually needed.",
                "question_type": "true_false",
                "correct_answer": True
            },
            {
                "question_id": "q3",
                "question_text": "Describe three strategies for scaling a Jac application to handle large graphs.",
                "question_type": "free_text",
                "keywords": ["distributed", "partitioning", "parallel", "caching", "batch"]
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
    },
    {
        "concept_id": "state-management",
        "concept_name": "State Management",
        "category": "advanced",
        "description": "Managing walker state during graph traversal",
        "resources": ["jac-advanced-walkers-2"]
    },
    {
        "concept_id": "multi-walker-systems",
        "concept_name": "Multi-Walker Coordination",
        "category": "advanced",
        "description": "Coordinating multiple walkers for parallel processing",
        "resources": ["jac-advanced-walkers-2"]
    },
    {
        "concept_id": "graph-algorithms",
        "concept_name": "Graph Algorithms",
        "category": "advanced",
        "description": "Implementing BFS, DFS, and centrality algorithms in Jac",
        "resources": ["jac-graph-algorithms-3"]
    },
    {
        "concept_id": "knowledge-graphs",
        "concept_name": "Knowledge Graphs",
        "category": "applications",
        "description": "Building and querying knowledge graphs with Jac",
        "resources": ["jac-knowledge-graphs-4"]
    },
    {
        "concept_id": "performance-optimization",
        "concept_name": "Performance & Scalability",
        "category": "advanced",
        "description": "Optimizing and scaling Jac applications",
        "resources": ["jac-performance-optimization-5"]
    },
    {
        "concept_id": "semantic-search",
        "concept_name": "Semantic Search",
        "category": "applications",
        "description": "Implementing semantic search using knowledge graphs and byLLM",
        "resources": ["jac-knowledge-graphs-4", "jac-by-llm-1"]
    },
    {
        "concept_id": "error-handling",
        "concept_name": "Error Handling",
        "category": "intermediate",
        "description": "Building robust Jac programs with exception handling",
        "resources": ["jac-advanced-walkers-2"]
    }
]
