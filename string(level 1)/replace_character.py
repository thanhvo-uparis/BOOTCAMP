# 20 - Challenge: Replace a Character in a String

# String -> curr_char -> new_char -> output
# "Hello" -> "l" -> "s" -> "Hesso"
# "Python" -> "p" -> "a" -> "Python"

s = "Hello"
curr_char = "l"
new_char = "s"
new_string = ""

# --------------
# Solution 1
# --------------
# for char in s:
#     if char == curr_char:
#         new_string += new_char
#     else:
#         new_string += char

# print(new_string)

# --------------
# Solution 2
# Utilise method replace(curr_char, new_char)
# --------------
new_string = s.replace(curr_char, new_char)
print(new_string)

# --------------
# Old solution
# --------------
# Dans le cas que curr_char n'existe pas dans string s
# if curr_char not in s:
#     print(s)
# else:
#     for i in s:
#         if i == curr_char:
#             new_string += new_char
#         else:
#             new_string += i

# print(new_string)
