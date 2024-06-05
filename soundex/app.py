# CLI for soundex
import logging
import os
import re

from itertools import groupby
from typing import Generator, Union

# create logger
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class SoundexCode:
    """Soundex code generator"""

    def __init__(self, word: str):
        """Initializes the Soundex code generator with a word
        Note this will not handle non-ascii characters, skipping them instead
        """
        if len(word) == 0:
            # Not actually a word
            return
        self.original_word = word
        self.value = self.code_name(word)

    def __eq__(self, value: object) -> bool:
        """Compare 2 soundex codes"""
        if not isinstance(value, SoundexCode):
            return False
        if not self.value or not value.value:
            return False
        # ignore trailing zeros
        # can use zip since should always be same lenght
        for self_letter, value_letter in zip(self.value, value.value):
            if (
                self_letter != value_letter
                and self_letter != "0"
                and value_letter != "0"
            ):
                return False
        return True

    @staticmethod
    def code_name(word) -> str:
        """Generates the Soundex code for a word"""
        # not the best, since it makes multiple passes
        resulting_value = word[0].upper()
        converted_letters = [SoundexCode.code_letter(letter) for letter in word]
        if "-3" in converted_letters:
            LOGGER.debug("Unsupported character found in the word, skipping it")
            return None
        # strip first letter and following letters have same value
        converted_letters = [k for k, g in groupby(converted_letters)]
        converted_letters.pop(0)
        # strip h, w, y since letters separated by them need to be counted once
        converted_letters = list(
            filter(lambda letter: letter != "-2", converted_letters)
        )
        converted_letters = [k for k, g in groupby(converted_letters)]
        converted_letters = list(
            filter(lambda letter: letter != "-1", converted_letters)
        )

        resulting_value += "".join(converted_letters[:3])
        if (len_value := len(resulting_value)) < 4:
            # pad the code with zeros
            resulting_value += "0" * (4 - len_value)
        return resulting_value

    @staticmethod
    def code_letter(letter: str) -> int:
        """Returns the code for a letter."""
        if len(letter) > 1:
            raise ValueError("Not a  letter")
        letter = letter.upper()
        match letter:
            case "A" | "E" | "I" | "O" | "U":
                # personal abstraction, these will be ignored in the Soundex code
                return "-1"
            case "Y" | "H" | "W":
                # personal abstraction, these will be ignored in the Soundex code
                return "-2"
            case "B" | "F" | "P" | "V":
                return "1"
            case "C" | "G" | "J" | "K" | "Q" | "S" | "X" | "Z":
                return "2"
            case "D" | "T":
                return "3"
            case "L":
                return "4"
            case "M" | "N":
                return "5"
            case "R":
                return "6"
            case _:
                # unsupported character, including non-ascii
                return "-3"


def get_file_path(file_name: str = "test.txt") -> Union[str, None]:
    """Returns the full path of the file if it exists in the input folder"""
    # just checking file extensions, file signature is overkill
    supported_extension = ".txt"
    if not file_name.endswith(supported_extension):
        LOGGER.error(f"Unsupported file '{file_name}', please provide a .txt file")
        return

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = f"{dir_path}/input/{file_name}"

    if not os.path.isfile(file_path):
        LOGGER.error(
            f"File '{file_name}' not found in the input folder, please make sure you copied it"
        )
        return
    return file_path


def read_file(file_path: str) -> Generator:
    """Reads provided file line by line and yields words from it"""
    LOGGER.debug(f"Reading file '{file_name}'")
    with open(file_path, "r") as file:
        for line in file:
            yield line.split()


def run_soundex(target_word: SoundexCode, file_name: str):
    """Runs the soundex code generator"""
    matches = []
    for line in read_file(file_name):
        if not line:
            continue
        # doesn't handle poorly formatted text, for example "word,word2"
        for word in line:
            word = re.sub(r"(^[^\w]+)|([^\w]+$)", "", word)
            soundex_code = SoundexCode(word)
            if soundex_code == target_word:
                matches.append(soundex_code.original_word)
                LOGGER.info(f"Match found: {soundex_code.original_word}")
    return matches


if __name__ == "__main__":
    file_path = None
    target_word = None
    while not file_path:
        file_name = input("Enter the file name: ")
        file_path = get_file_path(file_name)
    while True:
        target_word = input("Enter the word you want to match: ")
        target_word = SoundexCode(target_word)
        if target_word.value:
            break
        LOGGER.warning(
            "Unsupported character found in the word, please use ascii letters only"
        )
    matches = run_soundex(target_word, file_path)
