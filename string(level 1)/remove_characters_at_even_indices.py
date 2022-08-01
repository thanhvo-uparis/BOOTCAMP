# 14 - Challenge: Remove Characters at Even Indices (even: so chan)

# Input -> Output
# "Coding" -> "oig"
# "Pizza" -> "iz"
# "Python" -> "yhn"
# "A" -> ""
# "" -> ""

s = "Pizzab"
# -----------
# Option 1
# -----------

# def remove_characters(myString):
#     new_string = ""
#     for i in range(len(myString)):
#         if i%2 != 0:
#             new_string += myString[i]

#     print(new_string)

# -----------
# Option 2
# -----------

def remove_characters(myString):
    new_string = ""
    for i in range(1, len(myString), 2):
        new_string += myString[i]
        
    print(new_string)

remove_characters("Pizaab")

