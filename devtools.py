import sys

def switch(params):
    if len(params) > 1:
        if params[1] == "--hello":
            return "Hello World!"
        if params[1] == "--pswdchk":
            return "passwor check call here!"
        else:
            return "Please input a valid command."
    else:
        return "No command inserted."


# Parameter array.
params = sys.argv
print(switch(params))
