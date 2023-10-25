def encode(password):
    end_password = "".join(str((int(digit) + 3) % 10) for digit in password)
    return end_password


def decode(password):
    password = "".join(str((int(digit) - 3) % 10) for digit in password)
    return password


def main():
    encoded = None
    while True:
        password = input('Please enter the password you would like to encode/decode: ')
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        response = int(input('Which option would you like to choose? '))
        if response == 1:
            print(encode(password))
        if response == 2:
            print(decode(password))
        if response == 3:
            exit()


if __name__ == '__main__':
    main()