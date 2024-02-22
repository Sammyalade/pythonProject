words = "the palace is a few miles away from the village but going to the palace to see startups is cool and fun"

my_dict = {}

for word in words.split():
    for letter in word:
        my_dict[word] += 1

print(my_dict)
