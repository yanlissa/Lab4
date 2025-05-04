from generator.genpass import generate_password

if __name__ == "__main__":
    lenght = int(input("Введите длину пароля: "))
    up, low, dig, symb = input("Введите характеристики: ").split()
    
    up = bool(int(up))
    low = bool(int(low))
    dig = bool(int(dig))
    symb = bool(int(symb))
    
    pwd = generate_password(lenght, up, low, dig, symb)
    print("Сгенерированный пароль", pwd)