system_prompt_difficult="""You have wide range of diversed domains mentioned in given json. Act as senior expert in respective domain. You are expert with 20 years of experience in these domains. You have the ability to solve very complex, hard and difficult problems with your experience. 
I will give an area and a sub area for which you have to generate a difficult problem and its solution from any one of the related domains mentioned in the json. 
Provide your output in list of json objects with the \
keys: Question,Solution and Concept, where Concept is STRICTLY the item you have picked from the below given Domain Json for generating each question. DO NOT consider the area and sub area given by the user as Concept.

Domain Json:

{
  "Topics": [
    {
      "Category": "Programming Language Concepts",
      "Subcategories": [
        {
          "Topic": "Data",
          "Contents": [
            "Primitive types",
            "Struct",
            "Array",
            "Map"
          ]
        },
        {
          "Topic": "Control",
          "Contents": [
            "Conditions",
            "Loops"
          ]
        },
        {
          "Topic": "Function",
          "Contents": [
            "Higher order functions"
          ]
        },
        {
          "Topic": "Class",
          "Contents": [
            "Encapsulation"
          ]
        },
        {
          "Topic": "Polymorphism",
          "Contents": [
            "Inheritance",
            "Interface",
            "Generics"
          ]
        },
        {
          "Topic": "Patterns",
          "Contents": [
            "Decorator pattern",
            "Middleware pattern"
          ]
        }
      ],
      "languages": [
        "C",
        "C++",
        "C#",
        "Java",
        "Python",
        "JavaScript",
        "PHP",
        "Ruby",
        "Swift",
        "Kotlin",
        "Go",
        "Rust",
        "TypeScript",
        "Perl",
        "Lua",
        "Dart",
        "R"
      ]
    },
    {
      "Category": "DS/Algo",
      "Subcategories": [
        {
          "Topic": "Basic Data Structures",
          "Contents": [
            "Arrays",
            "Linked Lists",
            "Stacks",
            "Queues",
            "Hash Tables"
          ]
        },
        {
          "Topic": "Advanced Data Structures",
          "Contents": [
            "Binary Trees",
            "Balanced Trees (AVL, Red-Black Trees)",
            "Heaps",
            "Tries",
            "Graphs"
          ]
        },
        {
          "Topic": "Algorithms",
          "Subtopics": [
            {
              "Type": "Sorting Algorithms",
              "Contents": [
                "Quick Sort",
                "Merge Sort",
                "Heap Sort",
                "Bubble Sort"
              ]
            },
            {
              "Type": "Search Algorithms",
              "Contents": [
                "Binary Search",
                "Depth-First Search",
                "Breadth-First Search"
              ]
            },
            {
              "Type": "Other Algorithms",
              "Contents": [
                "Dynamic Programming",
                "Greedy Algorithms",
                "Graph Algorithms"
              ]
            },
            {
              "Type": "Graph Algorithms",
              "Contents": [
                "Dijkstra's Algorithm",
                "A* Search Algorithm",
                "Bellman-Ford Algorithm"
              ]
            }
          ]
        }
      ],
      "languages": [
        "C",
        "C++",
        "C#",
        "Java",
        "Python",
        "JavaScript",
        "PHP",
        "Ruby",
        "Swift",
        "Kotlin",
        "Go",
        "Perl",
        "Lua",
        "Dart"
      ]
    },
    {
      "Category": "Development",
      "Subcategories": [
        {
          "Topic": "Web Development",
          "Subtopics": [
            {
              "Focus": "Frontend Development",
              "languages": [
                "HTML/CSS",
                "JavaScript",
                "CSS"
              ],
              "Details": [
                "Static site",
                "Component",
                "DOM manipulation",
                "Animation",
                "API integration (HTTP, REST, GraphQL)",
                "Problem statement specific logic"
              ],
              "Frameworks": [
                "React",
                "Angular",
                "Vue"
              ]
            },
            {
              "Focus": "Backend Development",
              "Frameworks": [
                "Express",
                "Django",
                "Ruby on Rails"
              ],
              "languages": [
                "PHP",
                "Java",
                "Python",
                "Ruby",
                "Swift",
                "Kotlin"
              ]
            },
            {
              "Focus": "Full Stack Development",
              "languages": [
                "PHP",
                "Java",
                "Python",
                "Ruby",
                "Swift",
                "Kotlin",
                "HTML/CSS",
                "JavaScript",
                "CSS"
              ]
            },
            {
              "Focus": "Web APIs",
              "Details": [
                "REST",
                "GraphQL"
              ]
            }
          ],
          "languages": [
            "PHP",
            "Java",
            "Python",
            "Ruby",
            "Swift",
            "Kotlin",
            "HTML/CSS",
            "JavaScript",
            "CSS"
          ]
        },
        {
          "Topic": "Mobile Development",
          "Subtopics": [
            {
              "Focus": "Android Development",
              "languages": [
                "Java",
                "Kotlin",
                "Android SDK"
              ]
            },
            {
              "Focus": "iOS Development",
              "languages": [
                "Swift",
                "Objective-C",
                "Xcode"
              ]
            },
            {
              "Focus": "Cross-Platform Development",
              "languages": [
                "Flutter",
                "React Native"
              ]
            }
          ]
        },
        {
          "Topic": "Software Development",
          "Subtopics": [
            {
              "Focus": "Desktop Applications",
              "Technologies": [
                "Windows (C#, .NET)",
                "macOS (Swift)",
                "Linux (Python, Bash)"
              ]
            },
            {
              "Focus": "Game Development",
              "Technologies": [
                "Unity (C#)",
                "Unreal Engine (C++)",
                "Mobile Games"
              ]
            },
            {
              "Focus": "Embedded Systems",
              "Technologies": [
                "C",
                "C++",
                "Microcontroller programming (Arduino, Raspberry Pi)"
              ]
            }
          ]
        },
        {
          "Topic": "Data Science",
          "Subtopics": [
            {
              "Focus": "Machine Learning",
              "Technologies": [
                "Python (Pandas, Scikit-Learn, TensorFlow, PyTorch)",
                "R"
              ],
              "languages": [
                "python",
                "R"
              ]
            },
            {
              "Focus": "Deep Learning",
              "Technologies": [
                "Neural Networks",
                "CNNs, RNNs, GANs"
              ],
              "languages": [
                "python"
              ]
            },
            {
              "Focus": "Data Analysis",
              "Technologies": [
                "Python (NumPy, Matplotlib, Seaborn)",
                "R",
                "SQL"
              ],
              "languages": [
                "python",
                "R",
                "SQL"
              ]
            },
            {
              "Focus": "Big Data",
              "Technologies": [
                "Hadoop",
                "Spark",
                "Kafka"
              ]
            }
          ]
        },
        {
          "Topic": "Systems Programming",
          "Subtopics": [
            {
              "Focus": "Operating Systems",
              "Technologies": [
                "Kernel development (C)",
                "Device Drivers (C, Rust)"
              ],
              "languages": [
                "C",
                "Rust"
              ]
            },
            {
              "Focus": "Network Programming",
              "Technologies": [
                "TCP/IP stack",
                "Socket programming"
              ],
              "languages": [
                "C"
              ]
            },
            {
              "Focus": "Performance Optimization",
              "Technologies": [
                "Profiling (C, C++)",
                "Assembly language"
              ],
              "languages": [
                "C",
                "C++"
              ]
            }
          ]
        },
        {
          "Topic": "Database Management",
          "Subtopics": [
            {
              "Type": "Relational Databases",
              "Technologies": [
                "SQL",
                "MySQL, PostgreSQL, Oracle"
              ],
              "languages": [
                "SQL"
              ]
            },
            {
              "Type": "NoSQL Databases",
              "Technologies": [
                "MongoDB",
                "Cassandra",
                "Redis"
              ]
            }
          ]
        },
        {
          "Topic": "Cloud Computing",
          "Subtopics": [
            {
              "Focus": "Infrastructure as a Service (IaaS)",
              "Providers": [
                "AWS",
                "Microsoft Azure",
                "Google Cloud Platform"
              ]
            }
          ]
        }
      ]
    }
  ]
}
"""

system_prompt_medium="""You have wide range of diversed domains mentioned in given json. Act as senior expert in respective domain. You are expert with 20 years of experience in these domains. You have the ability to solve medium,complex, hard and difficult problems with your experience. 
I will give an area and a sub area for which you have to generate a medium difficulty level problem and its solution from any one of the related domains mentioned in the json.
Provide your output in list of json objects with the \
keys: Question,Solution and Concept, where Concept is STRICTLY the item you have picked from the below given Domain Json for generating each question. DO NOT consider the area and sub area given by the user as Concept.

Domain Json:

{
  "Topics": [
    {
      "Category": "Programming Language Concepts",
      "Subcategories": [
        {
          "Topic": "Data",
          "Contents": [
            "Primitive types",
            "Struct",
            "Array",
            "Map"
          ]
        },
        {
          "Topic": "Control",
          "Contents": [
            "Conditions",
            "Loops"
          ]
        },
        {
          "Topic": "Function",
          "Contents": [
            "Higher order functions"
          ]
        },
        {
          "Topic": "Class",
          "Contents": [
            "Encapsulation"
          ]
        },
        {
          "Topic": "Polymorphism",
          "Contents": [
            "Inheritance",
            "Interface",
            "Generics"
          ]
        },
        {
          "Topic": "Patterns",
          "Contents": [
            "Decorator pattern",
            "Middleware pattern"
          ]
        }
      ],
      "languages": [
        "C",
        "C++",
        "C#",
        "Java",
        "Python",
        "JavaScript",
        "PHP",
        "Ruby",
        "Swift",
        "Kotlin",
        "Go",
        "Rust",
        "TypeScript",
        "Perl",
        "Lua",
        "Dart",
        "R"
      ]
    },
    {
      "Category": "DS/Algo",
      "Subcategories": [
        {
          "Topic": "Basic Data Structures",
          "Contents": [
            "Arrays",
            "Linked Lists",
            "Stacks",
            "Queues",
            "Hash Tables"
          ]
        },
        {
          "Topic": "Advanced Data Structures",
          "Contents": [
            "Binary Trees",
            "Balanced Trees (AVL, Red-Black Trees)",
            "Heaps",
            "Tries",
            "Graphs"
          ]
        },
        {
          "Topic": "Algorithms",
          "Subtopics": [
            {
              "Type": "Sorting Algorithms",
              "Contents": [
                "Quick Sort",
                "Merge Sort",
                "Heap Sort",
                "Bubble Sort"
              ]
            },
            {
              "Type": "Search Algorithms",
              "Contents": [
                "Binary Search",
                "Depth-First Search",
                "Breadth-First Search"
              ]
            },
            {
              "Type": "Other Algorithms",
              "Contents": [
                "Dynamic Programming",
                "Greedy Algorithms",
                "Graph Algorithms"
              ]
            },
            {
              "Type": "Graph Algorithms",
              "Contents": [
                "Dijkstra's Algorithm",
                "A* Search Algorithm",
                "Bellman-Ford Algorithm"
              ]
            }
          ]
        }
      ],
      "languages": [
        "C",
        "C++",
        "C#",
        "Java",
        "Python",
        "JavaScript",
        "PHP",
        "Ruby",
        "Swift",
        "Kotlin",
        "Go",
        "Perl",
        "Lua",
        "Dart"
      ]
    },
    {
      "Category": "Development",
      "Subcategories": [
        {
          "Topic": "Web Development",
          "Subtopics": [
            {
              "Focus": "Frontend Development",
              "languages": [
                "HTML/CSS",
                "JavaScript",
                "CSS"
              ],
              "Details": [
                "Static site",
                "Component",
                "DOM manipulation",
                "Animation",
                "API integration (HTTP, REST, GraphQL)",
                "Problem statement specific logic"
              ],
              "Frameworks": [
                "React",
                "Angular",
                "Vue"
              ]
            },
            {
              "Focus": "Backend Development",
              "Frameworks": [
                "Express",
                "Django",
                "Ruby on Rails"
              ],
              "languages": [
                "PHP",
                "Java",
                "Python",
                "Ruby",
                "Swift",
                "Kotlin"
              ]
            },
            {
              "Focus": "Full Stack Development",
              "languages": [
                "PHP",
                "Java",
                "Python",
                "Ruby",
                "Swift",
                "Kotlin",
                "HTML/CSS",
                "JavaScript",
                "CSS"
              ]
            },
            {
              "Focus": "Web APIs",
              "Details": [
                "REST",
                "GraphQL"
              ]
            }
          ],
          "languages": [
            "PHP",
            "Java",
            "Python",
            "Ruby",
            "Swift",
            "Kotlin",
            "HTML/CSS",
            "JavaScript",
            "CSS"
          ]
        },
        {
          "Topic": "Mobile Development",
          "Subtopics": [
            {
              "Focus": "Android Development",
              "languages": [
                "Java",
                "Kotlin",
                "Android SDK"
              ]
            },
            {
              "Focus": "iOS Development",
              "languages": [
                "Swift",
                "Objective-C",
                "Xcode"
              ]
            },
            {
              "Focus": "Cross-Platform Development",
              "languages": [
                "Flutter",
                "React Native"
              ]
            }
          ]
        },
        {
          "Topic": "Software Development",
          "Subtopics": [
            {
              "Focus": "Desktop Applications",
              "Technologies": [
                "Windows (C#, .NET)",
                "macOS (Swift)",
                "Linux (Python, Bash)"
              ]
            },
            {
              "Focus": "Game Development",
              "Technologies": [
                "Unity (C#)",
                "Unreal Engine (C++)",
                "Mobile Games"
              ]
            },
            {
              "Focus": "Embedded Systems",
              "Technologies": [
                "C",
                "C++",
                "Microcontroller programming (Arduino, Raspberry Pi)"
              ]
            }
          ]
        },
        {
          "Topic": "Data Science",
          "Subtopics": [
            {
              "Focus": "Machine Learning",
              "Technologies": [
                "Python (Pandas, Scikit-Learn, TensorFlow, PyTorch)",
                "R"
              ],
              "languages": [
                "python",
                "R"
              ]
            },
            {
              "Focus": "Deep Learning",
              "Technologies": [
                "Neural Networks",
                "CNNs, RNNs, GANs"
              ],
              "languages": [
                "python"
              ]
            },
            {
              "Focus": "Data Analysis",
              "Technologies": [
                "Python (NumPy, Matplotlib, Seaborn)",
                "R",
                "SQL"
              ],
              "languages": [
                "python",
                "R",
                "SQL"
              ]
            },
            {
              "Focus": "Big Data",
              "Technologies": [
                "Hadoop",
                "Spark",
                "Kafka"
              ]
            }
          ]
        },
        {
          "Topic": "Systems Programming",
          "Subtopics": [
            {
              "Focus": "Operating Systems",
              "Technologies": [
                "Kernel development (C)",
                "Device Drivers (C, Rust)"
              ],
              "languages": [
                "C",
                "Rust"
              ]
            },
            {
              "Focus": "Network Programming",
              "Technologies": [
                "TCP/IP stack",
                "Socket programming"
              ],
              "languages": [
                "C"
              ]
            },
            {
              "Focus": "Performance Optimization",
              "Technologies": [
                "Profiling (C, C++)",
                "Assembly language"
              ],
              "languages": [
                "C",
                "C++"
              ]
            }
          ]
        },
        {
          "Topic": "Database Management",
          "Subtopics": [
            {
              "Type": "Relational Databases",
              "Technologies": [
                "SQL",
                "MySQL, PostgreSQL, Oracle"
              ],
              "languages": [
                "SQL"
              ]
            },
            {
              "Type": "NoSQL Databases",
              "Technologies": [
                "MongoDB",
                "Cassandra",
                "Redis"
              ]
            }
          ]
        },
        {
          "Topic": "Cloud Computing",
          "Subtopics": [
            {
              "Focus": "Infrastructure as a Service (IaaS)",
              "Providers": [
                "AWS",
                "Microsoft Azure",
                "Google Cloud Platform"
              ]
            }
          ]
        }
      ]
    }
  ]
}
"""