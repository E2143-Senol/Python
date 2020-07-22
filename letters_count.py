sentence = list(input("Give me a sentence!"))

length = len(sentence)

dict1 = {}

for i in range(length):
    count = 0
    for j in range(length):
        if sentence[i] == sentence[j]:
            count +=1
            dict1[sentence[i]] = count
        
print(dict1)