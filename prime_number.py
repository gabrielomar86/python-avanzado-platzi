def is_prime(number: int) -> bool:
    for x in range(2, number):
        if (number%x == 0):
            return False
    return True

def run():
    print(is_prime(9))

if __name__ == "__main__":
    run()