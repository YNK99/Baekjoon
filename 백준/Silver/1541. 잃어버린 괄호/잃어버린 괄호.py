sic = input()
S = 0
nums = sic.replace("+",  ' + ').replace("-", " - ").split(" ")
last = "+"

for num in nums:
    if num == "+":
        continue
    elif num == "-":
        last = "-"
    else:
        S += int(last + num)

print(S)