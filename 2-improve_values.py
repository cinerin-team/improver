import csv
import re

from configs.variables import FILE_TO_IMPROVE, TARGET_FOLDER


def new_value_calc(new_values_loc, o1, o2):
    old_middle = (int(o1) + int(o2)) / 2
    old_distance_from_middle_in_percent = ((old_middle - int(o1)) / old_middle) * 100
    tmp = 0.0
    for i in new_values_loc:
        tmp += float(i)
    new_average = tmp / len(new_values_loc)
    lower = round(new_average - new_average * old_distance_from_middle_in_percent / 100)
    higher = round(new_average + new_average * old_distance_from_middle_in_percent / 100)
    return [str(lower), str(higher)]


if __name__ == '__main__':
    checkpoints = []
    with open('configs/new_values.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        checkpoints = [row for row in csv_reader]

    for checkpoint in checkpoints:
        with open(TARGET_FOLDER + FILE_TO_IMPROVE, "r+") as file:
            file_contents = file.read()
            match = re.search("^\s*\(\s*verdict.config.tc.result\(\'" + checkpoint[
                'checkpoint'] + "\(?\w*\)?\'?\),\s*verdict\.config\.field\.range\((\d+), (\d+)\),?\s*\),",
                              file_contents, re.MULTILINE)
            new_values = new_value_calc(
                [checkpoint['new_value1'], checkpoint['new_value2'], checkpoint['new_value3']], match.group(1),
                match.group(2))
            old_line = match.group(0)
            print("for checkpoint: " + checkpoint + " old value: " + old_line)
            new_line = re.sub(str("\(" + match.group(1)), "(" + new_values[0], old_line)
            new_line = re.sub(str(match.group(2) + "\)"), new_values[1] + ")", new_line)
            print("new value: " + new_line)
            file_contents = file_contents.replace(old_line, new_line)
            file.seek(0)
            file.truncate()
            file.write(file_contents)
