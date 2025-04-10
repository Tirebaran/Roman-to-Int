import os 

def int_to_rom(number):
    alp = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}
    try:
        answer = ""
        cnt = 0 
        num = [int(number[i]) for i in range(len(number))]
        if num[0] == 0:
            return 0
        else:
            while len(num):
                if num[0] != 4 and num[0] != 9:
                    if num[0] < 4:
                        answer += alp[10 ** (len(num) - 1)] * num[0]
                    else:
                        answer += alp[5 * 10 ** (len(num) - 1)] + alp[10 ** (len(num) - 1)] * (num[0] - 5)
                elif num[0] == 4:
                    answer += alp[10 ** (len(num) - 1)] + alp[5 * 10 ** (len(num) - 1)]
                else:
                    answer += alp[10 ** (len(num) - 1)] + alp[10 * 10 ** (len(num) - 1)]
                num.pop(0)
                cnt += 1
        return answer
    
    except (KeyError, ValueError):
        print("Something went wrong! Try again!")
        number = input("Enter a number lower than 3999: ")
        return int_to_rom(number)

def rom_to_int(number):
    try:
        answer = 0
        alp = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
        if "CM" in number: answer += 900; number = number.replace("CM", "")
        if "CD" in number: answer += 400; number = number.replace("CD", "")
        if "XC" in number: answer += 90; number = number.replace("XC", "")
        if "XL" in number: answer += 40; number = number.replace("XL", "")
        if "IX" in number: answer += 9; number = number.replace("IX", "")
        if "IV" in number: answer += 4; number = number.replace("IV", "")

        for i in number:
            answer += alp[i]

        return answer
    except KeyError:
        print("Something went wrong! Try again!")
        number = input("Enter number between I and MMMCMXCIX (3999): ")
        return rom_to_int(number)
        
def wait():
    input("\nPress any key to continue...")


while True:
        os.system("cls")  
        print("\nMenu:")
        print("1. Int to Roman")
        print("2. Roman to Int")
        print("3. Quit")
        choice = input("Select: ")

        match choice:
            case "1":
                os.system("cls")
                number = input("Enter a number lower than 3999: ")
                print("Your answer is:", int_to_rom(number))
                wait()
            case "2":
                os.system("cls")
                number = input("Enter number between I and MMMCMXCIX (3999): ")
                print("Your answer is:", rom_to_int(number))
                wait()
            case "3":
                os.system("cls")
                print("Bye!")
                break
            case _:
                os.system("cls")
                print("Wrong key. Try again!")
                wait()



