# Break will end a loop entirely
for i in range(0, 5):
    if i == 3:
        break
    print(i)

print()

# Continue will skip the current loop
for i in range(0, 5):
    if i == 3:
        continue
    print(i)

print()

# Pass will do nothing and continue on
for i in range(0, 5):
    if i == 3:
        pass
    print(i)