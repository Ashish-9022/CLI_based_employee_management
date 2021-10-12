import logging

logging.basicConfig(filename='error.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def check_string_set_none(value):
    if value == "":
        return None
    else:
        return value


def convert_to_int(value):
    if value == "":
        return None
    else:
        try:
            return int(value)
        except ValueError:
            logging.critical('invalid literal for int() with base 10')


def create_list(value):
    if value == "":
        return []
    else:
        try:
            return value.split(",")
        except AttributeError:
            logging.critical('int object has no attribute split')

