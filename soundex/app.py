# CLI for soundex
import logging
import os

from itertools import groupby
from typing import Union, List

# create logger
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

    @staticmethod
    def code_name(word) -> str:
        """Generates the Soundex code for a word"""
        # not the best, since it makes multiple passes
        resulting_value = word[0].upper()
        try:
            converted_letters = [SoundexCode.code_letter(letter) for letter in word]
        except ValueError as e:
            # contains odd symbols, ignore
            resulting_value = None
            LOGGER.debug(f"Found word with strange symbol, skipping: {e}")
            return
        # strip first letter and following letters have same value
        converted_letters = [k for k, g in groupby(converted_letters)]
        converted_letters.pop(0)
        # strip h, w, y since letters separated by them need to be counted once
        converted_letters = list(filter(lambda letter: letter != "-2", converted_letters))
        converted_letters = [k for k, g in groupby(converted_letters)]
        converted_letters = list(filter(lambda letter: letter != "-1", converted_letters))

        resulting_value += "".join(converted_letters[:3])
        if len_value := len(resulting_value) < 4:
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
                # ignore words with strange symbols and non ascii characters
                raise ValueError(f"Unsupported character '{letter}'")

    @staticmethod
    def remove_adjacent(num_list: List[int]):
        """Remove adjacent numbers that have same value"""
        i = 1
        while i < len(num_list):
            if num_list[i] == num_list[i - 1]:
                num_list.pop(i)
                i -= 1
            i += 1
        return num_list


def read_file(file_name: str = "test.txt") -> Union[str, None]:
    """Reads the file names from the input folder"""
    # just checking file extensions, file signature is overkill
    supported_extension = ".txt"
    if not file_name.endswith(supported_extension):
        logging.info(f"Unsupported file '{file_name}', please provide a .txt file")
        return

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = f"{dir_path}/input/{file_name}"

    if not os.path.isfile(file_path):
        logging.info(
            f"File '{file_name}' not found in the input folder, please make sure you copied it"
        )
        return

    logging.info(f"Reading file '{file_name}'")
    with open(file_path, "r") as file:
        return file.read()


if __name__ == "__main__":
    a = SoundexCode("Ddimadubizumi")
    print("Hello, World!")
