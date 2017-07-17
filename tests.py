import sys

import owattr


__all__ = ["NAME", "NUMBER", "test_class", "test_module"]

NAME = "tests.py"
NUMBER = 0


def test_class():
    class TargetObject:
        name = "A"
        number = 1

    target_object = TargetObject()

    owattr.from_dict(target_object, {
        'name': "B",
        "number": "2",
    })

    assert target_object.name == "B"
    assert target_object.number == 2


def test_module():
    module = sys.modules[__name__]

    owattr.from_dict(module, {
        'NAME': "owattr test",
        'NUMBER': 1,
    })

    assert module.NAME == "owattr test"
    assert module.NUMBER == 1
