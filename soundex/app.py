# CLI for soundex
import logging
import os

from typing import Union

# create logger
LOGGER = logging.getLogger(__name__)


def read_file(file_name: str = "test.txt") -> Union[str, None]:
    """Reads the file names from the input folder"""
    # just checking file extensions, file signature is overkill
    supported_extension = ".txt"
    if not file_name.endswith(supported_extension):
        logging.info(f"Unsupported file '{file_name}', please provide a .txt file")
        return

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = f"{dir_path}/{file_name}"

    if not os.path.isfile(file_path):
        logging.info(
            f"File '{file_name}' not found in the input folder, please make sure you copied it"
        )
        return

    logging.info(f"Reading file '{file_name}'")
    with open(file_path, "r") as file:
        return file.read()


if __name__ == "__main__":
    read_file()
    print("Hello, World!")
