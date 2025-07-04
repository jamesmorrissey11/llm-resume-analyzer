import re

from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer


def print_colored_pii(string):
    colored_string = re.sub(r"(<[^>]*>)", lambda m: "\033[31m" + m.group(1) + "\033[0m", string)
    print(colored_string)


def anonymmize_text(text):
    anonymizer = PresidioReversibleAnonymizer(
        add_default_faker_operators=False,
    )
    return anonymizer.anonymize(text)
