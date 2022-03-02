#!/usr/bin/env python3
"""crowsnet module."""

import argparse
import sys
from typing import Any, Literal

SIDES = ("larboard", "starboard")


def get_args(args: list[Any] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "str",
        help="A word",
    )
    parser.add_argument(
        "-s",
        "--side",
        choices=SIDES,
        default="larboard",
        help="Select side.",
    )

    return parser.parse_args(args)


def get_article(word: str) -> Literal["a", "an", "A", "An"]:
    """Return article 'an' if word begins with a vowel, otherwise return 'a'.

    >>> get_article("consonants")
    'a'
    >>> get_article("apple")
    'an'
    >>> get_article("Consonants")
    'A'
    >>> get_article("Apple")
    'An'
    >>> word="example"
    >>> f"This is {get_article(word)} {word}."
    'This is an example.'
    """
    article = "an" if word.casefold().startswith(("a", "e", "i", "o", "u")) else "a"
    return article if word.islower() else article.title()


def is_word_ok(word: str) -> bool:
    """Raise exception if word is invalid.

    >>> is_word_ok("Yes")
    True
    >>> is_word_ok("!nope")
    Traceback (most recent call last):
    ValueError: '!nope' does not start with an alphabetic character.
    """
    if not word[0].isalpha():
        sys.tracebacklimit = 0
        raise ValueError(f"'{word}' does not start with an alphabetic character.")
    return True


def get_message(word: str, side: str) -> str:
    """Get message.

    >>> get_message("unicorn", "larboard")
    'Ahoy, Captain, an unicorn off the larboard bow!'
    >>> get_message("Shamu", "starboard")
    'Ahoy, Captain, A Shamu off the starboard bow!'
    """
    return f"Ahoy, Captain, {get_article(word)} {word} off the {side} bow!"


def main():
    """Run main logic."""
    args = get_args()
    is_word_ok(args.str)
    print(get_message(args.str, args.side))


if __name__ == "__main__":
    main()
