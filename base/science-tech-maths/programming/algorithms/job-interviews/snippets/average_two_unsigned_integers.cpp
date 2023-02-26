// Finding the average of two unsigned integers, rounding toward zero, sounds easy:

unsigned average_dumb(unsigned a, unsigned b) { return (a + b) / 2; }

// However, this gives the wrong answer in the face of integer overflow: For example, if unsigned integers are 32 bits
// wide, then it says that average(0x80000000U, 0x80000000U) is zero.

// If you know which number is the larger number (which is often the case), then you can calculate the width and halve
// it:

unsigned average_low_high(unsigned low, unsigned high) { return low + (high - low) / 2; }

// There’s another algorithm that doesn’t depend on knowing which value is larger, the U.S. patent for which expired in
// 2016:

unsigned average(unsigned a, unsigned b) { return (a / 2) + (b / 2) + (a & b & 1); }

// The trick here is to pre-divide the values before adding. This will be too low if the original addition contained a
// carry from bit 0 to bit 1, which happens if bit 0 is set in both of the terms, so we detect that case and make the
// necessary adjustment.

// a & b & 1: the &1 means that we only care about the lowest bit of a and b
// 0 & 0: 0, we add nothing, a/2 and b/2 divions don't have remainder
// 1 & 0: 0, a = 1 and b = 0 for exemple, mean is equal to 0, a/2 and b/2 divions don't have remainder
// 1 & 1: 1, a = 1 and b = 1 for exemple, mean is equal to 1, a/2 and b/2 divions are equal to 0, we add 1
