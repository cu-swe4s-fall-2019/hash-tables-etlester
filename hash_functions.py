import sys

def h_ascii(key, N):
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s%N

def h_rolling(key, N):
    p = 53
    m=2**64
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s2 = s % m
    return s % N


def main():
    key = 'act'
    size = 1000
    print(type(key))
    output = h_rolling(key, size)
    print(output)

if __name__ == '__main__':
    main()
