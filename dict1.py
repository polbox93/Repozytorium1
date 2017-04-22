import os
import sys
import csv
import time


def main():
    #Opening a file to read
    with open("dictionary.csv", mode='r') as infile:
        reader = csv.reader(infile)

        mydict = {rows[0]:(rows[1], rows[2]) for rows in reader}

#Main menu
    os.system('clear')
    print ("WELCOME IN A DICTIONARY FOR A LITTLE PROGRAEMER")
    print ("-" *80)
    print ("Menu:")
#Displaying a list of menu
    list_of_command = ["1) search explanation by appellation", "2) add new definition",\
                    "3) show all appellations alphabetically", "0) exit"]
    for command in list_of_command:
        print (command)

    print("")
    print("-" *80)
# Asking user to choose a number from the menu
    choose = input("What do you want to do? Choose the number")

    if choose == "1": # search explanation by appellation
        os.system('clear')
        wanted_appel = input("Type here what you are looking for: ").lower()

        if wanted_appel in mydict:
            def_source='// '.join(mydict[wanted_appel])
            print(def_source)
        elif wanted_appel not in mydict:
            os.system('clear')
            print("No such appellation in a dictionary. Try again.")


        back_to_menu()

    elif choose == "2": # add new definition
        os.system('clear')
        given_appel = input("Enter an appellation that you want to add to dictionary: ").lower()
        given_def = input("Enter a definition that you want to add to appellation: ").lower()
        given_source = input("Enter a source that you want to add to appellation: ").lower()
        #it's checking no to add to dictionary an appellation without definition or source
        if given_appel == '' or given_appel == ' ':
            empty_lines()
        elif given_def == '' or given_def == ' ':
            empty_lines()
        elif given_source == '' or given_source == ' ':
            empty_lines()
        else:
            new_appel = ', '.join([given_appel, given_def, given_source])
            print(new_appel)
            print ('''New appellation: {} and new definition: {} with source: {} will
            be added to dictionary after closing a program'''\
            .format(given_appel, given_def, given_source))

        new_dict = open("dictionary.csv", 'a')
        new_dict.write(new_appel)
        new_dict.write("\n")
        new_dict.close

        back_to_menu()

    elif choose == "3": # show all appellations alphabetically
        os.system('clear')
        print("-"*80)
        print("Appellations in alphabetical order:")
        print(""*4)
        dict_alpha = sorted(mydict)
        for i in dict_alpha:
            print (i)

        back_to_menu()

    elif choose == "0": # exit aplication
        os.system('clear')
        print("THX for using my dictionary :)")
        time.sleep(2)
        os.system('clear')
        sys.exit()

    else: # appears when user input isn't the number form the menu
        print("Wrong input ! ! !")
        time.sleep(1)
        main()


# function  shows after every option from the menu. It allow to go back
# to the menu or quit the program
def back_to_menu():
    for i in range(2):
        print("")
    print("-"*80)
    go_back = input("To go back to the menu - press: whatever \nTo quit program - press: q")
    if go_back == "q":
        sys.exit()
    else:
        main()

#function shows arter leaving an empty line in "add new definition"
def empty_lines():
    os.system('clear')
    print('''SORRY! Your appellation has not been added to a dictionary.
You have to fill all the required lines. Try again.''')
    time.sleep(4)
    main()



main()
