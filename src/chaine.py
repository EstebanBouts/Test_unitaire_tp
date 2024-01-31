def miroir(input_str):
    return input_str[::-1]


def palindrome(input_str):
    if input_str == input_str[::-1] and input_str != "":
        return input_str + " Bien dit"
    else:
        return input_str

def bonjour(input_str):
    return "Bonjour " + input_str
