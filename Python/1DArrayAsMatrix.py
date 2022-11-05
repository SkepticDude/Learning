numbers = list(range(1,10))
print(numbers)

print("\nMatrix")
for i in range(3):
    print(numbers[i*3:(i+1)*3])


print("\nAccessing rows")

for i in range(3):
    print(numbers[i*3:(i+1)*3])


# print(numbers[0*3:1*3])
# print(numbers[1*3:2*3])
# print(numbers[2*3:3*3])

print("\nAccessing columns")

for i in range(3):
    print(numbers[i::3])

# print(numbers[0::3])
# print(numbers[1::3])
# print(numbers[2::3])

print("")