# Author JRI 10/27/21

word1 = input("enter a vegetable ")
word2 = input("enter another vegetable ")

if word1 < word2:
    print(word1 + " comes before " + word2)
elif word1 > word2:
    print(word1 + " comes after " + word2)
else:
    print(word1 + " is " + word2)
