import re

from configs.variables import log1, result_value_file, log3, log2

if __name__ == '__main__':
    new_values = {}

    f = open("configs/checkpoints.csv", "r+")
    for line in f:
        new_values[line.strip()] = []
    f.close()

    for checkpoint in new_values.keys():
        with open(log1 + "/epg_testdata/" + result_value_file, "r+") as file:
            file_contents = file.read()
            match = re.search(checkpoint + "\(?\w*\)?\:\s(\d+\.?\d*)", file_contents, re.MULTILINE)
            new_values[checkpoint].append(match.group(1))

    for checkpoint in new_values.keys():
        with open(log2 + "/epg_testdata/" + result_value_file, "r+") as file:
            file_contents = file.read()
            match = re.search(checkpoint + "\(?\w*\)?\:\s(\d+\.?\d*)", file_contents, re.MULTILINE)
            new_values[checkpoint].append(match.group(1))

    for checkpoint in new_values.keys():
        with open(log3 + "/epg_testdata/" + result_value_file, "r+") as file:
            file_contents = file.read()
            match = re.search(checkpoint + "\(?\w*\)?\:\s(\d+\.?\d*)", file_contents, re.MULTILINE)
            new_values[checkpoint].append(match.group(1))

    with open("configs/new_values.csv", "w") as file:
        file.write("checkpoint,new_value1,new_value2,new_value3\n")
        for value in new_values.keys():
            file.write(
                value + ", " + new_values[value][0] + "," + new_values[value][1] + "," + new_values[value][2] + "\n")
