def main():
    rle = "0102030405060708090101112131415"
    encoded = encode(rle)
    decoded = decode(encoded)
    print(rle)
    print("Encoded Result: " + formatOutput(encoded))
    print("Decoded Result: " + decoded)

def encode(sequence):
    count = 1
    result = []
    for x, item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1

    result.append((sequence[len(sequence) - 1], count))

    return result


def decode(sequence):
    result = []

    for item in sequence:
        result.append(item[0] * item[1])

    return "".join(result)


def formatOutput(sequence):
    result = []

    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])

    return "".join(result)


if __name__ == "__main__":
    main()