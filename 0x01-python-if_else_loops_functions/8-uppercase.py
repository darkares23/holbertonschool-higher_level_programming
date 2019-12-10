def uppercase(str):
    for char in str:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            char = ord(char) - 32
            char = ord(char)
        print("{}".format(char), end="")
    print("")
