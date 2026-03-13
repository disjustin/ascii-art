# **ASCII String Generator**

## Table of Contents

- [**ASCII String Generator**](#ascii-string-generator)
  - [Table of Contents](#table-of-contents)
  - [Summary](#summary)
  - [Usage](#usage)

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

# Lowercase
python print_ascii_text.py --input "Hello" --case lower

# Mixed case (none)
python print_ascii_text.py --input "Hello World" --case none
```

**Full CLI Options:**

```plain
usage: print_ascii_text.py [-h] [--input INPUT] [--stdin] [--output OUTPUT]
                           [--mode {append,overwrite}] [--buffer BUFFER]
                           [--bold] [--case {upper,lower,none}] [--verbose]

Generate ASCII art text.

positional arguments:
  input_text           Input text (alternative to --input)

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT, -i INPUT
                       Input text string
  --stdin, -s          Read input from stdin
  --output OUTPUT, -o OUTPUT
                       Output file (default: stdout)
  --mode {append,overwrite}, -m {append,overwrite}
                       Output mode (default: append)
  --buffer BUFFER, -B BUFFER
                       Blank lines above/below font (default: 0)
  --bold, -b           Use bold font variant
  --case {upper,lower,none}, -c {upper,lower,none}
                       Case conversion (default: none)
  --verbose, -v        Print debug info
```

**Sample Output (default):**

```plain
# python print_ascii_text.py "Hello World" --bold

#   #       ##    ##                #   #             ##       #
#   #        #     #                #   #              #       #
#####  ##    #     #     ##         #   #  ##   ###    #     ###
#   # # ##   #     #    #  #        # # # #  #  #  #   #    #  #
#   # ##     #     #    #  #        # # # #  #  #      #    #  #
#   #  ##   ###   ###    ##          # #   ##   #     ###    ###

python print_ascii_text.py "Hello World"

H   H       ##    ##                W   W             ##       #
H   H        #     #                W   W              #       #
HHHHH  ##    #     #     ##         W   W  ##   ###    #     ###
H   H # ##   #     #    #  #        W W W #  #  #  #   #    #  #
H   H ##     #     #    #  #        W W W #  #  #      #    #  #
H   H  ##   ###   ###    ##          W W   ##   #     ###    ###

python print_ascii_text.py "Hello World" --case upper

H   H EEEEE L     L      OOO        W   W  OOO  RRRR  L     DDDD
H   H E     L     L     O   O       W   W O   O R   R L     D   D
HHHHH EEEEE L     L     O   O       W   W O   O RRRR  L     D   D
H   H E     L     L     O   O       W W W O   O R   R L     D   D
H   H E     L     L     O   O       W W W O   O R   R L     D   D
H   H EEEEE LLLLL LLLLL  OOO         W W   OOO  R   R LLLLL DDDD

python print_ascii_text.py "Hello World" --case lower

#           ##    ##                                  ##       #
#            #     #                                   #       #
###    ##    #     #     ##         #  #   ##   ###    #     ###
#  #  # ##   #     #    #  #        #  #  #  #  #  #   #    #  #
#  #  ##     #     #    #  #        ####  #  #  #      #    #  #
#  #   ##   ###   ###    ##         ####   ##   #     ###    ###

```
