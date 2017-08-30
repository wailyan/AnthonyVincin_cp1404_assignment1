song_file = "songs_to_learn.csv"
open_song_file = open(song_file, 'a+')


def song_count():
    read_file = open(song_file, 'r')
    count = 0
    for line in read_file:
        count += 1
    print("{} songs loaded".format(count))


def read_song_contents():
    read_file = open(song_file, 'r')
    read_song_file = read_file.readline()
    line_count = 0
    song_name, song_artist, song_year, song_status = read_song_file.split(',')
    print("{}. ".format(line_count), song_name, song_artist, song_year, song_status)
    for line in read_file:
        line_count += 1
        song_name, song_artist, song_year, song_status = line.split(',')
        print("{}. ".format(line_count), song_name, song_artist, song_year, song_status)
    return song_name, song_artist, song_year, song_status


def main():
    print("Songs To Learn 1.0 - by Anthony Vincin")
    song_count()
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
            print("Enter the number of a song to mark as learned: ")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Have a nice day :)")
    open_song_file.close()
main()
