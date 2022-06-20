import logging

log = logging.getLogger(__name__)


def to_category(string, categories):
    """
    Matches a string to a category based on categories given in a config file
    the config file should contain a dictionary for each category for this function to loop through
    return blank if no categories found
    """
    for code in categories:
        if str(string).lower() == str(code["code"]).lower():
            return code["code"]
        elif "name" in code:
            if str(code["name"]).lower() in str(string).lower():
                return code["code"]
            else:
                return "error"
        elif not string:
            return ""
        else:
            return "error"


def to_integer(string, config):
    """
    Convert any strings that should be integers based on the config into integers
    """
    if config == "integer":
        if string:
            return int(string)
        else:
            return ""
    else:
        return string

