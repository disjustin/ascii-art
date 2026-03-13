import sys
import argparse

# Embedded font dictionary
FONT = {
    ' ': ['     '] * 7,
    '!': [' !!! ', ' !!! ', ' !!! ', ' !!! ', '     ', ' !!! ', '     '],
    '"': ['"" ""', '"" ""', '     ', '     ', '     ', '     ', '     '],
    '#': [' # # ', '#####', ' # # ', ' # # ', '#####', ' # # ', '     '],
    '$': ['  $  ', ' $$$$', '$ $  ', ' $$$ ', '  $ $', '$$$$ ', '     '],
    '%': ['%   %', '   % ', '  %  ', '  %  ', ' %   ', '%   %', '     '],
    '&': ['  &  ', '&  & ', ' &&  ', ' && &', '& & &', ' & & ', '     '],
    "'": [' ''  ', ' ''  ', '     ', '     ', '     ', '     ', '     '],
    '(': [' ((  ', '((   ', '((   ', '((   ', '((   ', ' ((  ', '     '],
    ')': ['  )) ', ' ))  ', ' ))  ', ' ))  ', ' ))  ', '  )) ', '     '],
    '*': ['  *  ', ' *** ', '  *  ', '     ', '     ', '     ', '     '],
    '+': ['     ', '     ', '  +  ', ' +++ ', '  +  ', '     ', '     '],
    ',': ['     ', '     ', '     ', '     ', ' ,,  ', ' ,,  ', '     '],
    '-': ['     ', '     ', '     ', ' --- ', '     ', '     ', '     '],
    '.': ['     ', '     ', '     ', '     ', ' ..  ', ' ..  ', '     '],
    '/': ['    /', '   / ', '  /  ', '  /  ', ' /   ', '/    ', '     '],
    '0': ['00000', '0   0', '0   0', '0   0', '0   0', '00000', '     '],
    '1': [' 11  ', '1 1  ', '  1  ', '  1  ', '  1  ', '11111', '     '],
    '2': [' 222 ', '2   2', '   2 ', '  2  ', ' 2   ', '22222', '     '],
    '3': ['3333 ', '    3', '3333 ', '    3', '    3', '3333 ', '     '],
    '4': ['4   4', '4   4', '44444', '    4', '    4', '    4', '     '],
    '5': ['55555', '5    ', '5555 ', '    5', '    5', '5555 ', '     '],
    '6': [' 666 ', '6   6', '6    ', '6666 ', '6   6', ' 666 ', '     '],
    '7': ['77777', '    7', '   7 ', '  7  ', ' 7   ', '7    ', '     '],
    '8': [' 888 ', '8   8', ' 888 ', '8   8', '8   8', ' 888 ', '     '],
    '9': [' 999 ', '9   9', ' 9999', '    9', '9   9', ' 999 ', '     '],
    ':': ['     ', ' ::  ', ' ::  ', '     ', ' ::  ', ' ::  ', '     '],
    ';': ['     ', ' ;;  ', ' ;;  ', '     ', ' ;;  ', ' ;;  ', '     '],
    '<': ['     ', '    <', '  <  ', '<    ', '  <  ', '    <', '     '],
    '=': ['     ', '     ', ' === ', '     ', ' === ', '     '],
    '>': ['     ', '>    ', '  >  ', '    >', '  >  ', '>    ', '     '],
    '?': [' ??? ', '?   ?', '    ?', ' ??? ', '     ', '  ?  ', '     '],
    '@': [' @@@ ', '@   @', '@ @ @', '@ @@@', '@    ', ' @@@@', '     '],
    'A': [' AAA ', 'A   A', 'AAAAA', 'A   A', 'A   A', 'A   A', '     '],
    'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'B   B', 'BBBB ', '     '],
    'C': [' CCC ', 'C   C', 'C    ', 'C    ', 'C   C', ' CCC ', '     '],
    'D': ['DDDD ', 'D   D', 'D   D', 'D   D', 'D   D', 'DDDD ', '     '],
    'E': ['EEEEE', 'E    ', 'EEEEE', 'E    ', 'E    ', 'EEEEE', '     '],
    'F': ['FFFFF', 'F    ', 'FFFF ', 'F    ', 'F    ', 'F    ', '     '],
    'G': [' GGGG', 'G    ', 'G    ', 'G  GG', 'G   G', ' GGG ', '     '],
    'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H', 'H   H', '     '],
    'I': [' III ', '  I  ', '  I  ', '  I  ', '  I  ', ' III ', '     '],
    'J': ['    J', '    J', '    J', '    J', 'J   J', ' JJJ ', '     '],
    'K': ['K   K', 'K  K ', 'KKK  ', 'K  K ', 'K   K', 'K   K', '     '],
    'L': ['L    ', 'L    ', 'L    ', 'L    ', 'L    ', 'LLLLL', '     '],
    'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M', 'M   M', '     '],
    'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N', 'N   N', '     '],
    'O': [' OOO ', 'O   O', 'O   O', 'O   O', 'O   O', ' OOO ', '     '],
    'P': ['PPPP ', 'P   P', 'P   P', 'PPPP ', 'P    ', 'P    ', '     '],
    'Q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q   Q', 'Q  Q ', ' QQ Q', '     '],
    'R': ['RRRR ', 'R   R', 'RRRR ', 'R   R', 'R   R', 'R   R', '     '],
    'S': [' SSSS', 'S    ', ' SSS ', '    S', '    S', 'SSSS ', '     '],
    'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  ', '  T  ', '     '],
    'U': ['U   U', 'U   U', 'U   U', 'U   U', 'U   U', ' UUU ', '     '],
    'V': ['V   V', 'V   V', 'V   V', 'V   V', ' V V ', '  V  ', '     '],
    'W': ['W   W', 'W   W', 'W   W', 'W W W', 'W W W', ' W W ', '     '],
    'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X', 'X   X', '     '],
    'Y': ['Y   Y', 'Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  ', '     '],
    'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'Z    ', 'ZZZZZ', '     '],
    '[': [' [[[ ', ' [   ', ' [   ', ' [   ', ' [   ', ' [[[ ', '     '],
    '\\': ['\\    ', ' \\   ', '  \\  ', '  \\  ', '   \\ ', '    \\', '     '],
    ']': [' ]]] ', '   ] ', '   ] ', '   ] ', '   ] ', ' ]]] ', '     '],
    '^': ['  ^  ', ' ^ ^ ', '     ', '     ', '     ', '     ', '     '],
    '_': ['     ', '     ', '     ', '     ', '     ', ' ___ ', '     '],
    '`': [' `   ', '  `  ', '     ', '     ', '     ', '     ', '     '],
    'a': [],
    'b': [],
    'c': [],
    'd': [],
    'e': [],
    'f': [],
    'g': [],
    'h': [],
    'i': [],
    'j': [],
    'k': [],
    'l': [],
    'm': [],
    'n': [],
    'o': [],
    'p': [],
    'q': [],
    'r': [],
    's': [],
    't': [],
    'u': [],
    'v': [],
    'w': [],
    'x': [],
    'y': [],
    'z': [],
    '{': [],
    '|': [],
    '}': [],
    '~': [],
}

def main():
    parser = argparse.ArgumentParser(description="Generate ASCII art text.")
    parser.add_argument('input_text', nargs='?', help='Input text')
    parser.add_argument('--input', '-i', help='Input text string')
    parser.add_argument('--stdin', '-s', action='store_true', help='Read input from stdin')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--mode', '-m', choices=['append', 'overwrite'], default='append', help='Output mode')
    parser.add_argument('--buffer', '-B', type=int, default=0, help='Blank lines above/below font (default: 0)')
    parser.add_argument('--bold', '-b', action='store_true', help='Use bold font variant')
    parser.add_argument('--no-upper', '-u', action='store_true', help='Do not uppercase input')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print debug info')

    args = parser.parse_args()

    # Input handling
    if args.stdin:
        input_text = sys.stdin.read().strip()
    elif args.input:
        input_text = args.input
    elif args.input_text:
        input_text = args.input_text
    else:
        input_text = input()

    if not args.no_upper:
        input_text = input_text.upper()

    if args.verbose:
        print(f"Input: {input_text}")

    # Render
    def get_char_lines(c, bold):
        if c not in FONT or not FONT[c]:
            c = '?'
        lines = FONT[c][:7]  # base 7
        if bold:
            lines = [''.join('#' if ch != ' ' else ch for ch in line) for line in lines]
        return lines

    total_height = 7 + 2 * args.buffer
    output_lines = [''] * total_height
    for c in input_text:
        char_lines = get_char_lines(c, args.bold)
        for i in range(7):
            output_lines[args.buffer + i] += char_lines[i] + ' '

    # Trim trailing spaces
    output_lines = [line.rstrip() for line in output_lines]

    # Output
    if args.output:
        mode = 'a' if args.mode == 'append' else 'w'
        with open(args.output, mode) as f:
            for line in output_lines:
                f.write(line + '\n')
        if args.verbose:
            print(f"Output to {args.output}, mode {args.mode}, buffer {args.buffer}, bold {args.bold}")
    else:
        print('\n'.join(output_lines))
        if args.verbose:
            print(f"Output to stdout, buffer {args.buffer}, bold {args.bold}")

if __name__ == '__main__':
    main()