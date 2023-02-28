import random
import string

def generate_password():
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    random_source = string.ascii_letters + string.digits + string.punctuation
    for i in range(14):
        password += random.choice(random_source)

    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)
    return password

print(generate_password())