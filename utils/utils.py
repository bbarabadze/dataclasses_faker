import os


def check_file_exists(filename: str) -> bool:
    """
    Checks file existence
    :param filename: Name of file
    :return: Truth value of file existence
    """

    return os.path.exists(filename)


def track_lost_files(lost_files: dict, lost_record_idx: int, lost_filename: str) -> dict:
    """
    Adds name of a lost gender file as a key and lost record index as a value to the lost_files dictionary
    :param lost_files: Dictionary where keys are lost filenames and values are record indexes in users.txt
    :param lost_record_idx: Index of the record in users.txt, indicating moment of loss detection of a gender file
    :param lost_filename: Gender file, which get lost during runtime
    :return: Updated dictionary of lost files
    """

    lost_files[lost_filename] = lost_files.get(lost_filename, [])
    lost_files[lost_filename].append(lost_record_idx)

    return lost_files
