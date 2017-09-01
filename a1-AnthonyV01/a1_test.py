"""
' assignment1.py ' by Anthony Vincin
Date : 1/09/2017 
GitHub URL: https://github.com/AnthonyV01/AnthonyVincin_cp1404_assignment1
"""
song_file = "songs.csv"
open_song_file = open(song_file, 'a+')


def song_count(song_info):
    song_counter = 0
    for line in song_info:
        song_counter += 1
    print("{} songs loaded".format(song_counter))
    return song_counter


def list_song_contents(song_info):
    line_count = -1
    for line in song_info:
        line_count += 1
        split_song_info = line.split(',')
        if 'y' in line[-2:]:
            print("{}. * {:30} - {:25} ({})".format(line_count, split_song_info[0], split_song_info[1], split_song_info[2]))
        elif 'n' in line[-2:]:
            print("{}.   {:30} - {:25} ({})".format(line_count, split_song_info[0], split_song_info[1], split_song_info[2]))


def return_song_contents(read_file):
    read_song_file = read_file.readlines()
    line_count = 0
    song_info = read_song_file
    for line in read_file:
        line_count += 1
        song_info += line
    return song_info


def return_song_name(song_info):
    # add a input to be passed into this function so that the name of the song can be seen
    # ie. for trying to learn a learnt song #
    line_count = 0
    for line in song_info:
        line_count += 1
        each_song_name = line.split(',')
        print(each_song_name[0])


def learn_song(song_info):
    count = -1
    for i in list(song_info):
        count += 1
    valid_input = False
    while not valid_input:
        try:
            number = int(input("Enter the number of a song to mark as learned: \n >>>"))
            if number < 0 or number > count:
                valid_input = False
                print("Song number not in the list. The list goes up to {}".format(count))
            else:
                if ',y' in song_info[number]:
                    valid_input = True
                    print("Valid input. Song is now set to 'learned'.")
                if ',n' in song_info[number]:
                    valid_input = True
                    print("Song has already been learnt.")
        except ValueError:
            valid_input = False
            print("Invalid input; enter a valid number.")


def error_check(input):
        try:
            if input == "":
                print("Input can not be blank")
        except:
            print("Finished")


def add_song():
    valid_input = False
    new_song = []
    title_of_song = input("Title: ").strip()
    error_check(title_of_song)
    # artist_of_song = input("Artist: ").strip() #
    # year_of_song = input("Year: ").strip() #
    # status_of_song = input("Does this song need to be learnt? Yes ('y') or No ('n')") #


def main():
    read_file = open(song_file, 'r')
    song_info = return_song_contents(read_file)
    return_song_name(song_info)
    print("Songs To Learn 1.0 - by Anthony Vincin")
    song_counter = song_count(song_info)

    menu = """
    Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit
    """
    print(menu)
    choice = input(">>> ").upper().strip()
    while choice != "Q":
        if choice == "L":
            list_song_contents(song_info)
        elif choice == "A":
            # add error checking (refer to sample for info) #
            add_song()
        elif choice == "C":
            learn_song(song_info)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Have a nice day :)")
    open_song_file.close()
if __name__ == '__main__':
    main()
