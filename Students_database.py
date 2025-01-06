

student_name_list = ["Sophie", "Hana", "Abe", "Andrew"]
student_hometown_list = ["Italy", "Yemen", "Argentina", "America"]
student_fav_food = ["Pizza", "Steak", "Flafel", "Spaghetti"]

while True:

    print("Welcome! Which student would you like to learn more about? Enter a number 1-4:")
    student_num = int(input("> "))

    if 0 < student_num < 5:
        print(f"Student {student_num} is {student_name_list[student_num - 1]}. What would you like to know?")
        print("Enter 'hometown' or 'favorite food':")
        more_info = (input("> "))
        valid_info_selection = False
        while not valid_info_selection:
            if more_info == "hometown":
                print(f"{student_name_list[student_num - 1]} is from {student_hometown_list[student_num - 1]}")
                valid_info_selection = True
# This part right here has one of the extended challenges: that is to make 'Food' an option
            elif more_info == "favorite food" or more_info == "food":
                print(f"{student_name_list[student_num - 1]}'s favorite food is {student_fav_food[student_num - 1]}")
                valid_info_selection = True
            else:
                print("That category does not exist. Please try again. Enter 'hometown' or 'favorite food':")
                more_info = input("> ")
                valid_info_selection = False
    else:
        print("There is no student with that number. Please try again.")

    print("Would you like to learn about another student? Enter 'y' or 'n'")
    to_learn_more = input("> ")
    if to_learn_more == "y" or to_learn_more == "yes":
        print("OK.")
    elif to_learn_more == "n" or to_learn_more == "no":
        print("Thanks.")
        break
    else:
        print("Your input is invalid, Goodbye!")
        break

# EXTENDED CHALLENGE TWO
# To show list of students to the user.

print("Would you like to see the list of students? 'yes' or 'no'" )
show_list = input("> ")
if show_list == "yes":
    print(student_name_list)
else:
    pass