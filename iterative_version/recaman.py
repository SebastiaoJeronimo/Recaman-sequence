def recaman_sequence(n, sequence):
    i = 1
    sequence.append(0)
    while (i < n):
        if (sequence[i - 1] - i > 0) and ((sequence[i -1] - i) not in sequence):
            sequence.append(sequence[i - 1] - i)
        else :
            sequence.append(sequence[i - 1] + i) 
        i = i + 1
    return sequence

def main():
    n = int(input("Enter the nth number of the Recamán sequence: "))
    sequence = []
    recaman_sequence(n ,sequence)
    print("Recamán Sequence number:")
    print(sequence[n - 1])
    print("the sequence until it reaches that number:")
    print(sequence)

if __name__ == "__main__":
    main()
