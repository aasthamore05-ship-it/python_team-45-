print("1.Prime Number\n2.perfect Number\n3.Palindrome Number")
ch=int(input("Enter your choice:"))
match ch:
    case 1:
        num = int(input("Enter a number: "))

        if num <= 1:
            print("Not Prime")
        else:    
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print("Prime")
            else:
                print("Not Prime")

    case 2:
        num = int(input("Enter a number: "))

        total = 0

        for i in range(1, num):
            if num % i == 0:
                total+= i
        if total== num:
            print(num,"is a Perfect Number")
        else:
            print(num, "is Not a Perfect Number")

    case 3:
        num = input("Enter a number: ")

        if num == num[::-1]:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    case _:
        print("Invalid choice")

    