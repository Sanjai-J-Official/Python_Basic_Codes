import random
import time

print("Number Guessing Game!")

while True:
    ran_num = random.randint(1, 10)   
    chance = 3   

    while chance > 0:
        n = int(input("Enter your guess (1-10): "))
         
        
        if n == ran_num:
            print("You Win the Game!")
            break
        else:
            chance -= 1
            if chance > 0:
                print(f"Wrong guess! Try again. You have {chance} chance(s) left.")
            else:
                print("Wrong guess! No chances left.")
                print("Wait 5 seconds...")
                time.sleep(5)
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
