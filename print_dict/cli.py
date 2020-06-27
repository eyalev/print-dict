
import click
from print_dict import print_dict


@click.command()
@click.argument('arg')
def cli(arg):

    if arg == 'example1':

        object1 = CustomClass()

        data = {
            "one": "value-one",
            "two": "value-two",
            "three": "value-three",
            "four": {
                '1': '1', '2': '2', '3': [1, 2, 3, 4, 5], '4': {
                    'one': custom_method,
                    'tuple': (1, 2),
                    'unicode': u'\xa7',
                    'two': 'two-value',
                    'three': 'three-value',
                    '3': [1, 2, 3, 4]
                }
            },
            "five": object1,
            "six": CustomClass2()

        }

    else:
        raise NotImplementedError

    print_dict(data)


class CustomClass:
    pass


class CustomClass2:

    def __repr__(self):
        return """<CustomClass2 'aaa>"""


def custom_method():
    pass
