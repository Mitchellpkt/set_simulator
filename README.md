# set_simulator

setsimulatorproject@mitchellpkt.com

Toy implementation of the [Set card game](https://en.wikipedia.org/wiki/Set_(card_game)) for running some numeric simulations to experimentally validate some analytical theories posited during a recent game.

The code currently supports full deck generation and set spotting from an arbitrary number of cards. The code allows an arbitrary number of feature dimensions (`f`) with an arbitrary number of categorical possibilities (`p`). The standard game rules use `f=4` (number, color, shading, shape) and `p=3` (e.g. red, purple, green).

This can be used to run some simple Monte Carlo simulations. For example, to show that randomly drawing 3 cards results in a valid set with probability `1/(p^f)`, we can just run 10 million deckwise numeric simulations and scan through each (sampling without replacement) to count successful matches:


```
100%|██████████| 10000000/10000000 [11:16<00:00, 14776.70it/s]


# of generated decks: 10000000
# of sets checked: 260000000
# of sets FOUND: 3290024
-----
>> Expect 1 valid set per 79.0268 checked sets
>> (1.2654% of the time)
-----
Wall time: 676.75 seconds
```
