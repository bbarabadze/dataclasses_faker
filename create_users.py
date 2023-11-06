from faker import Faker
from random import randrange

fake = Faker()

with open("users.txt", "w") as f:
    for _ in range(100001):
        name = fake.name()
        age = randrange(13, 113)
        gender = randrange(0, 50)
        f.write(f"{name},{age},{gender}\n")