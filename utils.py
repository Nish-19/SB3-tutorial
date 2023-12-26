import json 

def get_code_dict(student_ids, pivot_code_id, code_df):
    code_dict = {}
    for student_id in student_ids:
        code_dict[student_id] = list(code_df[code_df['CodeStateID'] == student_id]['Code'].values)[0]
    # add pivot code
    code_dict[pivot_code_id] = list(code_df[code_df['CodeStateID'] == pivot_code_id]['Code'].values)[0]
    return code_dict

def get_problem_statement():
    with open('IRT_dataset/problem_502_45.txt') as f:
        problem_statement = f.read()
    return problem_statement

def get_pivot_code_id():
    with open('IRT_dataset/502_45/pivot_code_id.txt') as f:
        pivot_code_id = f.read().strip()
    return pivot_code_id

def load_test_cases():
    '''
    Load test cases from the test_cases folder
    '''
    with open('IRT_dataset/502_45/test_cases.json') as f:
        test_cases = json.load(f)
    return test_cases