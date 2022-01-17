from random import randint  # Do not delete this line


def displayIntro():
    print("""
_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________
""")
    pass


def displayEnd(result):
    print("""
__________________________________________________________________________
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
__________________________________________________________________________
    """) if result == False else print("""
    ________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________          
________________________________________________________________________
    """)


def displayHangman(state):
    if state == 0:
        print("""

     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___        

        """)
    if state == 1:
        print("""

     ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___        

        """)
    if state == 2:
        print("""

     ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___        

        """)
    if state == 3:
        print("""

     ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___        

        """)
    if state == 4:
        print("""

     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___        

        """)
    if state == 5:
        print("""

     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___        

        """)


def getWord():
    f = open('hangman-words.txt', 'r')
    lines = f.readlines()
    f.close()
    return lines[randint(0, len(lines) - 1)]


def valid(c):
    if len(c) == 1 and 97 <= ord(c) <= 122:
        return True
    return False


def play():
    resultWord = getWord()
    guessWord = ''.join(['_' for i in range(0, len(resultWord) - 1)])
    state = 0
    while True:
        displayHangman(state)
        print(f"""
Guess the word:  {guessWord}
Enter the letter: 
            """)
        letter = input()
        while not valid(letter):
            print("Enter the letter: ")
            letter = input()
        if letter not in resultWord:
            state += 1
        else:
            guessWord = ''.join([letter if resultWord[i] == letter else
                                 guessWord[i] if guessWord[i] == resultWord[i] else '_' for i in
                                 range(0, len(resultWord) - 1)])
        if guessWord in resultWord:
            print(f"Hidden word was:  {resultWord}")
            return True
        elif state == 5:
            displayHangman(state)
            print(f"Hidden word was:  {resultWord}")
            return False


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print("Do you want to play again? (yes/no)")
        wantToPlay = str(input())
        while wantToPlay.lower() != "yes" and wantToPlay.lower() != "no":
            print("Do you want to play again? (yes/no)")
            wantToPlay = str(input())
        if wantToPlay.lower() == "yes":
            hangman()
            return
        elif wantToPlay.lower() == "no":
            return


if __name__ == "__main__":
    hangman()
