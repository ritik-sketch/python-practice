'''
s = "Geeks"
for i in s:
    print(i)
'''
# Prints all letters except 'e' and 's'
'''
for i in 'geeksforgeeks':

    if i == 'e' or i == 's':
        continue
    print(i)
'''
'''
for i in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if i == 'e' or i == 's':
        break

print(i)
print("\n")


li = ["eat", "sleep", "repeat"]

for i, j in enumerate(li):
    print (i, j)
    print("\n")

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
    print("\n")



for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        print("\n")

'''

a = ["shirt", "sock", "pants", "sock", "towel"]
b = []
for i in a:
    if i == "sock":
        continue
    else:
        print(f"Washing {i}")
b.append("socks")
print(f"Washing {b}")