import numpy as np

from print_dict.print_dict import format_dict


def test_print_dict_format_1():

    dict_1 = {
        'one': 'long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long'
    }

    result = format_dict(dict_1)

    expected = """\
{
    'one': 'long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long-long'
}\
"""

    assert result == expected


def test_print_dict_format_2():

    dict_1 = {
        'one': 'one-value'
    }

    result = format_dict(dict_1)

    expected = """\
{
    'one': 'one-value'
}\
"""

    assert result == expected

    # --------------------

    dict_2 = {
        'one': 'one-value',
        'two': 'two-value',
        'three': 'three-value',
        'four': 'four-value',
        'five': 'five-value',
    }

    expected = """\
{
    'one': 'one-value',
    'two': 'two-value',
    'three': 'three-value',
    'four': 'four-value',
    'five': 'five-value'
}\
"""

    result = format_dict(dict_2)

    assert result == expected

    # --------------------

    dict_3 = {
        'one': 'one-value',
        'two': 'two-value',
        'three': 'three-value',
        'four': CustomClass(),
        'five': custom_method,
        'six': CustomClass2(),
    }

    # Expected
    """
    {
        'one': 'one-value',
        'two': 'two-value',
        'three': 'three-value',
        'four': <tests.test_print_dict.CustomClass object at 0x7f5c335cd6d8>,
        'five': <function custom_method at 0x7f5c33231840>,
        'six': CustomClass2 ` " some_sting
    }
    """

    result = format_dict(dict_3)

    lines = result.split('\n')
    assert '<tests.test_print_dict.CustomClass object at 0x' in lines[4]
    assert '<function custom_method at 0x' in lines[5]
    assert """CustomClass2 ` " some_sting""" in lines[6]


def test_key_and_value_are_objects():

    dict_1 = {
        np.int32(0): np.int32(1)
    }

    result = format_dict(dict_1)

    expected = """\
{
    0: 1
}\
"""

    assert result == expected


def test_sorting():

    dict_1 = {
        'ggg': 'ggg-value',
        'bbb': 'bbb-value',
        'aaa': {
            'eee': 'eee-value',
            'ddd': 'ddd-value',
        },
    }

    result = format_dict(dict_1, sort_keys=True)

    expected = """\
{
    'aaa': {
        'ddd': 'ddd-value',
        'eee': 'eee-value'
    },
    'bbb': 'bbb-value',
    'ggg': 'ggg-value'
}\
"""

    assert result == expected


class CustomClass:
    pass


class CustomClass2:
    def __repr__(self):
        return """CustomClass2 ` " some_sting"""


def custom_method():
    pass

