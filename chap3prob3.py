def lengthOfStr(word):
    if word == "":
        return 0
    else:
        return 1 + lengthOfStr(word[1:])

class main():
    word = input("What string would you like to calculate the length of? ")
    print("Length of {}:".format(word), lengthOfStr(word))

      
# Run the unit tests.
if __name__ == '__main__':
    main()