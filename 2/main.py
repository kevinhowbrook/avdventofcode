text_file = open("input.txt", "r")
lines = text_file.read().splitlines()


def validator(line=None):
    print(line)
    return False


for line in lines:
    print(validator(line))
