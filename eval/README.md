# Evaluation Guidelines
We provide instructions for evaluation. 
To execute our evaluation script, please ensure that the structure of your model outputs is the same as ours.

We provide two options:
1. Evaluate answer: you can parse the response on your own and simply provide one file with all the final answers.
2. Evaluate Response: you can leave all the responses to us with the output formats shown below.

## Output folder structure

```
└── model_name
    ├── category_name.jsonl
    └── category_name.jsonl
    ...
```

## Evaluate Answer
If you want to use your own parsing logic and *only provide the final answer*, you can use `eval_answer.py`.

### Output file
Each `category_name.json`` has a list of dict containing instances for evaluation.

```
{"id": 1727, "type": "选择", "answer": "ACD"}
{"id": 12080, "type": "判断", "answer": "对"}
{"id": 2356, "type": "填空", "answer": "甲"}
...
```

### Evaluation
```
python eval/eval_answer.py --output_dir eval/example/Yi-VL-34B-answer --answer_dir eval/example/cmmmu-data-val-answer
```


## Evaluate Response
You can also provide response and run the `eval_response.py` to use our answer parsing processing and evaluation pipeline as follows:

### Output file
Each `category_name.json`` has a list of dict containing instances for evaluation.
```
{"id": 1727, "type": "选择", "response": "(A) 黑陶距今约4000年的龙山文化中最重要的代表\n(C) 黑陶具有色泽鲜艳的，黑、光、薄的特点\n(D) 黑陶造型丰富，代表性的器形有碗"}
{"id": 12080, "type": "判断", "response": "正确"}
{"id": 2356, "type": "填空", "response": "甲品种"}
...
```

### Evaluation
```
python eval/eval_response.py --data_dir cmmmu-data-val --output_dir eval/example/Yi-VL-34B-response
```
