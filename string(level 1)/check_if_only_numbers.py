# 16 - Challenge: Check if a String Only Contains Numbers

def only_numbers(myString):
    list_integers  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    check = True
    for i in range(myString):
        if i not in list_integers:

