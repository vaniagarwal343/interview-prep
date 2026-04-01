# Bit Manipulation

## Core Sub-Patterns

- **XOR for finding unique elements:** pairs cancel (a ^ a = 0), single remains. Pick when exactly one element is unpaired and all others appear twice.
- **XOR for finding missing numbers:** XOR expected range with actual array. The missing number survives because it has no pair. Pick for "find the missing number in 0..n" problems.
- **Bit masking:** check/set/clear individual bits with `&`, `|`, `~`. Pick when the problem involves flags, subsets, or checking specific bit positions.
- **Bit shifting:** multiply/divide by powers of 2 with `<<` and `>>`. Pick when the problem involves powers of 2, binary representations, or efficient arithmetic.

## #136 Single Number

- **Pattern:** XOR (Bit Manipulation)
- XOR all elements together — pairs cancel to 0, the unique element remains
- Time: O(n) | Space: O(1)
