import random

def master_mind():

    num = random.randrange(1000, 10000)

    n = int(input("Guess the 4 digit number: "))

    if(n == num):
        print("Nice job! You guess the number in 1 try! You're a Mastermind!")
    else:
        counter = 0
        

        while (n != num):
            counter += 1
            count = 0

            n_str = str(n)
            num_str = str(num)
            correct = ['x']*4

            for i in range(4):
                if n_str[i] == num_str[i]:
                    count += 1
                    correct[i] = n_str[i]

            if count > 0:
                print("Not quite the number. But you did get", count, "digit(s) correct!\n")
            else:
                print("None of the numbers in your input match.")
            
            n = int(input("Enter your next choice of numbers: "))

    counter += 1 
    if n == num:
        if counter == 1:
            print("Nice job! You guessed the number in 1 try! You're a Mastermind!")
        else:
            print("You've become a Mastermind!")
            print("It took you", counter, "tries.")


if __name__ == "__main__":
    master_mind()