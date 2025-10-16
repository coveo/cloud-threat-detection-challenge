import os
from pathlib import Path
from typing import Iterator, Union


def read_log_files(input_path: Union[str, Path]) -> Iterator[str]:
    """
    Iterator-based function that reads log files line by line.

    Handles both single file and directory input paths.
    Yields raw log lines as strings without any parsing or processing.

    Args:
        input_path: Path to a single log file or directory containing log files

    Yields:
        str: Raw log lines from the input files
    """
    input_str = str(input_path)
    if os.path.isfile(input_str):
        # Handle single file input
        yield from _read_single_file(input_str)
    elif os.path.isdir(input_str):
        # Handle directory input - read all files in directory
        for filename in os.listdir(input_str):
            file_path = os.path.join(input_str, filename)
            if os.path.isfile(file_path):
                yield from _read_single_file(file_path)
    else:
        raise FileNotFoundError(f"Input path does not exist: {input_str}")


def _read_single_file(file_path: str) -> Iterator[str]:
    """
    Read a single file line by line.

    Args:
        file_path: Path to the file to read

    Yields:
        str: Raw lines from the file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Yield raw line without any processing or parsing
                yield line.rstrip("\n\r")
    except (IOError, OSError) as e:
        print(f"Warning: Could not read file {file_path}: {e}")
        return
