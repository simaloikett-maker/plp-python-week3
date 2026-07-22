age = int(input("Enter your age: "))

is_adult = age >= 18

print(is_adult)

if is_adult:
    print("Ticket Price: KSh 500")
else:
    print("Ticket Price: KSh 250")