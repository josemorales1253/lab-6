def encode(password):
    end_password = "".join(str((int(digit) + 3) % 10) for digit in password)
    return end_password



def main():
    encoded = None
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()