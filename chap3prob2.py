def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)
    
class main():
    num = int(input("What integer would you like to calculate the factorial of? "))
    print("Factorial:", factorial(num))

      
# Run the unit tests.
if __name__ == '__main__':
    main()