try:
    user_input = int(input("Enter a number: "))
    sum_of_even = 0
    sum_of_odd = 0
    for number in range(user_input):
        if number % 2 == 0:
            sum_of_even += number
            continue
        sum_of_odd += number

    print(f"The sum of even is {sum_of_even} and the sum of odd is {sum_of_odd}")

    print(f"The sum of even is {sum(filter(lambda x: x % 2 == 0, range(user_input)))} and the sum of odd is "
          f"{sum(filter(lambda x: x % 2 != 0, range(user_input)))}")
except ValueError:
    print("Please use your fucking brain and try again later")
except TypeError:
    print("Please use your brain and try again later")

