import random
name = input("Enter name: ")
x = "y"
while x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
   
    number = random.randint(1,8)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    *   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| *    * |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    *   |")
        print("|    *   |")
        print("|    *   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| *    * |")
        print("|        |")     
        print("| *    * |")
        print("----------")
    if number == 5:
        print("----------")
        print("| *    * |")
        print("|    *   |")
        print("| *    * |")
        print("----------")
    if number == 6:
        print("----------")
        print("| *    * |")
        print("| *    * |")
        print("| *    * |")
        print("----------")
    if number == 7:
        print("----------")
        print("| *    * |")
        print("| *  * * |")
        print("| *    * |")
        print("----------")
    if number == 8:
        print("----------")
        print("| *  * * |")
        print("| *    * |")
        print("| *  * * |")
        print("----------")
        
    x = input("Press Y to roll again:  ")
    


