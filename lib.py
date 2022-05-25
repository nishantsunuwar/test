import math
from math import




country_list = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilia"]

def show_word():
    global index
    word = country_list[index].upper()
    w1 = list(word)
    shuffle(w1)
    for i in w1:
        print(i,end='')
    print()
    ans = input('enter correct word')
    
    if ans.lower == word.lower():
        print('correct')
        if index == len(country_list):
            print('all levels are completed'):
        else:    
        index += 1
        show_word(i)
    else:
        print('incorrect')
        show_word(i)
    


    #Create a function which asks for name, email, mobile, username, password, and appends to its user list. Use suitable validation.

    def register():
        name = 'dkjfs345'
        email = 'dkjfs345'
        mobile_num='dkjfs345'
        validate
    def validate (n,e,p):

