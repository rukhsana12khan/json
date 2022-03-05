# a=[[2,3,4],[5,6,7],[8,1,2]]
# w=[]
# i=0
# while i<len(a):
#     s=[]
#     b=[]
#     d=[]
#     j=0
#     while j<len(a[i]):
#         if j==0:
#             s.append(a[i][j])
#         if j==1:..;[j])
#         print(s)
#         print(b)
#         print(d)
#         j+=1
#     w.append(s)
#     i+=1    
# print(w)          

# a="aab"
# b=[]
# i=0
# while i<3:
#     s=[]
#     j=0
#     while j<len(a):
#         s.append(a[j]) 
#         j+=1
#     b.append(s)   
#     i+=1      
# print(b)        



# a=[[3,5,6],[7,1,4],[8]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     i+=1
# print(sum)        

import random

def hangman():
    list_of_words = ['psycho','sin', 'cold', 'death', 'angel', 'demon','bummer','bullshit','bitch','bang','high','ride']
    word = random.choice(list_of_words)
    # print(word)
    '''Secret word'''
    
    chances = 10
    guess_made = ''
    valid_word = set('abcdefghijklmnopqrstuvwxyz')
    # print(valid_word)
    
    while len(word) > 0:
        main_word = ""
        
        for letter in word:
            if letter in guess_made:
                main_word = main_word + letter
            else:
                main_word = main_word + '_ '
                
        if main_word == word:
            print(main_word)
            print("You won !")
            break
        
        print("guess the word", main_word)
        guess = input()
        
        if guess in valid_word:
            guess_made = guess_made + guess
        else:
            print("Invalid character")
            guess = input()
            
        if guess not in word:
            chances -= 1
            
            if chances == 9:
                print("9 chances left")
                print("-----------")
            
            if chances == 8:
                print("8 chances left")
                print("-----------")
                print('     O     ')
                
            if chances == 7:
                print("7 chances left")
                print("-----------")
                print('     O     ')
                print("     |     ")
            
            if chances == 6:
                print("6 chances left")
                print("-----------")
                print('     O     ')
                print("     |     ")
                print('    /      ')
            
            if chances == 5:
                print("5 chances left")
                print("-----------")
                print('     O     ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 4:
                print("4 chances left")
                print("-----------")
                print('    \O     ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 3:
                print("3 chances left")
                print("-----------")
                print('    \O/    ')
                print("     |     ")
                print('    / \    ')
                
            
            if chances == 2:
                print("2 chances left")
                print("-----------")
                print('    \O/   | ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 1:
                print("1 chance left !! Hangmam on his last breath")
                print("-----------")
                print('    \O/__| ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 0:
                print("You loose")
                print("You let a good man die")
                print("-----------")
                print('     O__| ')
                print("    /|\     ")
                print('    / \    ')
                break
                
                
                
name = input("ENTER PLAYER NAME   -->  ")
print("Welcome", name, '!')
print('*******')
print("You have 10 chances to guess the word")

hangman()

def again():
    while True:
        play_again = input("Do you want to play again enter y if yes or anything if no")
        if play_again == "y":
            hangman()
        else:
            break
again()