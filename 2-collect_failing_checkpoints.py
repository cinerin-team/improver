import re

from configs.variables import LOG1, LOG2, LOG3

if __name__ == '__main__':
    new_fails = set()
    with open(LOG1 + "/verdict.log", "r+") as file:
        file_contents = file.read()
        match = re.search(".*218\s+(PDC.*)\sFailed\!", file_contents, re.MULTILINE)
        print("found: " + match.group(1))
        new_fails.add(match.group(1))

    with open(LOG2 + "/verdict.log", "r+") as file:
        file_contents = file.read()
        match = re.search(".*218\s+(PDC.*)\sFailed\!", file_contents, re.MULTILINE)
        print("found: " + match.group(1))
        new_fails.add(match.group(1))

    with open(LOG3 + "/verdict.log", "r+") as file:
        file_contents = file.read()
        match = re.search(".*218\s+(PDC.*)\sFailed\!", file_contents, re.MULTILINE)
        print("found: " + match.group(1))
        new_fails.add(match.group(1))

    with open("configs/checkpoints.csv", "w") as file:
        for item in new_fails:
            file.write(item + "\n")