import os
import sys

start = True
while start:
    os.system('clear')
    number = input("Enter your number and after space enter actual system ")

    def bin_to_dec(num):
        length = len(num)-2
        result = 0
        for i in range (1, length+1):
            result = result + int(num[i-1]) * 2 ** (length-i)
        print ("The decimal of entered binary is: ", result)

    def dec_to_bin(num):
        number = int(num[:-3])
        decimal = []
        while number > 0:
            bit = number % 2
            quotient = number // 2
            decimal.insert(0, str(bit))
            number = quotient
            result = ''.join(decimal)
        print("The binary of entered decimal is: ", result)

    def exit():
        exit = input("To count again press anything / to exit press q: ")
        if exit.lower() == "q":
            os.system('clear')
            print ("Thanks for using my super program")
            sys.exit()
        else:
            start = True


    if number[-2:] == " 2":
        bin_to_dec(number)
        exit()
    elif number[-3:] == " 10":
        dec_to_bin(number)
        exit()  #dlaczego bez tego program po wpisaniu np "8 10" startowal od nowa?
    else:
        os.system('clear')
        print("You entered wrong number format. Check it out and enter again")
        exit()
