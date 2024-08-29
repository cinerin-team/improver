import csv
import re

from configs.variables import FILE_TO_IMPROVE, TARGET_FOLDER
from functions.new_value_calc import new_value_calc

if __name__ == '__main__':
    checkpoints = []
    with open('configs/new_values.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        checkpoints = [row for row in csv_reader]

    for checkpoint in checkpoints:
        with open(TARGET_FOLDER + FILE_TO_IMPROVE, "r+") as file:
            file_contents = file.read()
            match = re.search(
                "^\s*\(\s*verdict.config.tc.result\(\'" + checkpoint['checkpoint']
                .replace("(", "\(").replace(")", "\)") +
                "\(?\w*\)?\'?\)?,\s*verdict\.config\.field\.range\((\d+), (\d+)\),?\s*\),",
                file_contents, re.MULTILINE)

            new_average = (float(checkpoint['new_value1']) + float(checkpoint['new_value2']) + float(
                checkpoint['new_value3'])) / 3
            new_values = new_value_calc(new_average, match.group(1), match.group(2))
            old_line = match.group(0)
            print("for checkpoint: " + checkpoint['checkpoint'] + " old value: " + old_line)
            new_line = re.sub(str("\(" + match.group(1)), "(" + new_values[0], old_line)
            new_line = re.sub(str(match.group(2) + "\)"), new_values[1] + ")", new_line)
            print("new value: " + new_line)
            print()
            file_contents = file_contents.replace(old_line, new_line)
            file.seek(0)
            file.truncate()
            file.write(file_contents)
