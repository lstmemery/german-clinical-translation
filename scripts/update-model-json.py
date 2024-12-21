import argparse
import json
import re
from functools import partial

parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str)
parser.add_argument("input_regex", type=str)
parser.add_argument("output_prepend", type=str)


def update_model_string(model_string: str, input_regex: str, output_regex: str) -> str:
    return re.sub(input_regex, output_regex, model_string)


def fix_match(match: re.Match, prepend) -> str:
    subscale = int(match.group(1))
    question = int(match.group(2))
    return f'{prepend}{subscale}_{(subscale - 1)*6 + question}'


if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.file_name, "r+") as f:
        data = json.load(f)
        output_partial = partial(fix_match, prepend=args.output_prepend)
        new_model_string = update_model_string(data["model_string"], args.input_regex, output_partial)
        print(new_model_string)
        data["model_string"] = new_model_string
        f.seek(0)
        json.dump(data, f, indent=2)