def decorator_con_hongo(func):
    def wrapper():
        func()
        print('con hongo')
    return wrapper

@decorator_con_hongo
def mario_bross():
    print('yo soy mario')

def run():
    mario_bross()
    
if __name__ == "__main__":
    run()