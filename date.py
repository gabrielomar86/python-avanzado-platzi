from datetime import datetime

def run():
    print(datetime.now().strftime('%d/%m/%Y : %H:%M:%S'))
    print(datetime.utcnow())
    print(datetime.utcfromtimestamp(0))

if __name__ == '__main__':
    run()