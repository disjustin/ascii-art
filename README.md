# **ASCII String Generator**

## Table of Contents
- [**ASCII String Generator**](#ascii-string-generator)
	- [Table of Contents](#table-of-contents)
	- [Summary](#summary)
	- [Usage](#usage)
	- [Future](#future)

## Summary

`print_ascii_text.py` reads a specified input and generates a 5x7 ascii text in `output.txt`. Handles ASCII characters #32-122 and prints #32-96, [see here for ascii table](https://www.asciitable.com/).

## Usage

**Program/script:**
```
git clone https://github.com/juuwong/ASCII_art.git
cd ASCII_ART
```
```bash
# The following produces the same output `HELLO WORLD`

# Command Line Arguments: 1
.\print_ascii_text.py
Please enter your input:
hello world
['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# Command Line Arguments: 2
.\print_ascii_text.py "hello world"
['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# Command Line Arguments: 3+
.\print_ascii_text.py hello world
['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
```
**output.txt**
```
H   H EEEEE L     L      OOO     W   W  OOO  RRRR  L     DDDD  
H   H E     L     L     O   O    W   W O   O R   R L     D   D 
HHHHH EEEEE L     L     O   O    W   W O   O RRRR  L     D   D 
H   H E     L     L     O   O    W W W O   O R   R L     D   D 
H   H E     L     L     O   O    W W W O   O R   R L     D   D 
H   H EEEEE LLLLL LLLLL  OOO      W W   OOO  R   R LLLLL DDDD  
                                                               
```

## Future
* output file options, overwrite or append (default)
* command short/long arguments (-h/--help, -v/--verbose, -q/--quiet)
* add lowercase ascii

> Updated 6/13/22