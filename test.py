user_phrase = str(input("Enter any text phrase: "))
output_file = "test.txt"
out_file = open(output_file, 'a+')
print(user_phrase, file=out_file)
out_file.close()

open_file = open(output_file, 'r')
read_file = open_file.read()
print("You entered: {}".format(read_file))