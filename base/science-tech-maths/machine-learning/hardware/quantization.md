# Quantization

Quantization is the process of converting the regular fp32 floats to lower precision floats, in order to reduce the memory and computational complexity.

## Floating-point formats

| Format | Sign bits | Exponent bits | Mantissa bits |
| ------ | --------- | ------------- | ------------- |
| FP32   | 1         | 8             | 23            |
| TF32   | 1         | 8             | 10            |
| FP16   | 1         | 5             | 10            |
| BF16   | 1         | 8             | 7             |

Mantissa bits are the bits that represent the precision of the number.

Exponent bits are the bits that represent the range of the number.

FP16 has a better precision than BF16, but BF16 has a better range.

FP16 is commonly used in deep learning training and inference, especially for tasks that require high precision in representing small fractional values within a limited range.

BF16 is becoming popular when dealing with large gradients or when numerical stability across a wide range is more important than precision of small values.

## INT8

1 bit for sign, 7 bits for the rest.

$2^7 = 128$, so values are from -128 to 127.

In practice, we do not need to map the entire FP32 range \[-3.4e38, 3.4e38\] into INT8.

To map FP32 to INT8, we can use the following formula:

$Q = \frac{S}{2^7} \times FP32$

where $S$ is the scaling factor, which is a constant value that scales the FP32 values to the INT8 range.

$S = \frac{2^7}{FP32_{max} - FP32_{min}}$

$FP32_{max}$ is the maximum value of the FP32 range.

$FP32_{min}$ is the minimum value of the FP32 range.

But if we know that our values will be in a specific range, we can use that range to calculate the scaling factor.

For example, if we know that our values will be in the range \[-1, 1\], we can use the following formula:

$S = \frac{2^7}{1 - (-1)} = 64$

This is a symmetric quantization. If your data follows a non-uniform distribution, you can use an asymmetric quantization.
