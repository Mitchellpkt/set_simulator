from typing import Dict, Any, List, Tuple, Union
from itertools import product, permutations
import random

# Define features of the deck, supports arbitrary number of dimensions and traits
standard_feature_possibilities: Dict[str, Tuple[Any, ...]] = {
    "number": (1, 2, 3),
    "color": ("red", "green", "purple"),
    "shading": ("open", "striped", "solid"),
    "shape": ("diamond", "squiggle", "oval"),
}

# Optionally define an order, this is cosmetic only. If you don't care, you can set to None for automatic ordering
standard_canonical_order: Tuple[str, str, str, str] = (
    "number",
    "color",
    "shading",
    "shape",
)


def generate_deck(
    feature_possibilities: Dict[str, Tuple[Any, ...]] = None,
    canonical_order: Union[None, Tuple[str, ...]] = None,
    shuffle: bool = True,
    seed: int = 42,
) -> List[tuple]:
    # Use default features if none specified
    if feature_possibilities is None:
        feature_possibilities = standard_feature_possibilities
        # If using standard features, also use standard canonical order
        if not canonical_order:
            canonical_order = standard_canonical_order

    # If canonical order of features not specified, just use alphabetical ordering
    if not canonical_order:
        canonical_order: Tuple[str, ...] = tuple(sorted(feature_possibilities.keys()))

    # Generate the deck
    deck: List[Tuple[Any, ...]] = list(
        product(*[feature_possibilities[f] for f in canonical_order])
    )

    # Shuffle the deck if desired
    if shuffle:
        if seed:
            random.seed(seed)
        random.shuffle(deck)  # note, this shuffles inplace

    return deck


def is_valid_set(cards: List[Tuple[Any, ...]]) -> bool:
    grouped_features: List[Tuple[Any, ...]] = list(zip(*cards))
    allowed_unique_counts: Tuple[int, int] = (
        1,
        len(cards),
    )  # read: must be all the same or all unique
    return all(len(set(g)) in allowed_unique_counts for g in grouped_features)


def count_valid_sets(
    cards: List[Tuple[Any, ...]], verbose: bool = True, set_size: int = 3
) -> int:
    if verbose:
        print(f"Checking: {cards}")
    found_matches: int = 0
    for candidate in list(permutations(cards, r=set_size)):
        if is_valid_set(candidate):  # noqa: general size accomodated
            found_matches += 1
            if verbose:
                print(f"... #{found_matches+1}: {candidate}")
    return found_matches


if __name__ == "__main__":
    # Define features of the deck, supports arbitrary number of dimensions and traits
    feature_possibilities: Dict[str, Tuple[Any, ...]] = {
        "number": (1, 2, 3),
        "color": ("red", "green", "purple"),
        "shading": ("open", "striped", "solid"),
        "shape": ("diamond", "squiggle", "oval"),
    }

    # Optionally define an order, this is cosmetic only. If you don't care, you can set to None for automatic ordering
    canonical_order: Tuple[str, str, str, str] = ("number", "color", "shading", "shape")

    # Generate the deck
    deck: List[Tuple[int, str, str, str]] = generate_deck(
        feature_possibilities=feature_possibilities,
        canonical_order=canonical_order,
        shuffle=True,
    )
