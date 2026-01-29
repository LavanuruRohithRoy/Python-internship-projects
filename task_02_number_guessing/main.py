import random

def main():
    while True:
        secret_number  = random.randint(1,50)
        attempts = 0
        max_attempts = 5

        print("\n Guess the number between 1-50")
        print("you have", max_attempts, "attempts to guess the number")

        while attempts < max_attempts:
            user_input=input("Enter your Guess:")
            digits=""
            for ch in user_input:
                if ch.isdigit():
                    digits+=ch
            if digits=="":
                print("Enter a valid number")
                continue

            guess=int(digits)
            attempts+=1
            if guess == secret_number:
                print("Correct! you guessed it in" , attempts, "attempts.")
                break
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Too low!")
            
        if attempts == max_attempts and guess !=secret_number:
            print("Game over. Number was:", secret_number)
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Bye!")
            break

if __name__ == "__main__":
    main()