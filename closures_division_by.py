def make_division_by(divisor):
    def repeater(number):
        assert divisor != 0, 'La division para 0 no se encuentra establecida'
        return number / divisor
   
    return repeater

def run():
    divisorBy3 = make_division_by(3)
    number = int(input('ingrese dato:'))
    print(divisorBy3(number))

if __name__ == "__main__":
    run()