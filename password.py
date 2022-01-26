# a beginner python project to check how valid a user's password is

def password():
    pass_word = input("Enter your password: ")
    too_much =("Characters are too many")
    exclamation =("Remove exclamation")
    comma =("Remove comma")
    back_slash = ("Invalid, Remove backslash")
    successful =("Your password was successfully set!")

    while True:
        if len(pass_word) > 8:
            print(too_much)
            break
        elif pass_word.count(",") > 0:
            print(comma)
            break
        elif pass_word.count("/") > 0:
            print(back_slash)
            break
        elif pass_word.count("!") > 0:
            print(exclamation)
            break
        else:
            print(successful)
            break



password()