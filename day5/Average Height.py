heights = input("Input a list of student heights ").split(" ")

sum = 0

for i in range(0,len(heights)):
    sum+= int(heights[i])

print(round(sum/len(heights)))