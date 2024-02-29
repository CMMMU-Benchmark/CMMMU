# Evaluation Guidelines
We provide instructions for evaluation. 
To execute our evaluation script, please ensure that the structure of your model outputs is the same as ours.

We provide two options:
1. Evaluate Answer: you can parse the responses on your own and simply provide one file with all the final answers.
2. Evaluate Response: you can leave all the responses to us with the output formats shown below.

You can use `eval/eval_script.py` to evaluate your results. This script will automatically select the evaluation method based on whether `your_output_file.jsonl` content contains `"answer"` or `"response"`.

## Evaluate Answer
If you want to use your own parsing logic and *only provide the final answer*, `your_output_file.jsonl` must only contain three fields: `"id"`, `"type"`, `"answer"` formatted as follows.

### Output File
`your_output_file.jsonl` has a list of dict containing instances for evaluation.

```
{"id": 1727, "type": "选择", "answer": "ACD"} # format like "A" "BC" etc. for multi-choice question
{"id": 12080, "type": "判断", "answer": "对"} # strictly "对" or "错" for true or false question
{"id": 2356, "type": "填空", "answer": "甲"} # any string response for fill in the blank question
...
```

### Evaluation Example
```
python eval/eval_script.py --output_path eval/example/Yi-VL-34B-answer.jsonl --data_path eval/example/cmmmu-data-val-answer.jsonl
```


## Evaluate Response
You can also provide response and run the `eval_script.py` to use our answer parsing processing and evaluation pipeline, just make sure `your_output_file.jsonl` only contains three fields: `"id"`, `"type"`, `"response"` formatted as follows.

### Output File
`your_output_file.jsonl` has a list of dict containing instances for evaluation.
```
{"id": 1727, "type": "选择", "response": "(A) 黑陶距今约4000年的龙山文化中最重要的代表\n(C) 黑陶具有色泽鲜艳的，黑、光、薄的特点\n(D) 黑陶造型丰富，代表性的器形有碗"}  # any string response
{"id": 12080, "type": "判断", "response": "正确"}  # any string response
{"id": 2356, "type": "填空", "response": "甲品种"}  # any string response
...
```

### Evaluation Example
```
python eval/eval_script.py --output_path eval/example/Yi-VL-34B-response.jsonl --data_path eval/example/cmmmu-data-val-answer.jsonl
```
