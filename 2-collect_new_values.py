import re

from configs.variables import LOG1, RESULT_VALUE_FILE, LOG3, LOG2

if __name__ == '__main__':
    new_values = {}

    f = open("configs/checkpoints.csv", "r+")
    for line in f:
        new_values[line.strip()] = []
    f.close()

    for checkpoint in new_values.keys():
        with open(LOG1 + RESULT_VALUE_FILE, "r+") as file:
            file_contents = file.read()
            match = re.search(checkpoint + "\(?\w*\)?\:\s(\d+\.?\d*)", file_contents, re.MULTILINE)
            new_values[checkpoint].append(match.group(1))

    for checkpoint in new_values.keys():
        with open(LOG2 + RESULT_VALUE_FILE, "r+") as file:
            file_contents = file.read()
            match = re.search(checkpoint + "\(?\w*\)?\:\s(\d+\.?\d*)", file_contents, re.MULTILINE)
            new_values[checkpoint].append(match.group(1))

    for checkpoint in new_values.keys():
        with open(LOG3 + RESULT_VALUE_FILE, "r+") as file:
            file_contents = file.read()
            match = re.search(checkpoint + "\(?\w*\)?\:\s(\d+\.?\d*)", file_contents, re.MULTILINE)
            new_values[checkpoint].append(match.group(1))

    with open("configs/new_values.csv", "w") as file:
        file.write("checkpoint,new_value1,new_value2,new_value3\n")
        for value in new_values.keys():
            print("found value: " + value + ", " + new_values[value][0] + "," + new_values[value][1] + "," +
                  new_values[value][2])
            file.write(
                value + ", " + new_values[value][0] + "," + new_values[value][1] + "," + new_values[value][2] + "\n")
