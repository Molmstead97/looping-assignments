def reverse_while(s):
    reverse_string = ''
    index = len(s) - 1
    while index >= 0:
        reverse_string += s[index]
        index -= 1
    return reverse_string

def reverse_for(s):
    reverse_string = ''
    for index in range(len(s) - 1, -1, -1):
        reverse_string += s[index]
    return reverse_string

def reverse_foreach(s):
    reverse_string = ''
    for char in s:
        reverse_string = char + reverse_string
    return reverse_string


string = "Krungthepmahanakhon Amonrattanakosin Mahintharayutthaya Mahadilokphop Noppharatratchathaniburirom Udomratchaniwetmahasathan Amonphimanawatansathit Sakkathattiyawitsanukamprasit"

reverse_while = reverse_while(string)
reverse_for = reverse_for(string)
reverse_foreach = reverse_foreach(string)

print(f"\nWhile loop: {reverse_while}")
print(f"\nFor loop: {reverse_for}")
print(f"\nFor each loop: {reverse_foreach}")
