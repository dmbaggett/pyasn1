#
# Some precomputation, to speed up bit string maniuplations up by about 5x.
#
# Dave Baggett (Arcode Corporation)
#

# Tuples corresponding to bit patterns from 0 to 255:
BITPATTERN = [
    tuple(((x >> shift)  & 1)
          for shift in reversed(range(8)))
    for x in range(256)
]

# dict mapping bit patterns to characters
BITPATTERN_TO_BYTE = dict(
    (pattern, chr(value))
    for value, pattern in enumerate(BITPATTERN)
)
