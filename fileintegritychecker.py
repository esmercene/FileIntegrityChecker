import os
import hashlib


def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()


def check_integrity(directory_path, checksum_value):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist!")
        return

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            print(f"File: {file_path}\nSHA-256 Hash: {calculated_hash}")
            if calculated_hash == checksum_value:
                print("Integrity Check: Matched (Checksum Verified)")
            else:
                print("Integrity Check: Not Matched (Checksum Verification Failed)")


if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check file integrity: ")
    checksum_value = input("Enter the SHA-256 checksum value to compare: ")
    check_integrity(directory_to_check, checksum_value)
