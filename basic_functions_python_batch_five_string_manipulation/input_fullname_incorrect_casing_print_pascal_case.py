# ask the user to input their fullname in incorrect casing.
user_fullname = input("Enter your full name (incorrect casing): ") 

# make a condition that will make the fullname in proper casing and remove the spacing.
pascal_case = user_fullname.title().replace(" ", "") 

# print the fullname in pascal case.