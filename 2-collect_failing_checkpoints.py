import re

from configs.variables import LOG1, LOG2, LOG3

if __name__ == '__main__':
    new_fails = set()
    with open(LOG1 + "/verdict.log", "r+") as file:
        file_contents = file.read()
        match = re.findall(".*218\s+PDC.*\sFailed\!.*", file_contents)
        print("found: " + str(match))
        for item in match:
            new_fails.add(item)

    with open(LOG2 + "/verdict.log", "r+") as file:
        file_contents = file.read()
        match = re.findall(".*218\s+PDC.*\sFailed\!.*", file_contents)
        print("found: " + str(match))
        for item in match:
            new_fails.add(item)

    with open(LOG3 + "/verdict.log", "r+") as file:
        file_contents = file.read()
        match = re.findall(".*218\s+PDC.*\sFailed\!.*", file_contents)
        print("found: " + str(match))
        for item in match:
            new_fails.add(item)

    with open("configs/checkpoints.csv", "w") as file:
        for item in new_fails:
            file.write(item + "\n")