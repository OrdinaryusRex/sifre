import random

count = 0
password = []

servicename = input("\nService: ")
username = input("Username: ")
length = input("Number of characters: ")
length = int(length)

while count < length:
    rand = random.randint(0, 3)

    if rand == 0:
        b = int(random.randint(97, 123))
        password.append(b)

    elif rand == 1:
        b = random.randint(65, 91)
        password.append(b)

    elif rand == 2:
        b = random.randint(48, 58)
        password.append(b)

    elif rand == 3:
        r = random.randint(0, 2)
        if r == 0:
            b = random.randint(33, 48)
            password.append(b)
        elif r == 1:
            b = random.randint(91, 97)
            password.append(b)
        elif r == 2:
            b = random.randint(123, 126)
            password.append(b)

    count += 1

pw = "".join([chr(e) for e in password])

with open(servicename + "-sifre.txt", 'w') as foo:
    foo.write(username + "  :  " + pw)
print("\n" + pw + "\n")