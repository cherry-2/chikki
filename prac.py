x = [20, 30, 20, 30, 20, 40, 30]
freq = {}
count = 0
for item in x:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
for key, value in freq.items():
    count+=value/2
print("Pairs : ",int(count))



'''for i in range(0, len(ar)):
    if ar[i] == ar[i+1]:
        pair1.append(ar[i])


print(int(len(pair1))/2)'''