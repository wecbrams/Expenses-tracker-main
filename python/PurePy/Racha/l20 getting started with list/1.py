empty_list = []
print()
number=[4,3,3,554,5777,87]
print(number)

number1=[4,3,3,554,5777,87] *3
print(number1)

number=[4,3,3,554,5777,87]
print(number[::-1])

# Word matching 
print("\nWord matching\n")
def match_words(words):
    ctr = 0
    lst=[]
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr +=1
            lst.append(word)
        print("List of words with first and last character same\n",lst)
        return ctr
count =match_words(["abc",'cfc','xyz','aba','1221'])
print("Number of words having first and last character same: ",count)