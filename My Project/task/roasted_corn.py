user_input = 'google.com'
my_dict1 = {}
for char in user_input:
    if char not in my_dict1:
        my_dict1[char] = 1
    else:
        my_dict1[char] += 1
print(my_dict1)

print({k: user_input.count(k) for k in user_input})
