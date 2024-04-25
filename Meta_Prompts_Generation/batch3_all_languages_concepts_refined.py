import os
import openai
import json
import time
import pandas as pd
from langchain import PromptTemplate
import random
from tqdm import tqdm
from system_msg import system_prompt_difficult,system_prompt_medium

openai.api_base = "https://api.aimlapi.com/"  # use the IP or hostname of your instance
openai.api_key = '2cd60781c98843dfa09cef598719bcd1'


def query_qwen(query_str,system_content):
    '''
    Given a query, prompt QWEN for results
    
    query_str: str
    '''

    #system_content = "You are a helpful assistant"
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


def generate_code_prompts(input_file,output_file,prompt,system_prompt_difficult,system_prompt_medium,levels,per_topic_ques):
    df=pd.read_excel(input_file)
    #print(df.head)
    df_dict_list=df.to_dict('records')
    out_dict_list=[]
    for i in tqdm(range(len(df_dict_list))):
        t1=time.time()
        l2_task=df_dict_list[i]['L2 Category']
        l3_task=df_dict_list[i]['L3 Category']
        for level in levels:
            input_prompt = prompt.format_prompt(L2_TASK=l2_task,L3_TASK=l3_task,NO_QUES=per_topic_ques,LEVEL=level).to_string()
            if level=="medium":
                response=query_qwen(input_prompt,system_prompt_medium)
            else:
                response=query_qwen(input_prompt,system_prompt_difficult)
            print('\n input prompt :\n',input_prompt)
            print('\n response:\n',response)
            print('-'*100)
            out_dict_list.append({"L2_TASK":l2_task,"L3_TASK":l3_task,"Complexity_Level":level,"Response":response})
            with open(output_file, "w") as f:
                json.dump(out_dict_list, f)
        t2=time.time()
        print("\n Time taken in response generation :",t2-t1)

        
if __name__ == '__main__':
    levels=["medium","extremely difficult"]
    prompt_template="""Generate {NO_QUES} questions and their responses with example code in suitable language for Area: “{L2_TASK}”, Sub Area: “{L3_TASK}”. The level of complexity has to be {LEVEL}."""
    prompt=PromptTemplate.from_template(prompt_template)
    input_file="./input/L2_L3_Tasks.xlsx"
    output_folder="./output/Batch3"
    per_topic_ques=2
    num_iteration=10
    
    #Running the generate_code_prompts() 10 times in a loop
    for i in tqdm(range(num_iteration)):
        output_filename="Batch3_all_languages_concept_iter_{}.json".format(str(i))
        output_path=os.path.join(output_folder,output_filename)
        generate_code_prompts(input_file,output_path,prompt,system_prompt_difficult,system_prompt_medium,levels,per_topic_ques)