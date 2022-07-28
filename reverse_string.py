# 9 - Challenge: Reverse a String

# Input -> Output
# "Hello" -> "olleH"
# "Wo" -> "oW"
# "" -> ""

# def reverse(word):
#     new_word = ""
#     longeur = len(word)
#     if longeur == 0:
#         print("")
#     else:
#         for i in range(longeur):
#             new_word += word[longeur -1 -i]
#         print(new_word)

# reverse("")

s = "heLLo"
new_word = "".join(reversed(s))
print(new_word)
