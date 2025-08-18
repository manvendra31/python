def tabel(i):
    for a in range(1, 11):   # 1 to 10
        c = i * a
        print(f"{i} x {a} = {c}")

x = int(input("Enter the number you want the multiplication table of:\n"))
tabel(x)
