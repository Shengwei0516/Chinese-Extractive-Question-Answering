import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Finetune a transformers model on a Question Answering task")
    parser.add_argument(
        "--context_file",
        type=str,
        default=None,
        help="A json file containing the Context data."
    )
    parser.add_argument(
        "--train_file",
        type=str,
        default=None,
        help="A json file containing the Train data."
    )
    parser.add_argument(
        "--validation_file",
        type=str,
        default=None,
        help="A json file containing the Validation data."
    )
    parser.add_argument(
        "--test_file",
        type=str,
        default=None,
        help="A json file containing the Test data."
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge training data and validation data."
    )
    parser.add_argument(
        "--end_to_end",
        action="store_true",
        help="Train a end-to-end transformer-based model."
    )
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_args()

    def expected_format(path: str, test: bool = False) -> dict:

        CONTEXT = json.load(open(args.context_file, "r", encoding="utf-8"))
        data = json.load(open(path, "r", encoding="utf-8"))
        new_data = []
        for i in range(len(data)):
            new = {}
            

            if args.end_to_end:
                if test:
                    label = 0
                    answer_start = 0
                else:
                    label = data[i]["paragraphs"].index(data[i]["relevant"])
                    answer_start = data[i]["answer"]["start"]
                
                context = ""
                for j in range(4):
                    ending = CONTEXT[data[i]["paragraphs"][j]]
                    context += ending
                    if i < label:
                        answer_start += len(ending)

                new["answers"] = {}

                if test:
                    new["answers"]["answer_start"] = [0]
                    new["answers"]["text"] = [""]
                else:
                    new["answers"]["answer_start"] = [answer_start]
                    new["answers"]["text"] = [data[i]["answer"]["text"]]
                
                new["context"] = context
                new["id"] = data[i]["id"]
                new["question"] = data[i]["question"]

            else:
                new["question"] = data[i]["question"]
                new["id"] = data[i]["id"]
                new["sent1"] = data[i]["question"]
                new["sent2"] = data[i]["question"]
                new["ending0"] = CONTEXT[data[i]["paragraphs"][0]]
                new["ending1"] = CONTEXT[data[i]["paragraphs"][1]]
                new["ending2"] = CONTEXT[data[i]["paragraphs"][2]]
                new["ending3"] = CONTEXT[data[i]["paragraphs"][3]]
                if test:
                    new["label"] = 0
                    new["context"] = ""
                    new["answers"] = {}
                    new["answers"]["text"] = [""]
                    new["answers"]["answer_start"] = [0]
                    
                else:
                    new["label"] = data[i]["paragraphs"].index(data[i]["relevant"])
                    new["context"] = CONTEXT[data[i]["relevant"]]
                    new["answers"] = {}
                    new["answers"]["text"] = [data[i]["answer"]["text"]]
                    new["answers"]["answer_start"] = [data[i]["answer"]["start"]]
            new_data.append(new)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)

        print(f"Formatting completed --> {path}")

        return new_data

    if args.context_file:
        if args.train_file:
            train_data = expected_format(args.train_file)
        if args.validation_file:
            valid_data = expected_format(args.validation_file)
            if args.merge:
                train_data += valid_data
                with open(args.train_file, "w", encoding="utf-8") as file:
                    json.dump(train_data, file, ensure_ascii=False, indent=4)

        if args.test_file:
            expected_format(args.test_file, test=True)


if __name__ == "__main__":
    main()
