from pprint import pprint
from utils import check_file_exists, track_lost_files
from read_write import read_line, add_to_file, log_lost_records

USERS_FILE = "users.txt"


def create_gender_data(idx: int, record: str, lost_files_dict: dict, occurred_genders: set) -> tuple[dict, set]:
    """
    This function gets record from users file, processes it to put into gender files
    It tracks presence and losses of gender files
    :param idx: Index of a record
    :param record: Record about user from users file
    :param lost_files_dict: Dictionary where keys are lost filenames and values are record indexes in users file
    :param occurred_genders: Set of already processed genders
    :return: Dictionary of lost files and set of processed genders
    """

    # Splits a record to values, error occurrences are handled by the main function
    try:
        name, age, gender = record.split(",")
    except ValueError:
        raise

    gender = gender.strip()

    filename = f"./genders/{gender}.txt"

    if gender in occurred_genders:  # In case gender is already occurred, checks presence of a gender file

        if not check_file_exists(filename):
            # Updates dictionary is there is no gender file
            lost_files_dict = track_lost_files(lost_files_dict, idx, filename)

        add_to_file(filename, name, age, gender, "a")

    else:  # In case of the first occurrence of certain gender, stores it into the set and creates new gender file
        add_to_file(filename, name, age, gender, "w")
        occurred_genders.add(gender)

    return lost_files_dict, occurred_genders


def main():

    # Initializes the dictionary in which we track file losses
    lost_files_dict = {}

    # Initializes the set in which we add genders at their first occurrences
    occurred_genders = set()

    # Get records from users file
    for idx, record in read_line(USERS_FILE):
        try:
            # We pass the dictionary and the set to the function and get updated ones
            lost_files_dict, occurred_genders = create_gender_data(idx, record, lost_files_dict, occurred_genders)
        except ValueError:  # Error may raise into the "create_gender_data" function and handled here
            print(f"Cannot process line {idx} in users.txt")

    pprint(lost_files_dict)


if __name__ == '__main__':
    main()
