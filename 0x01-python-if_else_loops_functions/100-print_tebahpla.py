for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
        k = 0
        else:
            k = 32
            print('{}'.format(chr(c - k)), end='')
