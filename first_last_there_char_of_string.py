# 11 - Challenge: First and Last Three Characters of a String

# Input -> Output: 
# "Blue" -> ""
# "Wonderful" -> "Wonful"
# "Amazing" -> "Amaing"

s = "codingame"
# len = 9

def first_and_last(myString):
    longeur = len(myString)
    first_string = ""
    last_string = ""
    if longeur < 6:
        print("")
    else:
        # pour 3 premiers caracteres , l'index compte de 0 à 2
        for i in range(3):
            first_string += myString[i]
        # pour 3 derniers caracteres, index: 0 1 2 -> len - index - 1: 8 7 6
        for i in range(3):
            # obtenir: "ema"
            last_string += myString[longeur - 1 -i]
        
        # reverse string old
        last_string_reverse = "".join(reversed(last_string))
        
        new_string = first_string + last_string_reverse
        print(new_string)
        
## Exemple
# s1 = "test"
# new_s = s1.join("programme")

# s2 = "".join("test programme")
# print(s2)

first_and_last("hello1p")