def fibonachi(n):
    if n == 0:
        return "Incorrect reference"

    elif n == 1 or n == 2:
        return 1
    
    else:
        return fibonachi(n-1) + fibonachi(n-2)

count = int(input("Enter the quantity: "))

for i in range(1,count + 1):
    print(f"{fibonachi(i)}",)