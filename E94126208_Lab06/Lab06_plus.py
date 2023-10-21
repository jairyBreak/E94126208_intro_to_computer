
def put(input_word):
    ans_list = []
    if len(input_word) == 1:
        return [input_word]#if length is 1,there is no need to change position again.
    for i in input_word:
        input_list = list(input_word)#let input_word str to list.
        input_list.remove(i)#remove "i"th number.
        left_word = "".join(input_list)#after remove,have the left word from list to str.
        
        #print(i,":",left_word)
        for j in put(left_word):#let left word remove the number again, until the word length is 1
            #print(j,":",left_word,i)
            ans_list.append(i+j)#let the "i"th number which was removed join the left word(after process),and  
    return ans_list
    
input_word = input("輸入字串")
print(put(input_word))

