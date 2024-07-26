import json
import re

from configs.variables import LOG1, LOG2, LOG3

if __name__ == '__main__':
    new_fails = set()
    key_to_find = 'Failure Reason'

    def find_values(key, json_obj):
        """Rekurzívan megkeresi a megadott kulcs értékeit a JSON struktúrában"""
        results = []

        def _find_values(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == key:
                        results.append(v)
                    if isinstance(v, (dict, list)):
                        _find_values(v)
            elif isinstance(obj, list):
                for item in obj:
                    _find_values(item)

        _find_values(json_obj)
        return results


    with open(LOG1 + "/verdict.json", "r+") as f:
        json_data = json.load(f)
    values = find_values(key_to_find, json_data)
    for item1 in values:

        match = re.findall(".*31m(.*)\(\d+\.?\d+\) not inbetween.*", item1)
        print("found: " + str(match))
        for item in match:
            new_fails.add(item)


    # with open(LOG1 + "/verdict.json", "r+") as file:
    #     file_contents = file.read()
    #     match = re.findall(".*218\s+PDC.*\sFailed\!.*", file_contents)
    #     print("found: " + str(match))
    #     for item in match:
    #         new_fails.add(item)

    # with open(LOG2 + "/verdict.log", "r+") as file:
    #     file_contents = file.read()
    #     match = re.findall(".*218\s+PDC.*\sFailed\!.*", file_contents)
    #     print("found: " + str(match))
    #     for item in match:
    #         new_fails.add(item)
    #
    # with open(LOG3 + "/verdict.log", "r+") as file:
    #     file_contents = file.read()
    #     match = re.findall(".*218\s+PDC.*\sFailed\!.*", file_contents)
    #     print("found: " + str(match))
    #     for item in match:
    #         new_fails.add(item)

    with open("configs/checkpoints.csv", "w") as file:
        for item in new_fails:
            file.write(item + "\n")