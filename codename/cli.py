#!/usr/bin/env python3
"""
codename: generate random codenames from system dictionary words.

Usage:
  codename [-n NUM] [-d DELIM]
  codename (-h | --help)
  codename --version

Options:
  -n NUM --num NUM              Number of words to join [default: 2]
  -d DELIM --delimiter DELIM    Delimiter to use between words [default: -]
  -h --help                     Show this help message.
  --version                     Show version.

"""
import random
import sys
from pathlib import Path
from typing import List, Set

from docopt import docopt

from codename import __version__

# Constants
VALID_DELIMITERS: Set[str] = {"-", ",", "_", "|", ";", ":"}
DICTIONARY_PATH: str = "/usr/share/dict/words"

def load_words(filepath: str) -> List[str]:
    """Load words from the system dictionary file.
    
    Args:
        filepath: Path to the dictionary file
        
    Returns:
        List of valid words (lowercase, alphabetic, 3+ characters)
        
    Raises:
        FileNotFoundError: If dictionary file doesn't exist
        IOError: If there are issues reading the file
    """
    try:
        with open(filepath, 'r') as f:
            words = [
                line.strip().lower()
                for line in f
                if len(line.strip()) >= 3 and line.strip().isalpha()
            ]
        if not words:
            print(f"Error: No valid words found in dictionary at {filepath}", file=sys.stderr)
            sys.exit(1)
        return words
    except FileNotFoundError:
        print(f"Error: Dictionary file not found at {filepath}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading dictionary file: {e}", file=sys.stderr)
        sys.exit(1)

def generate_codename(words: List[str], num_words: int = 2, delimiter: str = '-') -> str:
    """Generate a random codename by joining words with a delimiter.
    
    Args:
        words: List of valid words to choose from
        num_words: Number of words to join [default: 2]
        delimiter: Character to join words with [default: -]
        
    Returns:
        A string containing the generated codename
    """
    return delimiter.join(random.choice(words) for _ in range(num_words))

def main() -> None:
    """Main entry point for the CLI tool."""
    args = docopt(__doc__, version=f"codename {__version__}")

    try:
        num_words = int(args['--num'])
        if num_words < 1:
            print("Error: Number of words must be at least 1", file=sys.stderr)
            sys.exit(1)
    except ValueError:
        print("Error: Number of words must be an integer", file=sys.stderr)
        sys.exit(1)

    delimiter = args['--delimiter']
    if delimiter not in VALID_DELIMITERS:
        print(
            f"Error: Invalid delimiter '{delimiter}'. Must be one of {''.join(VALID_DELIMITERS)}", 
            file=sys.stderr
        )
        sys.exit(1)

    words = load_words(DICTIONARY_PATH)
    codename = generate_codename(words, num_words=num_words, delimiter=delimiter)
    print(codename)

if __name__ == "__main__":
    main()
