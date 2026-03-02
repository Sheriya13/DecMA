import os


def main_menu():
    print("\n\t\tDecMA\n\n\t\t1. Encrypt\n\t\t2. Decrypt\n\t\t3. Exit")


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def xor(data, key):
    modif_data = bytearray(len(data))
    for i in range(len(data)):
        modif_data[i] = data[i] ^ key[i % len(key)]
    return modif_data


def encrypt():
    f_name = input("\n\t\tFile name: ")

    try:
        key_str = input("\n\t\tKey: ")
        if key_str == "" or len(key_str) <= 2:
            raise Exception("\n\t\t!!!The key must not be empty. Three or more characters")

    except Exception as e:
        clr()
        print(e)
        return

    key = key_str.encode('utf-8')

    try:
        with open(f_name, "rb") as file_source:
            data = file_source.read()
            modif_data = xor(data, key)
            try:
                with open(f"{f_name}.enc", "wb") as file_source:
                    file_source.write(modif_data)
            except FileNotFoundError: print("\n\t\tFile not found")
            clr()
            print("\n\t\tSuccesfull encrypted")
    except FileNotFoundError: print("\n\t\tFile not found")


def decrypt():
    f_name = input("\n\t\tFile name: ")

    try:
        key_str = input("\n\t\tKey: ")
        if key_str == "" or len(key_str) <= 2:
            raise Exception("\n\t\t!!!The key must not be empty. Three or more characters")

    except Exception as e:
        clr()
        print(e)
        return

    key = key_str.encode('utf-8')

    try:
        with open(f_name, "rb") as file_source:
            enc_data = file_source.read()
            modif_data = xor(enc_data, key)

            if not os.path.exists("decrypt"):
                os.mkdir("decrypt")
            output_name = f_name.replace(".enc", "")

            try:
                with open(f"decrypt\\{output_name}", "wb") as file_source:
                    file_source.write(modif_data)
            except FileNotFoundError: print("\n\t\tFile not found")
        clr()
        print("\n\t\tSuccesfull decrypted")
    except FileNotFoundError: print("\n\t\tFile not found")


def main():
    while True:
        main_menu()
        while True:
            try:
                so = int(input("\n\t\tSo: "))
                break
            except ValueError: 
                clr()
                print("\n\t\t!!!Invalid value")
                main_menu()

        match so:
            case 1:
                clr()
                encrypt()
            case 2:
                clr()
                decrypt()
            case 3: break
            case _:
                clr()
                print("\n\t\t!!!Invalid number")


if __name__ == "__main__":
    main()