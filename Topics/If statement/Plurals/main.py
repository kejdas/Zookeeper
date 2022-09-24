number = int(input())
word = input()

if(number >= 2 or number == 0):
    word = word + "s"
    print(number, word)

elif (number < 2):
    print(number, word)