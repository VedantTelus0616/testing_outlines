import pandas as pd
import json
import re
import getopt
import sys
def split_response(input,fieldname):
    file_name = input
    with open(file_name, 'r') as file:
        data = json.load(file)
    final_retrieved_questions = []
    final_retrieved_responses = []
    for data_items in data:
        question = data_items[fieldname]
        # print(question)
        q1= re.split("Question", question)
        q2 = []
        r2 = []
        for question in q1:
            beta = re.split("Answer", question)
            no_of_words = len(beta[0].split())
            if len(beta) > 1 and no_of_words > 10:
                no_of_words2 = len(beta[1].split())
            if len(beta) > 1  and no_of_words > 10:
                q2.append(beta[0])
                r2.append(beta[1])
            gamma = re.split("Solution", question)

            no_of_words = len(gamma[0].split())
            if len(gamma) > 1:
                no_of_words2 = len(gamma[1].split())
            if len(gamma) > 1 and no_of_words > 10 :
                q2.append(gamma[0])
                r2.append(gamma[1])
        q3 = []
        r3 = []
        for question in q2:
            question = re.sub(r'^[\W\d]+', '', question)
            question = re.sub(r'\W+$', '', question)
            q3.append(question)
        final_retrieved_questions.append(q3)
        for response in r2:
            response = re.sub(r'^[\W\d]+', '', response)
            response = re.sub(r'\W+$', '', response)
            r3.append(response)
        final_retrieved_responses.append(r3)
    for data_items in data:
        data_items['extracted_questions'] = final_retrieved_questions[data.index(data_items)]
        data_items['extracted_responses'] = final_retrieved_responses[data.index(data_items)]
    final_file_name = file_name + '_extracted_question.json'
    with open(final_file_name, 'w') as file:
        json.dump(data, file, indent=4)
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:f:", ["input=", "fieldname="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    filename = None
    fieldname = None
    output = 'output.txt'
    
    for opt, arg in opts:
        if opt in ("-i", "--input"):
            filename = arg
        elif opt in ("-f", "--fieldname"):
            fieldname = arg
    
    if filename is None or fieldname is None:
        print("Both filename and fieldname are required.")
        sys.exit(2)

    split_response(filename, fieldname)