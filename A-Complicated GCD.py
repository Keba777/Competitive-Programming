from sys import stdin
def main():
    a, b = map(int, stdin.readline().strip().split())
    if a == b:
        print(a)
    else:
        print(1)
main()
