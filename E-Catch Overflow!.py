def main():
    l = int(input())
    result = 0
    multiplier = 1
    overflow = 2 ** 32
    counter = []

    for _ in range(l):
        command = input()
        if command.startswith("for"):  # command == "for n"
            n = int(command.split()[1])
            multiplier *= n
            counter.append(n)
        elif command == "end":  # command == end
            n = counter[-1]
            multiplier //= n
            counter.pop()
        else:  # command == "add"
            result += multiplier
            if result >= overflow:
                print("OVERFLOW!!!")
                return

    print(result)


if __name__ == "__main__":
    main()
