import os
import json
import random
from argparse import ArgumentParser
from tabulate import tabulate
from utils.eval_utils import evaluate_response

def read_jsonl_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return {json.loads(line)['id']: json.loads(line) for line in file}

def process_jsonl_file(data_path, output_path, category):
    global global_cnt
    global global_correct_cnt

    data_dict = read_jsonl_to_dict(data_path)
    output_dict = read_jsonl_to_dict(output_path)

    if set(data_dict.keys()) != set(output_dict.keys()):
        print("The ids are not exactly the same and cannot be processed further, please check files")
        return

    for data, output in zip(data_dict.values(), output_dict.values()):
        if data.get('type') == "选择":
            index2ans = {
                'A': data.get('option1', ''),
                'B': data.get('option2', ''),
                'C': data.get('option3', ''),
                'D': data.get('option4', '')
            }
            output['index2ans'] = index2ans
        output['answer'] = data.get('answer')

    results_count = evaluate_response(output_dict.values())
    
    return results_count


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--data_dir', type=str, default="cmmmu-data-val", help="data file path.")
    parser.add_argument('--output_dir', type=str, default="eval/example/Yi-VL-34B-response", help="The path to model output file.")
    args = parser.parse_args()

    category_list = ['art_and_design', 'business', 'science', 'health_and_medicine', 'humanities_and_social_sciences', 'technology_and_engineering']
    headers = ['Subject', 'Correct Num', 'Entries Num', 'Acc']
    table = []
    correct_sum = 0
    entries_sum = 0

    for category in category_list:
        data_path = f'{args.data_dir}/{category}/{category}.jsonl'
        output_path = f'{args.output_dir}/{category}.jsonl'
        results_count = process_jsonl_file(data_path, output_path, category)
        correct_sum += results_count['correct_num']
        entries_sum += results_count['entries_num']
        table.append([category, results_count['correct_num'], results_count['entries_num'], results_count['correct_num']/results_count['entries_num']])

    table.append(['all', correct_sum, entries_sum, correct_sum/entries_sum])
    print(tabulate(table, headers=headers, tablefmt='orgtbl'))