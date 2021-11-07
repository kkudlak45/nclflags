#!/usr/bin/python3

print("hello world")

l = open("letters.txt", "r")

while True:
    currentLetters = l.readline()
    if not currentLetters:
        break

    n = open("numbers.txt", "r")
    while True:
        currentNumber = n.readline()
        if not currentNumber:
            break
        print("SKY-" + currentLetters[:4] + "-" + currentNumber[:4])

    n.close()

l.close()
