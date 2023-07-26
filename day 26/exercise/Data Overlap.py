s1 = set(open("./file1.txt", 'r').readlines())
s2 = set(open("./file2.txt", 'r').readlines())

result = [int(n.strip('\n')) for n in (s1 & s2)]  # just to get the integer values.

# Write your code above 👆

print(result)
