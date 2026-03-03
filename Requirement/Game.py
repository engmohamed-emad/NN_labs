import numpy as np

# TODO [1]: implement the guessing_game function
def guessing_game(max, attempts): # hint: return type is tuple[bool, list[int], int]:
    chosen_int:int = 20
    guesses:List[int]=[]
    i=0
    while i< attempts:
        try:
            guess=int(input(f"Attempt {i+1}/{attempts}: Guess the number between 1 and {max}: "))
            guesses.append(guess)
            i+=1
            if(guess== chosen_int):
                print("Conratulations you guessed the number")
                return (True,guesses,chosen_int)
            elif(guess< chosen_int):
                print("Too low try again")
            else:
                print("Too high try again")
        except ValueError:
            print("Please enter a valid integer.")
    return (False,guesses,chosen_int)

# TODO [2]: implement the play_game function
def play_game()-> None:
    max_value:int = 20
    attempts:int = 5
    flage=True
    while flage:
        result=guessing_game(max_value,attempts)
        if result[0]:
            assert result[2] in result[1],f"Error: {result[2]} should be in the list of guesses {result[1]}"
            print(f"You won! The number was {result[2]}. Your guesses were: {result[1]}")
        else:
            assert result[2] not in result[1],f"Error: {result[2]} should not be in the list of guesses {result[1]}"
            print(f"Game over! The number was {result[2]}. Your guesses were: {result[1]}")
        play_again=input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            flage=False
    pass
            

