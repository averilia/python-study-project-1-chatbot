def greeting(bot_name, birth_year): # the bot writes its name and birth year
    print('Hello! My name is ' + bot_name + ' .')
    print('I was created in ' + birth_year + ' .')

def remind_name(): # bot asks for the user's name
    print('Please, remind me your name.')
    user_name = input() # user inputs his name
    print('What a great name you have, ' + user_name + '!')

def guess_age(): # user age is calculated on the basis of 3 integers taken from input
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input()) # remainder of user's age integer division by 3
    rem5 = int(input()) # remainder of user's age integer division by 5
    rem7 = int(input()) # remainder of user's age integer division by 7
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105 # age is calculated here

    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count(): # bot prints numbers from 0 up to the input integer value, each on a new line
    print('Now I will prove to you that I can count to any number you want.')
    end_number = int(input()) # user inputs a number
    counter = 0
    while counter <= end_number:
        print(str(counter) + ' !') # each next number is printed on a new line accompanied by an exclamation mark
        counter += 1

def testing(): # question with answers to choose from
    print("Let's test your programming knowledge.")
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    answer = input()
    while answer != '2': # the correct answer is 2. "To decompose..."
        print('Please, try again.')  # the while loop continues until the input is 2, which is the correct answer
        answer = input()
    print('Completed, have a nice day!') # the result of a correct answer

def end():
    print('Congratulations, have a nice day!') # message in the end


greeting('Zax', '2022') # name and birth year used as parameters for the greeting function
remind_name()
guess_age()
count()
testing()
end()
