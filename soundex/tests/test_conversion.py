# Tests conversion of string to soundex code
import pytest

from soundex.app import SoundexCode


@pytest.mark.parametrize(
    "input_letter, expected_result",
    [
        ("a", "-1"),
        ("e", "-1"),
        ("i", "-1"),
        ("o", "-1"),
        ("u", "-1"),
        ("y", "-2"),
        ("h", "-2"),
        ("w", "-2"),
        ("b", "1"),
        ("f", "1"),
        ("p", "1"),
        ("v", "1"),
        ("c", "2"),
        ("g", "2"),
        ("j", "2"),
        ("k", "2"),
        ("q", "2"),
        ("s", "2"),
        ("x", "2"),
        ("z", "2"),
        ("d", "3"),
        ("t", "3"),
        ("l", "4"),
        ("m", "5"),
        ("n", "5"),
        ("r", "6"),
        ("-", "-3"),
        ("č", "-3"),
    ],
)
def test_letter_conversion(input_letter, expected_result):
    assert SoundexCode.code_letter(input_letter) == expected_result
