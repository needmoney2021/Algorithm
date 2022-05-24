def is_prime_number(number: int) -> bool:

    for i in range(2, int(number ** 0.5) + 1):
        if number % 2 == 0:
            return False
    return True


if __name__ == "__main__":
    numbers = [7, 11, 1231234]
    for number in numbers:
        print(is_prime_number(number))
