
import re
from pathlib import Path

from .config import UNIQUE_TOKEN
from .pprint_python_3_9 import PrettyPrinter
from yapf.yapflib.yapf_api import FormatCode


def print_dict(arg):
    print(format_dict(arg))


def format_dict(arg):

    pretty_printer = PrettyPrinter(
        indent=1, width=200, depth=None,
        compact=False, sort_dicts=False
    )

    formatted_dict_step_1 = pretty_printer.pformat(arg)

    # formatted_dict_step_2 = re.sub('(<.* 0x.*>)', "'\\1'", formatted_dict_step_1)

    style_file_text = """\
[style]
COLUMN_LIMIT: 96
"""

    temp_style_file_path = f'/tmp/{UNIQUE_TOKEN}-style'
    Path(temp_style_file_path).write_text(style_file_text)

    formatted_dict_step_3, _ = FormatCode(formatted_dict_step_1, style_config=temp_style_file_path)
    formatted_dict_step_4 = formatted_dict_step_3.strip()

    # formatted_dict = re.sub("'(<.*0x.*>)'", "\\1", formatted_dict_step_4)

    formatted_dict_step_5 = re.sub(f"'{UNIQUE_TOKEN}(.*)'", "\\1", formatted_dict_step_4)
    formatted_dict = formatted_dict_step_5.replace("\\'", "'")

    return formatted_dict
