from print_dict.print_dict import format_dict


def test_print_dict_format():

    dict_1 = {
        'one': 'one-value'
    }

    result = format_dict(dict_1)

    assert result == "{'one': 'one-value'}"

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
        'six': CustomClass2 ' ` " some_sting
    }
    """

    result = format_dict(dict_3)

    lines = result.split('\n')
    assert '<tests.test_print_dict.CustomClass object at 0x' in lines[4]
    assert '<function custom_method at 0x' in lines[5]
    assert """CustomClass2 ' ` " some_sting""" in lines[6]


class CustomClass:
    pass


class CustomClass2:
    def __repr__(self):
        return """CustomClass2 ' ` " some_sting"""


def custom_method():
    pass

