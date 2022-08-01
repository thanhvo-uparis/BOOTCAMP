# 14 - Challenge: Remove Characters at Even Indices (even: so chan)

# Input -> Output
# "Coding" -> "oig"
# "Pizza" -> "iz"
# "Python" -> "yhn"
# "A" -> "A"

s = "A"

def remove_characters(myString):
    new_string = ""
    longeur = len(myString)
    if longeur == 0 or longeur == 1:
        print(myString)
    else:
        for i in range(longeur):
            if (i % 2) != 0:
                new_string += myString[i]
    
    print(new_string)

remove_characters("A")
