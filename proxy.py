import sys
import socket
import threading

HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range (256)])

def hexdump(src, length = 16, show = True):

    results = list()
    length = 16
    for i in range(0, len(src), length):
        word = str(src[i:i + length])
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexawidth = length * 3
        results.append(f'{i:04x} {hexa:<{hexawidth}} {printable}')
    if show:
        for line in results:
            print(line)
    else: 
        return results

if __name__ == '__main__':
    hexdump('1233242klasjgd alkmflkasjf laksjf aksldj flasjd flkas jfkjafk l')