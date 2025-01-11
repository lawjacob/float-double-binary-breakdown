
# IEEE754-Binary-Breakdown

A Python script that breaks down and visualizes the IEEE 754 representation of single-precision (float) and double-precision (double) floating-point numbers in binary. This project is intended to help users better understand how the IEEE 754 standard works behind the scenes to represent floating-point numbers in binary form.

---

## Overview

This project provides:

- A detailed breakdown of the **sign**, **exponent**, and **mantissa** of a floating-point number in both single-precision (32-bit) and double-precision (64-bit) formats.
- Methods to reconstruct the original floating-point number from its binary representation.
- A visualization of the implicit components of the mantissa and how the exponent bias works.
- An educational explanation of how floating-point numbers are stored and calculated in binary.

---

## Features

- **Single-Precision (32-bit)** and **Double-Precision (64-bit)** support.
- Conversion of a floating-point number into its binary representation.
- Deconstruction of the following components:
  - **Sign**: Determines whether the number is positive or negative.
  - **Exponent**: Encoded with a bias (127 for float, 1023 for double).
  - **Mantissa**: Encodes the fractional part of the number with an implicit leading 1.
- Reconstruction of the floating-point number from its binary components.
- Explanation of the mantissa's fractional terms and how they contribute to the final number.
- Educational output to help visualize the process.

---

## How It Works

### Single-Precision (32-bit)

The IEEE 754 single-precision representation:
- **1 bit** for the sign
- **8 bits** for the exponent (biased by 127)
- **23 bits** for the mantissa (with an implicit leading "1")

### Double-Precision (64-bit)

The IEEE 754 double-precision representation:
- **1 bit** for the sign
- **11 bits** for the exponent (biased by 1023)
- **52 bits** for the mantissa (with an implicit leading "1")

---

## Usage

1. Clone the repository
2. Run the script:
   ```bash
   python ieee754_decoder.py
   ```

3. By default, the script demonstrates the breakdown of a double-precision number (`5.75`). You can modify the `main()` function to test other values.

---

## Example Output

For the double-precision number `5.75`, the script will output:

```
Binary representation of 0100000000010111000000000000000000000000000000000000000000000000
Sign: + 
Exponent: 10000000001 = 2
Mantissa: 0111000000000000000000000000000000000000000000000000
Deconstructed: 0*2^-1 + 1*2^-2 + 1*2^-3 + 1*2^-4 + trailing 0s
With implicit 1: 1.875
Final value: +1*2^2*1.875 = 7.5
```

This output explains each part of the binary representation, how the mantissa is reconstructed, and how the final value is computed.

---

## Code Structure

### `IEEE754Float` Class
Handles single-precision (32-bit) floating-point numbers:
- `from_float(num: float)`: Converts a Python float to its IEEE 754 binary representation.
- `get_actual_exponent()`: Calculates the actual exponent by removing the bias.
- `get_mantissa_value()`: Computes the value of the mantissa, including the implicit leading "1".
- `to_float()`: Reconstructs the original float from the binary components.
- `get_mantissa_terms()`: Returns a list of fractional terms that contribute to the mantissa.

### `IEEE754Double` Class
Handles double-precision (64-bit) floating-point numbers:
- Similar methods to `IEEE754Float`, but adjusted for double-precision representation.

### `main()`
Demonstrates the usage of the `IEEE754Double` class by breaking down a double-precision number.

---

## Requirements

- Python 3.8 or later

No external libraries are required, as the script uses Python's built-in `struct` module.

---

## Customization

To analyze a different number:
- Modify the `double_number` or `float_number` variable in the `main()` function:

   ```python
   double_number = YOUR_NUMBER
   ieee754 = IEEE754Double.from_double(double_number)
   ```

For single-precision:
- Use the `IEEE754Float` class instead:

   ```python
   float_number = YOUR_NUMBER
   ieee754 = IEEE754Float.from_float(float_number)
   ```
