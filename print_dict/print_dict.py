
import re
from .pprint_python_3_9 import PrettyPrinter
from yapf.yapflib.yapf_api import FormatCode


def print_dict(arg):
    print(format_dict(arg))


def format_dict(arg):

    pretty_printer = PrettyPrinter(
        indent=1, width=80, depth=None,
        compact=False, sort_dicts=False
    )

    formatted_dict_step_1 = pretty_printer.pformat(arg)

    formatted_dict_step_2 = re.sub('(<.* 0x.*>)', "'\\1'", formatted_dict_step_1)

    formatted_dict_step_3, _ = FormatCode(formatted_dict_step_2)
    formatted_dict_step_4 = formatted_dict_step_3.strip()

    formatted_dict = re.sub("'(<.*0x.*>)'", "\\1", formatted_dict_step_4)

    return formatted_dict
