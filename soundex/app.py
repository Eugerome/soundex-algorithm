# CLI for soundex
import logging
import os

from typing import List


# create logger
LOGGER = logging.getLogger(__name__)

# default values
INPUT_FOLDER = "input"


def read_file_names(input_folder: str = INPUT_FOLDER) -> list:
    """Reads the file names from the input folder"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        file_names = os.listdir(f"{dir_path}/{input_folder}")
    except FileNotFoundError as e:
        logging.error(f"Folder '{input_folder}' not found: {e}")
        return
    return file_names


def clean_file_names(file_names: List[str]) -> List[str]:
    """Cleans the file names and returns a list os supported files"""
    # just checking file extensions, file signature is overkill
    supported_extensions = ".txt"
    cleaned_files = [
        file_name
        for file_name in file_names
        if file_name.endswith(supported_extensions)
    ]
    if (raw_len := len(file_names)) != (clean_len := len(cleaned_files)):
        logging.info(
            f"Found {raw_len - clean_len} unsupported files in the input folder, they will be skipped"
        )
    if clean_len == 0:
        logging.info("No supported files found in the input folder, exiting...")
    return cleaned_files


if __name__ == "__main__":
    clean_file_names(read_file_names())
    print("Hello, World!")
