
# print-dict

## Motivation

Apparently, pretty-printing nested python dictionaries with values such as classes and functions (where you can't use `json.dumps`) is
not as straightforward as you would think.

See: https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries

This library tries to make it a little bit easier.

## Install

```
$ pip install -U print-dict
```

## Usage

```python
from print_dict import pd
pd({'key': 'value'})

# Or

from print_dict import print_dict
print_dict({'key': 'value'})


# Get the string without printing
from print_dict import format_dict
string = format_dict({'key': 'value'})

```

## Example 1

Code:

```python
from print_dict import pd

dict1 = {
    'key': 'value'
}

pd(dict1)
```

Output:

```
{
    'key': 'value'
}
```

## Example 2

Code:

```python
from print_dict import pd


class Object1:
    pass


class Object2:

    def __repr__(self):
        return "<Object2 info>"


def custom_method():
    pass


object1 = Object1()

data = {
    "one": "value-one",
    "two": "value-two",
    "three": "value-three",
    "four": {
        '1': '1', '2': '2', '3': [1, 2, 3, 4, 5], '4': {
            'method': custom_method,
            'tuple': (1, 2),
            'unicode': u'\u2713',
            'ten': 'value-ten',
            'eleven': 'value-eleven',
            '3': [1, 2, 3, 4]
        }
    },
    "object1": object1,
    "object2": Object2(),
    "class": Object1

}

pd(data)

```

Output:

```

{
    'one': 'value-one',
    'two': 'value-two',
    'three': 'value-three',
    'four': {
        '1': '1',
        '2': '2',
        '3': [1, 2, 3, 4, 5],
        '4': {
            'method': <function custom_method at 0x7ff6ecd03e18>,
            'tuple': (1, 2),
            'unicode': '✓',
            'ten': 'value-ten',
            'eleven': 'value-eleven',
            '3': [1, 2, 3, 4]
        }
    },
    'object1': <__main__.Object1 object at 0x7ff6ecc588d0>,
    'object2': <Object2 info>,
    'class': <class '__main__.Object1'>
}


```

