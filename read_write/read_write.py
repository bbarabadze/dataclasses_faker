LOST_RECORDS = "./lost_records.txt"


def read_line(filename: str):
    """
    Generator, which reads file and yields each line per iteration
    :param filename: Name of file to be read
    :return: Generator object
    """
    with open(filename, "r") as f:
        for idx, record in enumerate(f):

            yield idx, record


def add_to_file(filename: str, name: str, age: str, gender: str, flag: str) -> None:
    """
    This function creates or appends into a gender file, depending on a flag value
    :param filename: Name of file
    :param name: Name of user
    :param age: Age of user
    :param gender: Gender of user
    :param flag: Writing mode
    :return: None
    """
    try:
        with open(filename, flag) as f:
            f.write(f"{name},{age}\n")
    except Exception as ex:
        print(f"Unable to open {filename} for {flag}, {str(ex)}")
        log_lost_records(name, age, gender)


def log_lost_records(name: str, age: str, gender: str) -> None:
    """
    This function logs lost records from gender files
    :param name: Name of user
    :param age: Age of user
    :param gender: Gender of user
    :return: None
    """
    with open(LOST_RECORDS, "a") as f:
        f.write(f"{name},{age},{gender}\n")
