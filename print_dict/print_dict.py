
import re
import os
import tempfile

from .config import UNIQUE_TOKEN
from .pprint_python_3_9 import PrettyPrinter
from yapf.yapflib.yapf_api import FormatCode


def print_dict(arg):
    print(format_dict(arg))


def pd(arg):
    print_dict(arg)


def format_dict(arg):

    pretty_printer = PrettyPrinter(
        indent=1, width=200, depth=None,
        compact=False, sort_dicts=False
    )

    formatted_dict_step_1 = pretty_printer.pformat(arg)

    style_file_text = """\
[style]
COLUMN_LIMIT: 96
EACH_DICT_ENTRY_ON_SEPARATE_LINE: true
FORCE_MULTILINE_DICT: true
INDENT_DICTIONARY_VALUE: false
ALLOW_SPLIT_BEFORE_DICT_VALUE: false
"""

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    try:
        temp_file.write(style_file_text.encode("utf-8"))
        temp_file.seek(0)
        formatted_dict_step_3, _ = FormatCode(formatted_dict_step_1, style_config=temp_file.name)
    finally:
        temp_file.close()
        os.unlink(temp_file.name)

    formatted_dict_step_4 = formatted_dict_step_3.strip()

    formatted_dict_step_5 = re.sub(f"'{UNIQUE_TOKEN}(.*)'", "\\1", formatted_dict_step_4)
    formatted_dict = formatted_dict_step_5.replace("\\'", "'")

    return formatted_dict
