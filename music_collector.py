import os
import sys
import csv
import time
import random

def add_new_album():
    os.system('clear')
    add_artist_name = input('Enter a name of artist: ')
    add_album_name = input('Enter a name of album: ')
    add_year = input('Enter a year of release: ')
    add_genre = input('Enter a genre of music: ')
    add_length = input('Enter length of album: ')

    with open('music.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([add_artist_name , add_album_name , add_year , add_genre , add_length])


def find_albums_by_artist(my_list):
    music_final_2 = []
    music_final_2_1 = []
    for album in my_list:
        name_list_2 = (album[0].lower().strip(), album[1].strip())
        music_final_2.append(name_list_2)
        music_final_2_1.append(album[0].lower().strip())

    os.system('clear')

    given_artist = input("Enter artist name to find album name: ").lower()
    if given_artist in music_final_2_1:
        os.system('clear')
        print("Your request: %s" %(given_artist))
        print("Album:")
        for element in music_final_2:
            if given_artist == element[0]:
                print(element[1])
        exit()

    elif not given_artist in music_final_2_1:
        os.system('clear')
        print("No such artist on a playlist. Try again.")
        time.sleep(2)
        True

def find_albums_by_year(my_list):
    list_of_year = []      # dodaję na listę tuple z danymi:album, wykonawca i rok
    for album in my_list:
        name_list_3 = (album[0].strip(), album[1].strip(), int(album[2]))
        list_of_year.append(name_list_3)


    os.system('clear')

    given_year = input("Enter a year to find album name: ")

    # spradza czy wpisana wartosc ma 4 znaki i jest cyfrą
    if len(given_year) == 4 and given_year .isdigit():
        given_year_int = int(given_year)    #zmienia rok z pliku na integera

        for item in list_of_year:       #jeśli wpisany rok jest na liście, wyświetla album i autora
            if given_year_int == item[2]:
                print(item[1],' by: ',item[0])
        exit()      #Funkcja pyta czy po wykonaniu instrukcji ma wyjść z programu czy wróic do menu
    else:
        os.system('clear')
        print('No such years on a playlist. Try again')
        time.sleep(2)
        True


def find_musician_by_album(my_list):
    music_final_4 = []
    music_final_4_1 = []
    for album in my_list:
        name_list_4 = (album[0].strip(), album[1].lower().strip())
        music_final_4.append(name_list_4)
        music_final_4_1.append(album[1].lower().strip())

    os.system('clear')

    given_album = input("Enter album name to find artist: ").lower()
    if given_album in music_final_4_1:
        os.system('clear')
        print("Your request: %s" %(given_album))
        print("Artists:")
        for element in music_final_4:
            if given_album == element[1]:
                print(element[0])
        exit()
    elif not given_album in music_final_4_1:
        os.system('clear')
        print("No such album on a playlist. Try again.")
        time.sleep(2)
        True


def find_albums_by_letter(my_list):
    music_final_5 = []      #lista tupli nazwa albumu i wykonawca
    music_final_5_1 = []        #lista samych nazw albumów
    for album in my_list:
        name_list_5 = (album[0].strip(), album[1].lower().strip())
        music_final_5.append(name_list_5)
        music_final_5_1.append(album[1].lower().strip())

    letters = set(music_final_5_1)      # set w celu niepowtarzania nazw
    let_1 = []
    for element in letters:
        let = list(element)
        let_1.extend(let)
        let_2 = set(let_1)      #set z literami

    os.system('clear')

    given_letter = input("Enter letter(s): ")
    if given_letter in let_2:       #jeśli litera jest w "secie sprawdzającym"
        os.system('clear')
        print("Your request: %s" %(given_letter))
        print("Albums:")

        for item in music_final_5:      # dla elementów w liście z tuplami
            if given_letter in item[1]:
                print(item[0]," by: ",album[1])
        exit()
    elif not given_letter in let_2:
        print("no such letter in word")
        time.sleep(2)
        True


def find_albums_by_genre(my_list):
    list_of_genre = []
    list_of_genre_1 = []
    for album in my_list:
        name_list_6 = (album[0].strip(), album[1].strip(), album[3].strip())
        list_of_genre.append(name_list_6)
        list_of_genre_1.append(album[3].strip())

    os.system('clear')

    given_genre = input("Enter genre to find album name: ")
    if given_genre in list_of_genre_1:
        os.system('clear')
        print("Your request: %s" %(given_genre))
        print("Album:")

        for item in list_of_genre:
            if given_genre == item[2]:
                print(item[1],' by: ',item[0])
        exit()
    elif not given_genre in list_of_genre_1:
            os.system('clear')
            print('No such genre on a playlist. Try again')
            time.sleep(2)
            True

def age_of_all_albums(my_list):
    list_of_year = []
    list_of_ages = []
    for album in my_list:
        list_of_ages.append(2017 - int(album[2]))

    os.system('clear')

    sum_age = sum(list_of_ages)

    print(sum_age)
    exit()

def random_album_by_genre(my_list):
    list_of_genre_random = []
    list_of_genre_8 = []
    for album in my_list:
        name_list_8 = (album[0].strip(), album[1].strip(), album[3].strip())
        list_of_genre_random.append(name_list_8)
        list_of_genre_8.append(album[3].strip())

    os.system('clear')

    given_genre = input("Enter genre to find a random album name: ")
    if given_genre in list_of_genre_8:
        os.system('clear')
        print("Your request: %s" %(given_genre))
        print("Random album:")

        list_of_albums_random = []

        for item in list_of_genre_random:
            if given_genre == item[2]:
                list_of_albums_random.append(item[1])

        random_index = random.randint(0, len(list_of_albums_random))
        print(list_of_albums_random[random_index])
        exit()

    elif not given_genre in list_of_genre_8:
            os.system('clear')
            print('No such genre on a playlist. Try again')
            time.sleep(2)
            True


def exit_by_0():
    os.system('clear')
    print("THX for using my program :)")
    time.sleep(2)
    os.system('clear')
    sys.exit()

def exit():
    print(''*4)
    print('#'*80)
    chose = input("To quit press q, to go back to menu press anything")
    if chose == "q" or chose == "Q":
        sys.exit()
    else:
        True


def main():
    start = True
    while True:

        with open("music.csv", mode='r') as f:
            reader = csv.reader(f, delimiter = '|')

            my_list = list(reader)

        name_list = ()
        info_list = ()
        music_list = []
        music_final = []

        for album in my_list:
            name_list = (album[0], album[1])
            info_list = (int(album[2]), album[3], album[4])
            album_list = [name_list, info_list]
            music_final.append(album_list)


        os.system('clear')
        print('-'*80)
        print ("WELCOME IN A MUSIC COLLECTOR")
        print ("-" *80)
        print ("Menu:")

        list_of_command = ["1) Add new album",\
                           "2) Find albums by artist",\
                           "3) Find albums by year",\
                           "4) Find musician by album",\
                           "5) Find albums by letter(s)",\
                           "6) Find albums by genre",\
                           "7) Calculate the age of all albums ",\
                           "8) Choose a random album by genre",\
                           "0) exit"]
        for command in list_of_command:
            print (command)

        print("")
        print("-" *80)

        choose = input("What do you want to do? Choose the number")

        if choose == "1":
            add_new_album()

        elif choose == "2":
            find_albums_by_artist(my_list)

        elif choose == "3":
            find_albums_by_year(my_list)

        elif choose == "4":
            find_musician_by_album(my_list)

        elif choose == "5":
            find_albums_by_letter(my_list)

        elif choose == "6":
            find_albums_by_genre(my_list)

        elif choose == "7":
            age_of_all_albums(my_list)

        elif choose == "8":
            random_album_by_genre(my_list)

        elif choose == "0":
            exit_by_0()


main()
