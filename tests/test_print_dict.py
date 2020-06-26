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
    }

    expected = """\
{
    'one': 'one-value',
    'two': 'two-value',
    'three': 'three-value',
    'four': <tests.test_print_dict.CustomClass object at 0x7f5c335cd6d8>,
    'five': <function custom_method at 0x7f5c33231840>
}\
"""

    result = format_dict(dict_3)

    print(result)

    # assert result == expected
    lines = expected.split('\n')
    # import pdb; pdb.set_trace()
    assert '<tests.test_print_dict.CustomClass object at 0x' in lines[4]
    assert '<function custom_method at 0x' in lines[5]


class CustomClass:
    pass


def custom_method():
    pass

