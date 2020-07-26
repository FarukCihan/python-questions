word = input("Please enter your word : ")
count_upper = 0
if word.isalpha():
    for i in word[1:]:
        if i.isupper():
            count_upper += 1
else:
    print("Please enter a string value!")
if count_upper>0:
    print(True)
else:
    print(False)