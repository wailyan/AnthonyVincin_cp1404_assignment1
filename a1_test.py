song_file = "songs_to_learn.csv"
open_song_file = open(song_file, 'a+')


def song_count():
    read_file = open(song_file, 'r')
    song_counter = 0
    for line in read_file:
        song_counter += 1
    print("{} songs loaded".format(song_counter))
    return song_counter


def read_song_contents():
    read_file = open(song_file, 'r')
    read_song_file = read_file.readlines()
    line_count = 0
    song_info = read_song_file
    # print("{}. ".format(line_count), song_info) #
    for line in song_info:
        # print("LINE [-2:] (yes or no check)",line[-2:]) #
        line_count += 1
        split_song_info = line.split(',')
        print("{}. ".format(line_count), split_song_info, "\n")
        if 'y' in line[-2:]:
            print("YES, song learnt \n")
        elif 'n' in line[-2:]:
            print("NO, song not learnt \n")
    return song_info, read_file, line_count


def return_song_contents():
    read_file = open(song_file, 'r')
    read_song_file = read_file.readlines()
    line_count = 0
    song_info = read_song_file
    for line in read_file:
        line_count += 1
        song_info += line
    return song_info, read_file, line_count


def main():
    print("Songs To Learn 1.0 - by Anthony Vincin")
    song_counter = song_count()
    song_info, read_file, line_count = return_song_contents()
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
            read_song_contents()
        elif choice == "A":
            # add error checking (refer to sample for info) #
            print("Song name: ")
        elif choice == "C":
            count = -1
            reverse_count = 0
            for i in list(song_info):
                count += 1
                reverse_count += 1
                print("Song {} status: ".format(song_info[count:reverse_count]), i[-2:])
            try:
                number = int(input("Enter the number of a song to mark as learned: "))
                if number < 0 or number > song_counter:
                    print("Song number not in the list. The list goes up to {}".format(song_counter))
                else:
                    print("Valid input. Song is now set to 'learned'.")
            except ValueError:
                print("Not a valid number")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Have a nice day :)")
    open_song_file.close()
main()
