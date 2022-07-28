# 7- Challenge: Print the Character at a Specific Index

# String -> i -> Output
# "Hello" -> 2 -> "l"
# "Pizza" -> 4 -> "a"
# "" -> 3 -> "Empty String"
# "World" -> 15 -> "i is out of range"

def character(word, position):
    if word == "":
        print("Empty String")
    elif position < len(word):
        print(word[position])
    else:
        print("i is out of range")


character("hi", 5)
