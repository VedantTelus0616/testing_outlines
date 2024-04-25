import openai
import pandas as pd
import json
import time
from langchain import PromptTemplate
import random
from tqdm import tqdm

openai.api_base = "https://api.aimlapi.com/"  # use the IP or hostname of your instance
openai.api_key = '2cd60781c98843dfa09cef598719bcd1'

def query_qwen(query_str):
    '''
    Given a query, prompt QWEN for results
    
    query_str: str
    '''

    system_content = "You are a helpful assistant"
    client = openai.OpenAI(api_key = openai.api_key, base_url=openai.api_base)
    chat_completion = client.chat.completions.create(
        model="Qwen/Qwen1.5-72B-Chat",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": query_str},
        ],
        temperature=0.7,
        max_tokens=4096,
    )
    response = chat_completion.choices[0].message.content
    return response


def generate_questions_response_pairs(prompt, 
                                      levels, 
                                      language_concept, 
                                      programming_concepts, 
                                      concepts, 
                                      per_concept_ques):
    dict_list=[]
    for concept in tqdm(concepts):
        t1=time.time()
        for level in levels:
            languages,context=random.choice(language_concept)
            languages=[x.strip() for x in languages.split(',')]
            languages=random.sample(languages,k=3)
            for language in languages:
                programming_concept=random.choice(programming_concepts)
                input_prompt=prompt.format_prompt(CONCEPT=concept,NoQ=per_concept_ques,LANGUAGE=language,LEVEL=level,PROGRAMMING_CONCEPT=programming_concept,CONTEXT=context).to_string()
                # print('input_prompt:',input_prompt)
                response=query_qwen(input_prompt)
                # print('Generated Complex Question :\n',response)
                dict1={'L3':concept,'Level':level,'Questions':response,'Language':language,'Context':context,'Programming_Concept':programming_concept}
                #print('dict1:',dict1)
                # print('-'*100)
                dict_list.append(dict1)
                with open("./output/results_qwen72b_multi_language_concepts.json", "w") as f:
                    json.dump(dict_list, f)
        t2=time.time()
        print('#'*100)
        print('Time taken for a L3 task for a single language for a single difficulty level:',t2-t1)

L3_TASKS = [
"Code synthesis",
"Code retreival",
"Text to SQL",
"Math programming",
"Code snippets & examples",
"Plot generation",
"Generating bash commands",
"Database query generation",
"UI code generation",
"Configuration file generation",
"Completing a function",
"Completing a class",
"Code infilling",
"Predicting next line of code",
"Autocomplete code blocks",
"Variable name suggestion",
"Method signature completion",
"Auto-generate test cases",
"Completing HTML tags",
"Syntax correction",
"Summarizing a file / script / repository in a paragraph (or 5 bullets)",
"Automatic commenting",
"Minify code",
"Extracting main features of code",
"Generating code abstract",
"Visual code summary",
"Code compression techniques",
"Summarizing changes in version control",
"Documentation summarization",
"Inline code summarization",
"Code modification (refactoring)",
"Code optimization",
"Code simplification",
"Code search - given a bit of code, search within it",
"API Mining - e.g. help generating calls for APIs",
"Redundancy Removal",
"Converting loops to recursion",
"Refactoring for readability",
"Refactoring for performance",
"Standardization of code format",
"Linux/Mac/Windows common CLI tasks",
"CLI package management",
"Software development environment config",
"Automated script generation",
"Environment setup automation",
"CLI shortcuts",
"CLI for cloud management",
"CLI tools for network troubleshooting",
"Command line data processing",
"Shell script optimization",
"Package management (for all languages)",
"Code repository management",
"Integration with IDEs",
"Build automation",
"Dependency resolution",
"Cross-platform compatibility checks",
"Ecosystem migration tools",
"Code sharing platforms",
"Collaborative coding tools",
"Real-time code synchronization",
"Code translation (one from language to another)",
"Cross-language API usage",
"Legacy code modernization",
"Interoperability solutions",
"Scripting to compiled code conversion",
"Automatic code localization",
"Platform-specific adaptations",
"Framework-specific code generation",
"Code porting for different OS",
"Multi-language code integration",
"Writing a javadoc for this function",
"Generating comments based on code logic",
"Automatic inline comments",
"Updating outdated comments",
"Generating comments for algorithms",
"Comment based on code complexity",
"Summarizing logical blocks with comments",
"Code annotation for review",
"Extracting and commenting critical sections",
"Tool-generated comment consistency check",
"Creating a descriptive and useful commit text for a code commit",
"Automatic commit classification",
"Semantic commit messaging",
"Code Commit message templates",
"Version control integration for commit messages",
"Multi-language commit support",
"Code Commit summarization for changelogs",
"Context-aware commit suggestions",
"Feature-specific commit messages",
"Code Commit message consistency checker",
"Writing a docstring",
"Extended documentation with examples",
"API endpoint documentation",
"Function parameter details",
"Error handling documentation",
"Performance notes",
"Usage scenarios",
"Deprecation notices",
"Security implications",
"Compatibility notes",
"Basic usage scenario",
"Advanced usage scenario",
"Performance critical use case",
"Error handling example",
"Integration with other functions",
"Cross-platform usage example",
"Thread safety demonstration",
"Usage with optional parameters",
"Deprecation alternatives",
"Common pitfalls and workarounds",
"Endpoint description",
"Parameter details",
"Return values",
"Authentication requirements",
"Error codes explanation",
"Sample request/response",
"Versioning and compatibility",
"Deprecation policy",
"Rate limits",
"Security guidelines",
"Code repair",
"Bug identification",
"Code fix suggestions",
"Defect detection",
"Clone detection",
"bugs in this code",
"fixing the bugs in a code",
" an error message/traceback",
"fixing an error message <message> in a code",
"Debugging Strategies/Tooling",
"Unit Test Generation",
"Testing Strategy (e.g. frameworks/guides)",
"Automated regression testing",
"Integration testing tools",
"Continuous testing practices",
"Load and performance testing",
"Security penetration testing",
"User acceptance testing",
"Code coverage analysis",
"Test data generation",
"Deobfuscation",
"Code classification",
"Peer review automation",
"Static code analysis",
"Code style enforcement",
"Security review integration",
"Review metrics and dashboards",
"Automated refactor suggestions",
"Code smell detection",
"Best practices checklist",
"Identifying mistakes that allow for XSS injection",
"SQL injection prevention",
"Code audit for security vulnerabilities",
"Encryption standards review",
"Authentication mechanism review",
"Access control checks",
"Data privacy compliance",
"Security best practices",
"Third-party library security",
"Secure coding training",
"Code fuzzing",
"Assertion Generation",
"Automated code quality reports",
"Performance profiling",
"Memory leak detection",
"Usability testing",
"Cross-browser testing",
"Mobile responsiveness testing",
"Accessibility compliance",
"Internationalization checks",
"Parsing logs into structured templates",
"Finding anomalies from raw logs",
"Log event correlation",
"Predictive log analysis",
"Log-based alerting",
"Real-time log monitoring",
"Log archiving strategies",
"Log data visualization",
"User behavior analysis from logs",
"Security incident detection through logs"
]


if __name__ == '__main__':
    strategies_file='./input/Strategies_Sheet4.csv'
    strategies_df=pd.read_csv(strategies_file)
    programming_concepts=strategies_df['Programming Concept'].values
    concept1=strategies_df['Context_1'].values
    languages=strategies_df['Languages'].values
    
    language_concept=list(zip(languages,concept1))
    language_concept=language_concept[:-4]
    
    # levels=["high school student","college student","extreme difficult"]
    levels=["college student","extreme difficult", "extreme difficult"]
    per_concept_ques=5
    prompt_template="""
    Generate {NoQ} questions and their responses with example code in {LANGUAGE} language to identify and explain {CONCEPT} for {PROGRAMMING_CONCEPT} in the context of {CONTEXT}. The level of complexity has to be {LEVEL}.
    """
    prompt=PromptTemplate.from_template(prompt_template)
    
    generate_questions_response_pairs(prompt,
                                      levels,
                                      language_concept,
                                      programming_concepts,
                                      L3_TASKS,
                                      per_concept_ques)