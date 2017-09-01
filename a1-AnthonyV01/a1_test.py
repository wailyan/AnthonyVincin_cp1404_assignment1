"""
' assignment1.py ' by Anthony Vincin
Date : 1/09/2017 
GitHub URL: https://github.com/AnthonyV01/AnthonyVincin_cp1404_assignment1
GitHub URL (private repo): https://github.com/CP1404-2017-2/a1-AnthonyV01

Pseudocode for two functions:
LOAD SONG:
return_song_contents(read_file):
    open file to read, this value is passed into the function
    count is set to 0
    song_info = list
    for each line in file
        count = count + 1
        song_info = song_info + line
    return song_info, count
    
COMPLETE A SONG:
learn_song(song_info, count):
    input = song to be learnt
    if input not on list
        invalid input
    elif 
        song has already been learnt
    else
        song is now learnt
"""
song_file = "songs.csv"
open_song_file = open(song_file, 'r')


def list_song_contents(song_info):
    """
    Lists each song in addition to the status of the song (learnt or un-learnt)
    """
    for i in range(0, len(song_info), 1):
        print("{:2} ".format(i), end="")
        if song_info[i][len(song_info[i])-1] == 'y':
            print(" * ", end="")
        else:
            print("   ", end="")
        print("{:30} - {:25} ({})".format(song_info[i][0], song_info[i][1], song_info[i][2]))


def return_song_contents(read_file):
    """
    Takes the read file as a parameter and appends each of the songs to the list (song_info)
    """
    song_counter = 0
    song_info = []
    for line in read_file:
        song_counter += 1
        line = line.strip("\n")
        each_song = line.split(',')
        song_info.append(each_song)
    return song_info, song_counter


def learn_song(song_list, song_counter):
    """
    Changes the status of a song in the list (learnt or not), does error checking within the function
    """
    valid_input = False
    number = 0
    while not valid_input:
        try:
            number = int(input("Enter the number of a song to mark as learned: \n >>>"))
            if number < 0:
                print("Invalid song number. Number must be >= 0")
            elif number > song_counter:
                print("Song number not in the list. The list goes up to {}".format(song_counter-1))
            else:
                valid_input = True
        except ValueError:
            valid_input = False
            print("Invalid input; enter a valid number.")
    if song_list[number][len(song_list[number]) - 1] == 'y':
        song_list[number][len(song_list[number]) - 1] = 'n'
        print(song_list[number][0], "learned.")
    else:
        print("Song already learnt.")


def add_song(song_info, song_counter):
    """
    Takes user input to append a song to the list, does error checking within the function
    """
    new_song = []
    title_of_song = input("Title: ").strip()
    while len(title_of_song) < 1:
        print("Input can not be blank")
        title_of_song = input("Title: ").strip()
    artist_of_song = input("Artist: ").strip()
    while len(artist_of_song) < 1:
        print("Input can not be blank")
        artist_of_song = input("Artist: ").strip()
    year_of_song = input("Year: ").strip()
    while len(year_of_song) < 1:
        print("Input can not be blank")
        year_of_song = input("Year: ").strip()
    if new_song in song_info:
        print("Song already in list ")
    else:
        new_song.append(title_of_song)
        new_song.append(artist_of_song)
        new_song.append(year_of_song)
        new_song.append('y')
        song_info.append(new_song)
        song_counter += 1
    return song_counter


def main():
    """
    Takes user input to the menu, decides which path the user takes, opens and closes the files for reading/writing
    """
    read_file = open(song_file, 'r')
    song_info, song_counter = return_song_contents(read_file)
    read_file.close()
    print("Songs To Learn 1.0 - by Anthony Vincin")
    print("{} songs loaded".format(song_counter))
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
            song_counter = add_song(song_info, song_counter)
        elif choice == "C":
            learn_song(song_info, song_counter)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Have a nice day :)")
    write_song_file = open(song_file, 'w')
    for line in song_info:
        print("{},{},{},{}".format(line[0], line[1], line[2], line[3]), file=write_song_file)
    open_song_file.close()
    read_file.close()
if __name__ == '__main__':
    main()
