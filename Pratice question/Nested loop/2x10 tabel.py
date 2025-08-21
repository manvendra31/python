a = int(input("Enter the number up to which you want the table:\n"))

def tabel(n):  # Take 'n' as a parameter
    for i in range(1, n+1):        # Rows
        for j in range(1, n+1):    # Columns
            print(i*j, end="\t")   # \t for better alignment
        print()                    # Newline after each row

def condition(n):
    if n>=10:
        tabel(n)
    else:
        print("Enter the number grater the 10")    


condition(a)