

shoplist = []
while True:
    item = input("Enter shopping items: ")
    if len(item) == 0:
        break
shoplist.append(item)
print(shoplist)
