import time

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

def run():
    number = int(input("Ingrese numero: "))
    for i in fibonacci(number):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    run()
    