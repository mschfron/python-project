# filename: Salvador_e1.py
# author: Ronald Salvador 
# description: This is a python program that prints the contents of a dictionary in a specific format

message = "I am  {}.\n" + \
        "My Spirit animal is {},\n" + \
        "because {}.\n" + \
        "When not in school, I love to {}.\n" + \
        "I dream of being a/an {} in the future "


data = {"Name":"Ronald Salvador","Spirit Animal":"Dragon",
"Reason":"I love adventures more than you do","Hobby": "Biking","Profession":"Engineer"}


print (message.format( \
    data["Name"], \
    data["Spirit Animal"],\
    data["Reason"],\
    data["Hobby"],\
    data["Profession"]))     

    