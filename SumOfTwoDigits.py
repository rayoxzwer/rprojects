print('This is demo calculator of sum of two characters\nof two digit number, type "end" if you wanna stop it.')
num = input("Give any 2 digit number you want: ")
while(num != "end"):
    first_character = num[0]
    second_character = num[1]
    print("Sum: " + str(int(first_character) + int(second_character)))
    num = input("Give any 2 digit number you want: ")
print("-------------\nThat's it\n-------------")