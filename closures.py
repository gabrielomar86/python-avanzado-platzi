def make_repeater_of(number):
    def repeater(word):
        assert type(word) == str, 'Pilas solo string se necesita'
        return word * number

    return repeater

def run():
    repeat5 = make_repeater_of(5)
    word = input('ingrese dato:')
    print(repeat5(word))

if __name__ == "__main__":
    run()