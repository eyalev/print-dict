from print_dict import print_dict


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

print_dict(data)

