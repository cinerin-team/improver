import csv
import difflib
import os.path

from cryptography.fernet import Fernet
import base64


# Kulcs betöltése
def load_key():
    if not os.path.exists("configs/secret.key"):
        key = Fernet.generate_key()
        with open("configs/secret.key", "wb") as key_file:
            key_file.write(key)
    return open("configs/secret.key", "rb").read()


# String titkosítása
def encrypt_string(input_string, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(input_string.encode())

    # Base64 URL-safe kódolás az eredmény string-gé alakításához
    base64_encoded = base64.urlsafe_b64encode(encrypted).decode()

    return base64_encoded


# String visszafejtése
def decrypt_string(encrypted_string, key):
    fernet = Fernet(key)

    # Base64 URL-safe dekódolás
    base64_decoded = base64.urlsafe_b64decode(encrypted_string.encode())
    decrypted = fernet.decrypt(base64_decoded).decode()

    return decrypted


# Fájlok beolvasása
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


# Blokkok összehasonlítása és titkosítása
def compare_and_encrypt(file1_lines, file2_lines, key):
    diff = difflib.ndiff(file1_lines, file2_lines)
    blocks = []
    block1, block2 = [], []
    for line in diff:
        if line.startswith('  '):  # Közös sor
            if block1 or block2:
                blocks.append((block1, block2))
                block1, block2 = [], []
        elif line.startswith('- '):  # Csak az első fájlban van
            block1.append(line[2:])
        elif line.startswith('+ '):  # Csak a második fájlban van
            block2.append(line[2:])

    # Az utolsó blokk hozzáadása
    if block1 or block2:
        blocks.append((block1, block2))

    encrypted_blocks = []
    for block1, block2 in blocks:
        encrypted_block1 = encrypt_string(''.join(block1), key)
        encrypted_block2 = encrypt_string(''.join(block2), key)
        encrypted_blocks.append((encrypted_block1, encrypted_block2))

    return encrypted_blocks


# Blokkok mentése CSV-be
def save_blocks_to_csv(blocks, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for block1, block2 in blocks:
            writer.writerow([block1, block2])


# CSV-ből blokkok visszafejtése
def load_blocks_from_csv(input_csv, key):
    blocks = []
    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            block1 = decrypt_string(row[0], key)
            block2 = decrypt_string(row[1], key)
            blocks.append((block1, block2))
    return blocks


# Fájl frissítése blokkok alapján
def update_file(file_lines, blocks):
    updated_lines = file_lines[:]
    diff = difflib.ndiff(updated_lines, updated_lines)  # Ez csak egy placeholder

    block_idx = 0
    for line in diff:
        if block_idx >= len(blocks):
            break
        if line.startswith('- '):  # Csak az első fájlban van
            block1, block2 = blocks[block_idx]
            updated_lines = updated_lines.replace(block1, block2)
            block_idx += 1

    return updated_lines


# Fő funkció
def main(file1_path, file2_path, output_csv):
    key = load_key()
    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)

    encrypted_blocks = compare_and_encrypt(file1_lines, file2_lines, key)
    save_blocks_to_csv(encrypted_blocks, output_csv)

    # Az egyik fájl frissítése a CSV alapján
    blocks = load_blocks_from_csv(output_csv, key)
    updated_lines = update_file(file1_lines, blocks)

    with open(file1_path, 'w') as file:
        file.writelines(updated_lines)


if __name__ == '__main__':

    # Futtatás példa
    file1_path = 'improved.txt'
    file2_path = 'repo.txt'
    output_csv = 'configs/diff.csv'
    main(file1_path, file2_path, output_csv)
