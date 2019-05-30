import sys

import owattr

import pytest


__all__ = ["NAME", "NUMBER", "test_class", "test_module"]

NAME = "tests.py"
NUMBER = 0


def test_class():
    class TargetObject:
        name = "A"
        number = 1
        is_foo = True
        is_bar = True
        is_baz = False

    target_object = TargetObject()

    owattr.from_dict(target_object, {
        'name': "B",
        "number": "2",
        "is_foo": "false",
        "is_bar": "False",
        "is_baz": "true",
    })

    assert target_object.name == "B"
    assert target_object.number == 2
    assert target_object.is_foo is False
    assert target_object.is_bar is False
    assert target_object.is_baz is True


def test_class_invalid_bool():
    class TargetObject:
        is_a_bool = True

    target_object = TargetObject()

    with pytest.raises(ValueError):
        owattr.from_dict(target_object, {
            'is_a_bool': 'no_it_is_not',
        })


def test_module():
    module = sys.modules[__name__]

    owattr.from_dict(module, {
        'NAME': "owattr test",
        'NUMBER': 1,
    })

    assert module.NAME == "owattr test"
    assert module.NUMBER == 1
