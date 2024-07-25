import csv
import difflib
import os.path
import shutil
import base64

from configs.variables import REPO_FOLDER, FILE_TO_IMPROVE, TARGET_FOLDER, EPGCATS_VERSION, ADDITIONAL_FILES_TO_COPY


# Encrypt strings to hide special characters
def encrypt_string(input_string):
    base64_encoded = base64.urlsafe_b64encode(input_string.encode()).decode()
    return base64_encoded


# Decrypt Strings
def decrypt_string(encrypted_string):
    base64_decoded = base64.urlsafe_b64decode(encrypted_string.encode()).decode()
    return base64_decoded


# Reading files
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


# Comparing files
def compare_files(original_lines, modified_lines):
    diff = difflib.ndiff(original_lines, modified_lines)
    blocks = []
    block = []
    for line in diff:
        if line.startswith('  '):  # common row
            if block:
                blocks.append(block)
                block = []
        else:
            block.append(line)
    if block:
        blocks.append(block)
    return blocks


# Save blocks ro CSV
def save_blocks_to_csv(blocks, output_csv_loc):
    encrypted_blocks = []
    for block in blocks:
        block1 = ''.join([line[2:] for line in block if line.startswith('- ')])
        block2 = ''.join([line[2:] for line in block if line.startswith('+ ')])
        if block1 and block2:
            encrypted_block1 = encrypt_string(block1)
            encrypted_block2 = encrypt_string(block2)
            encrypted_blocks.append((encrypted_block1, encrypted_block2))

    with open(output_csv_loc, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for block1, block2 in encrypted_blocks:
            writer.writerow([block1, block2])


# Decompile blocks from CSV
def load_blocks_from_csv(input_csv):
    blocks = []
    with open(input_csv, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            block1 = decrypt_string(row[0])
            block2 = decrypt_string(row[1])
            blocks.append((block1, block2))
    return blocks


# Apply blocks to file
def apply_blocks_to_file(original_lines, file2_lines, blocks):
    updated_lines = file2_lines[:]
    for block1, block2 in blocks:
        block1_lines = block1.splitlines(keepends=True)
        block2_lines = block2.splitlines(keepends=True)
        for i in range(len(original_lines)):
            if original_lines[i:i + len(block1_lines)] == block1_lines:
                for j in range(len(updated_lines)):
                    if updated_lines[j:j + len(block1_lines)] == block1_lines:
                        updated_lines[j:j + len(block1_lines)] = block2_lines
                        break
                break
    return updated_lines


def download_the_original_file(file_loc):
    if os.path.exists("configs/original"):
        os.remove("configs/original")
    shutil.copy("/lab/epg_scm4_builds/program/ci/" + EPGCATS_VERSION + "/" + file_loc, "configs/original")


def main(original_path_loc, improved_file_loc, repo_file_loc, output_csv_loc):
    original_lines = read_file(original_path_loc)
    file1_lines = read_file(improved_file_loc)
    file2_lines = read_file(repo_file_loc)

    # Differences in the original and the improved file
    blocks = compare_files(original_lines, file1_lines)
    save_blocks_to_csv(blocks, output_csv_loc)

    # Decompiling blocks from CSV
    decrypted_blocks = load_blocks_from_csv(output_csv_loc)

    # Original and improved files comparison
    updated_lines = apply_blocks_to_file(original_lines, file2_lines, decrypted_blocks)

    with open(repo_file_loc, 'w') as file:
        file.writelines(updated_lines)


if __name__ == '__main__':
    download_the_original_file(FILE_TO_IMPROVE)
    original_file = "configs/original"
    repo_file = REPO_FOLDER + FILE_TO_IMPROVE  # This is on repo which should be updated
    improved_file = TARGET_FOLDER + FILE_TO_IMPROVE  # This is the improved file
    output_csv = 'configs/diff.csv'

    main(original_file, improved_file, repo_file, output_csv)

    if len(ADDITIONAL_FILES_TO_COPY) > 0:
        for file in ADDITIONAL_FILES_TO_COPY:
            download_the_original_file(file)
            original_file = "configs/original"
            repo_file = REPO_FOLDER + file  # This is on repo which should be updated
            improved_file = TARGET_FOLDER + file  # This is the improved file
            output_csv = 'configs/diff.csv'
            main(original_file, improved_file, repo_file, output_csv)
