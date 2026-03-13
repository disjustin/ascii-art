# **ASCII String Generator**

## Table of Contents

- [**ASCII String Generator**](#ascii-string-generator)
  - [Table of Contents](#table-of-contents)
  - [Summary](#summary)
  - [Usage](#usage)
  - [Future](#future)

## Summary

`print_ascii_text.py` generates ASCII art text from input using an embedded 5x7 font. Supports buffer padding, bold variant, and various CLI options. Outputs to stdout by default or file with append/overwrite modes. Handles printable ASCII characters (32-126), defaults to uppercase.

## Usage

**Installation:**

```bash
git clone https://github.com/juuwong/ASCII_art.git
cd ASCII_ART
python print_ascii_text.py --help
```

**Examples:**

```bash
# Basic usage (prompts for input)
python print_ascii_text.py

# Direct input
python print_ascii_text.py "HELLO WORLD"

# Custom output and options
python print_ascii_text.py --input "BIG TEXT" --buffer 2 --bold --output art.txt --mode overwrite --verbose

# Stdin input
echo "test" | python print_ascii_text.py --stdin --buffer 1

# No uppercase
python print_ascii_text.py --input "Hello" --no-upper
```

**Full CLI Options:**

```plain
usage: print_ascii_text.py [-h] [--input INPUT] [--stdin] [--output OUTPUT]
                           [--mode {append,overwrite}] [--buffer BUFFER]
                           [--bold] [--no-upper] [--verbose]

Generate ASCII art text.

positional arguments:
  input_text           Input text (alternative to --input)

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT, -i INPUT
                       Input text string
  --stdin, -s          Read input from stdin
  --output OUTPUT, -o OUTPUT
                       Output file (default: output.txt)
  --mode {append,overwrite}, -m {append,overwrite}
                       Output mode (default: append)
  --buffer BUFFER, -B BUFFER
                       Blank lines above/below font (default: 0)
  --bold, -b           Use bold font variant
  --no-upper, -u       Do not uppercase input
  --verbose, -v        Print debug info
```

**Sample Output (default):**

```plain
H   H EEEEE L     L      OOO     W   W  OOO  RRRR  L     DDDD
H   H E     L     L     O   O    W   W O   O R   R L     D   D
HHHHH EEEEE L     L     O   O    W   W O   O RRRR  L     D   D
H   H E     L     L     O   O    W W W O   O R   R L     D   D
H   H E     L     L     O   O    W W W O   O R   R L     D   D
H   H EEEEE LLLLL LLLLL  OOO      W W   OOO  R   R LLLLL DDDD
```

## Future

- Add lowercase font support

- Custom font loading
- Color output options
- Web interface

> Updated 6/13/22
