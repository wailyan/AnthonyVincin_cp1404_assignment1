song_file = "songs_to_learn.csv"
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
    read_file = open(song_file, 'r')
    read_song_file = read_file.readlines()
    line_count = 0
    for line in read_song_file:
        line_count += 1
        # print(line.split(',')) #
        each_song_name = line.split(',')
        # print(each_song_name[0:1]) #
        print(each_song_name[0])


def learn_song(song_info):
    count = -1
    reverse_count = 0
    for i in list(song_info):
        count += 1
        reverse_count += 1
        # print("Song {} status: ".format(song_info[count:reverse_count]), i[-2:]) #
        each_song_status = i.split(',')
        print(each_song_status[3])
    try:
        number = int(input("Enter the number of a song to mark as learned: "))
        if number < 0 or number > count:
            print("Song number not in the list. The list goes up to {}".format(count))
        else:
            if 'y' in song_info[-2:]:
                print("Valid input. Song is now set to 'learned'.")
            if 'n' in song_info[-2:]:
                print("Song has already been learnt!")
    except ValueError:
        print("Not a valid number")


def main():
    return_song_name()
    print("Songs To Learn 1.0 - by Anthony Vincin")
    song_counter = song_count()
    song_info = return_song_contents()
    print("SONG INFO:",song_info)
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
