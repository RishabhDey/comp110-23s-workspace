'''Excercise 03 - Structured Wordle'''
__author__:int = 730558424

def contains_char(string:str , guess:str)-> bool:
    assert len(guess) == 1
    
    if(guess in string):
        return True
    else:
        return False
    


def emojified( string:str, guess_string:str)-> list[str, int]:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(string) == len(guess_string)
    total = ""
    i =0
    correct = 0
    print(string)
    while(i<len(guess_string)):
       if(contains_char(guess_string, string[i])):
           if(string[i] == guess_string[i]):
               total += f"{GREEN_BOX}"
               correct +=1
           else:
               total += f"{YELLOW_BOX}"
           
       else:
           total += f"{WHITE_BOX}"
       i +=1
       
    return total, correct
      
        
def input_guess(guess_size:int)-> str:
     guess_string = input(f"Enter a {guess_size} character word: ")
     while True:
         if(len(guess_string) == guess_size):
             
             return guess_string
         else:
             guess_string = input(f"That wasn't {guess_size} chars! Try again: ")
             
             
             
     
def main()-> None:
    turn = 1
    string = "codes"
    cond = False
    while turn <=6 and cond == False:   #<- workaround for break operator? Is this allowed?
        print(f"=== Turn {turn}/6 ===")
        guess_string = input_guess(len(string))
        emoji, correct = emojified(guess_string, string)
        print(emoji)
        if(correct == len(string)):
            print(f"You won in {turn}/6 turns!")
            cond = True
        turn+=1
        
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")
        
        

if __name__ == "__main__":
    main()
