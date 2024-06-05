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
        # characters and non-ascii characters are not supported
        ("-", "-3"),
        ("č", "-3"),
    ],
)
def test_letter_conversion(input_letter, expected_result):
    """Verify that the individual letter conversion works as expected."""
    assert SoundexCode.code_letter(input_letter) == expected_result


@pytest.mark.parametrize(
    "input_word, expected_result",
    [
        ("Robert", "R163"),
        ("Rupert", "R163"),
        ("Rubin", "R150"),
        ("Ashcraft", "A261"),
        ("Ashcroft", "A261"),
        ("Tymczak", "T522"),
        ("Pfister", "P236"),
        ("Honeyman", "H555"),
        # characters and non-ascii characters are not supported
        ("Emily-Rose", None),
        ("Acemoğlu", None),
    ],
)
def test_full_conversion(input_word, expected_result):
    """Verify that the full conversion works as expected."""
    assert SoundexCode(input_word).value == expected_result


@pytest.mark.parametrize(
    "source, target, expected_result",
    [
        ("Robert", "Rupert", True),  # R163
        ("Robert", "Rubin", False),  # R163 and R150
        # trailing zeros
        ("Lithuania", "Lithuanian", True),  # L350 and L355
        ("Lithuanian", "Lithuania", True),  # L355 and L350
        # None Values
        ("Robert", "Emily-Rose", False),
        ("Acemoğlu", "Rupert", False),
        ("Acemoğlu", "Emily-Rose", False),
    ],
)
def test_equals(source, target, expected_result):
    """Verify that the __eq__ method works as expected."""
    assert (SoundexCode(source) == SoundexCode(target)) is expected_result
