from set_simulator.main import generate_deck, is_valid_set
from typing import Dict, Any, Tuple
from time import time
from tqdm.auto import tqdm

num_experiment_decks: int = 1_000_000
verbose: bool = False

# Define features of the deck, supports arbitrary number of dimensions and traits
standard_feature_possibilities: Dict[str, Tuple[Any, Any, Any]] = {
    "number": (1, 2, 3),
    "color": ("red", "green", "purple"),
    "shading": ("open", "striped", "solid"),
    "shape": ("diamond", "squiggle", "oval"),
}

num_options: int = 3  # more generally: len(standard_feature_possibilities[standard_canonical_order[0]])
num_checked_sets: int = 0
num_found_sets: int = 0
tic: float = time()
for experiment_number in tqdm(range(num_experiment_decks), mininterval=2):

    # Make the deck for this experiment
    deck = generate_deck(
        feature_possibilities=standard_feature_possibilities,
        canonical_order=None,  # will use standard
        seed=experiment_number,
        shuffle=True,
    )

    for i in range(int(len(deck) / num_options) - 1):
        three_card_draw = deck[i * num_options : num_options * (i + 1)]
        this_set_valid: bool = is_valid_set(three_card_draw)
        num_checked_sets += 1
        if this_set_valid:
            num_found_sets += 1
        if verbose:
            print(
                f"**\n{experiment_number=}\n{i=}\n{three_card_draw=}\n{this_set_valid=}"
            )

ratio: float = num_found_sets / num_checked_sets
print(
    f"""

# of generated decks: {num_experiment_decks}
# of sets checked: {num_checked_sets}
# of sets FOUND: {num_found_sets}
-----
>> Expect 1 valid set per {1/ratio:.4f} checked sets
>> ({ratio * 100:.4f}% of the time)
-----
Wall time: {time() - tic:.2f} seconds
"""
)
