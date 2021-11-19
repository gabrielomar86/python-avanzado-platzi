from datetime import datetime
import pytz

def timezone(timezone_name):
    time = pytz.timezone(timezone_name)
    date = datetime.now(time)
    print(timezone_name, ": ", date.strftime("%d/%m/%Y %H %M %S"))

def run():
    timezone('America/Bogota')
    timezone('America/Caracas')
    
if __name__ == '__main__':
    run()