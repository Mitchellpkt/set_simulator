import pytest
from set_simulator.main import (
    generate_deck,
    is_valid_set,
    standard_canonical_order,
    count_valid_sets,
)


def test_order():
    assert standard_canonical_order == ("number", "color", "shading", "shape")


def test_deck_generation_unshuffled():
    test_deck = generate_deck(shuffle=False)
    assert test_deck[:3] == [
        (1, "red", "open", "diamond"),
        (1, "red", "open", "squiggle"),
        (1, "red", "open", "oval"),
    ]


def test_deck_generation_shuffled():
    test_deck = generate_deck(shuffle=True, seed=12345678)
    assert test_deck[:3] == [
        (2, "red", "striped", "diamond"),
        (1, "red", "open", "diamond"),
        (2, "purple", "solid", "diamond"),
    ]


def test_is_set_ok():
    assert is_valid_set(
        [
            (2, "green", "striped", "diamond"),
            (1, "red", "open", "diamond"),
            (3, "purple", "solid", "diamond"),
        ]
    )


def test_is_set_bad():
    assert not is_valid_set(
        [
            (2, "green", "striped", "oval"),
            (1, "red", "open", "diamond"),
            (3, "purple", "solid", "diamond"),
        ]
    )


def test_count_valid_sets():
    expected: int = 6
    observed: int = count_valid_sets(
        [
            (2, "green", "striped", "diamond"),
            (1, "red", "open", "diamond"),
            (3, "purple", "solid", "diamond"),
            (1, "purple", "open", "diamond"),
        ],
        verbose=True,
    )
    assert expected == observed


def test_count_valid_sets_with_none():
    expected: int = 0
    observed: int = count_valid_sets(
        [
            (2, "green", "striped", "diamond"),
            (1, "red", "open", "diamond"),
            (2, "purple", "solid", "diamond"),
            (1, "purple", "open", "diamond"),
        ],
        verbose=True,
    )
    assert expected == observed
