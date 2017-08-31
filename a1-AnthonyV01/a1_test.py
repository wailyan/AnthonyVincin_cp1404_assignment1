song_file = "songs.csv"
open_song_file = open(song_file, 'a+')


def song_count():
    read_file = open(song_file, 'r')
    song_counter = 0
    for line in read_file:
        song_counter += 1
    print("{} songs loaded".format(song_counter))
    return song_counter


def list_song_contents():
    read_file = open(song_file, 'r')
    read_song_file = read_file.readlines()
    line_count = -1
    song_info = read_song_file
    for line in song_info:
        line_count += 1
        split_song_info = line.split(',')
        if 'y' in line[-2:]:
            print("{}. * {:30} - {:25} ({})".format(line_count, split_song_info[0], split_song_info[1], split_song_info[2]))
        elif 'n' in line[-2:]:
            print("{}.   {:30} - {:25} ({})".format(line_count, split_song_info[0], split_song_info[1], split_song_info[2]))


def return_song_contents():
    read_file = open(song_file, 'r')
    read_song_file = read_file.readlines()
    line_count = 0
    song_info = read_song_file
    for line in read_file:
        line_count += 1
        song_info += line
    return song_info


def return_song_name():
    # add a input to be passed into this function so that the name of the song can be seen
    # ie. for trying to learn a learnt song #
    read_file = open(song_file, 'r')
    read_song_file = read_file.readlines()
    line_count = 0
    for line in read_song_file:
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


def main():
    return_song_name()
    print("Songs To Learn 1.0 - by Anthony Vincin")
    song_counter = song_count()
    song_info = return_song_contents()
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
            list_song_contents()
        elif choice == "A":
            # add error checking (refer to sample for info) #
            print("Song name: ")
        elif choice == "C":
            learn_song(song_info)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Have a nice day :)")
    open_song_file.close()
main()
