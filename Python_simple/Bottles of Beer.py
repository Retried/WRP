n = 3
for i in range(n, -1, -1):
    if i <= 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {n} bottles of beer on the wall...")
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down, pass it around, {i-1} bottles of beer on the wall...")
