def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Бөлгіш 0 болмауы тиіс!"

print("Операциялар:")
print("1. Қосынды")
print("2. Азайту")
print("3. Көбейту")
print("4. Бөлу")

while True:
    operation = input("Қандай операцияны таңдаасыз (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        san1 = float(input("Бірінші санды енгізіңіз: "))
        san2 = float(input("Екінші санды енгізіңіз: "))

        if choice == '1':
            print(f"{san1} + {san2} = {add(san1, san2)}")
        elif choice == '2':
            print(f"{san1} - {san2} = {subtract(san1, san2)}")
        elif choice == '3':
            print(f"{san1} * {san2} = {multiply(san1, san2)}")
        elif choice == '4':
            print(f"{san1} / {san2} = {divide(san1, san2)}")
    else:
        print("Қате таңдау!")

    next_calculation = input("Тағы бір есептеу жасау керек пе? (иә/жоқ): ")
    if next_calculation.lower() != 'иә':
        break





