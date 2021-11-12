z = 5 # global
def my_func():
    z = 3 # local
    def my_func2():
        z = 2 # local
        print(z)
    my_func2()
    
    print(z)

def run():
    my_func()
    print(z)

if __name__ == '__main__':
    run()