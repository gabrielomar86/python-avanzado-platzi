def main():
    
    a = 1
    
    def nested():
        print(a)
        
    return nested()

def run():
    my_func = main()
    my_func()

if __name__ == "__main__":
    run()