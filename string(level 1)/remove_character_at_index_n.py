# 18- Challenge: Remove nth Character from a String

s = "World"
n = 2

new_string = ""
for i in range(len(s)):
    if i != n:
        new_string += s[i]
    
print(new_string)

