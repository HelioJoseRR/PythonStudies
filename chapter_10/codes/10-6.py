def sum(first_number, second_number):
    return first_number + second_number

while True:
    
    try:
        f_num = int(input("Enter the first number: "))
    except ValueError:
        print("Please enter a number!")
        continue

    try:
        s_num = int(input("Enter the second number: "))
    except ValueError:
        print("Please enter a number!")
        continue   

    print(sum(f_num, s_num))

    if input("Do you want to continue? (y/n): ") == 'n':
        break