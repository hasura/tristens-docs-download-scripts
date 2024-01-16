import os

root = "files/ndc-sdk-typescript"

import os
import json


def read_files_to_json(directory, output_file):
    """
    Walks through the given directory, reads each file, and writes the contents
    into a JSON file.

    :param directory: The directory to walk through.
    :param output_file: The path of the JSON file to write the data to.
    """
    file_contents = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if "/.git/" in file_path:
                continue
            elif file_path.endswith("LICENSE"):
                continue
            elif file_path.endswith("package-lock.json"):
                continue
            try:
                with open(file_path, 'r') as f:
                    file_contents[file_path] = f.read()
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(file_contents, json_file, indent=4, ensure_ascii=False)


# Example usage
directory_to_walk = 'files/ndc-turso-python'  # Replace with your directory path
output_json_file = 'files/ndc-turso-python/ndc-turso-python.json'  # Replace with your desired output file path

read_files_to_json(directory_to_walk, output_json_file)
