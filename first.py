
import math
import random
import datetime

while True:

    print("\n========== DAY 8 MENU ==========")
    print("1. Write File")
    print("2. Read File")
    print("3. Append File")
    print("4. Count Lines")
    print("5. Copy File")
    print("6. Safe Division")
    print("7. Age Validation")
    print("8. Math Module")
    print("9. Random Module")
    print("10. Date & Time")
    print("0. Exit")

    choice = input("Enter Choice : ")

    if choice == "0":
        print("Thank You")
        break

    elif choice == "1":

        try:
            name = input("Enter Your Name : ")

            with open("student.txt", "w") as file:
                file.write(name)

            print("Data Written Successfully")

        except Exception as e:
            print("Error :", e)

    
    # 2 Read File
    
    elif choice == "2":

        try:

            with open("student.txt", "r") as file:
                print("\nFile Content\n")
                print(file.read())

        except FileNotFoundError:
            print("File Not Found")

    
    # 3 Append File
   
    elif choice == "3":

        try:

            text = input("Enter New Data : ")

            with open("student.txt", "a") as file:
                file.write("\n" + text)

            print("Data Appended Successfully")

        except Exception as e:
            print("Error :", e)

    
    # 4 Count Lines
    
    elif choice == "4":

        try:

            with open("student.txt", "r") as file:

                lines = file.readlines()

                print("Total Lines :", len(lines))

        except FileNotFoundError:

            print("File Not Found")

    
    # 5 Copy File
    
    elif choice == "5":

        try:

            with open("student.txt", "r") as source:

                data = source.read()

            with open("backup.txt", "w") as destination:

                destination.write(data)

            print("File Copied Successfully")

        except FileNotFoundError:

            print("Source File Not Found")

   
    # 6 Safe Division
    
    elif choice == "6":

        try:

            a = int(input("First Number : "))
            b = int(input("Second Number : "))

            print("Answer =", a / b)

        except ZeroDivisionError:

            print("Cannot Divide By Zero")

        except ValueError:

            print("Invalid Number")

        finally:

            print("Program Finished")

   
    # 7 Custom Exception
    
    elif choice == "7":

        try:

            age = int(input("Enter Age : "))

            if age < 18:
                raise Exception("Not Eligible")

            print("Eligible")

        except Exception as e:

            print(e)

    
    # 8 Math Module
    
    elif choice == "8":

        number = int(input("Enter Number : "))

        print("Square Root :", math.sqrt(number))
        print("Power :", math.pow(number, 2))
        print("Factorial :", math.factorial(number))

    
    # 9 Random Module
    
    elif choice == "9":

        print("Random Number :", random.randint(1, 100))

    # 10 Date Time
    
    elif choice == "10":

        print("Current Date & Time")
        print(datetime.datetime.now())

    else:

        print("Invalid Choice")