# Armstrong Number Example
# 153 = 1^3 + 5^3 + 3^3

num = 153
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

print("Original Number:", num)
print("Calculated Sum:", sum)

if sum == num:
    print("Armstrong Number ✅")
else:
    print("Not Armstrong Number ❌")