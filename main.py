import os
import argparse
import sys


def main_menu():
    print("\n\t\tDecMA\n\n\t\t1. Encrypt\n\t\t2. Decrypt\n\t\t3. Exit")


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def xor(data, key):
    modif_data = bytearray(len(data))
    for i in range(len(data)):
        modif_data[i] = data[i] ^ key[i % len(key)]
    return modif_data

def file_name_input():
    f_name = input("\n\t\tFile name: ")
    return f_name

def key_input():
    try:
        key_str = input("\n\t\tKey: ")
        if key_str == "" or len(key_str) <= 2:
            raise Exception("\n\t\t!!!The key must not be empty. Three or more characters")
        return key_str

    except Exception as e:
        clr()
        print(e)
        return

def file_process(f_name, key_str, f_mode):
    if key_str is None:
        return
    
    key = key_str.encode('utf-8')
    
    try:
        with open(f_name, "rb") as f_in:
            data = f_in.read()
        
        modif_data = xor(data, key)
        
        if f_mode == "encrypt":
            output_name = f"{f_name}.enc"
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            decrypt_dir = os.path.join(script_dir, "decrypt")
            if not os.path.exists(decrypt_dir):
                os.mkdir(decrypt_dir)
            output_name = os.path.join(decrypt_dir, os.path.basename(f_name.replace(".enc", "")))
            
        with open(output_name, "wb") as f_out:
            f_out.write(modif_data)
        
        clr()
        print(f"\n\t\tSuccesfully {f_mode}ed")
    
    except FileNotFoundError:
        print("\n\t\t File not found")


def main():
    
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description= "Python file encryption utility")
        parser.add_argument("--mode", choices=["encrypt", "decrypt"], required=True, type= str, help = "Program operating mode")
        parser.add_argument("--path", type= str, required=True, help="File location")
        parser.add_argument("--key", type= str, required=True, help="Key for encrypt or decrypt")
        args = parser.parse_args()
        
        if args.mode == "encrypt":
            file_process(args.path, args.key, args.mode)
            return
        elif args.mode == "decrypt":
            file_process(args.path, args.key, args.mode)
            return
    
    
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
                file_process(file_name_input(), key_input(), "encrypt")
            case 2:
                clr()
                file_process(file_name_input(), key_input(), "decrypt")
            case 3: return
            case _:
                clr()
                print("\n\t\t!!!Invalid number")


if __name__ == "__main__":
    main()