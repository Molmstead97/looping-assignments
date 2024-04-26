def char_count_while(target, c):
    count = 0
    index = 0
    while index < len(target):
        if target[index] == c:
            count += 1
        index += 1
    return count

def char_count_for(target, c):
    count = 0
    for index in range(len(target)):
        if target[index] == c:
            count += 1
    return count

def char_count_foreach(target, c):
    count = 0
    for char in target:
        if char == c:
            count += 1
    return count


string = "Batman vs Superman"
char = "m"

char_count_while = char_count_while(string, char)
char_count_for = char_count_for(string, char)
char_count_foreach = char_count_foreach(string, char)

print(f"\nWhile loop count: {char_count_while}")
print(f"\nFor loop count: {char_count_for}")
print(f"\nFor each loop: {char_count_foreach}")

