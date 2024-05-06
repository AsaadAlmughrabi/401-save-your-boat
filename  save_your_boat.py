print("""
      Welcome to save your boat game :D 
      
      Description :

        1) you have a boat that have 5 lives when boat lives end it will drown
        2) you should guess the word by choosing a letter from the Eeglish laphapet
        3) if you got a letter wrong you will lose a live
        4) when you guess the letter right you will be provided with the updated word
        5) if you guess everything right you will win
        6) if you finish your lives and did not guess the word you will lose
        7) to quit you can write exit
      """)


words = [
    {
        'name': "cat",
        'hint': [
            "Has pointed ears",
            "Fur can be black, white, or orange",
            "Sleeps a lot during the day",
            "Loves to play with string",
            "Hisses when angry",
            "Can see in the dark",
            "Likes to climb trees",
            "Often cleans itself with its tongue"
        ]
    },
    {
        'name': "dog",
        'hint': [
            "Known for its loyalty",
            "Comes in various breeds and sizes",
            "Enjoys going for walks",
            "Can be trained to do tricks",
            "Barks to communicate",
            "Has a strong sense of smell",
            "Likes to dig holes in the yard",
            "Known as 'man's best friend'"
        ]
    },
    {
        'name': "fish",
        'hint': [
            "Breathes underwater using gills",
            "Can be found in oceans, rivers, and lakes",
            "Some species have scales, others don't",
            "Swims using fins",
            "Many species are kept as pets in aquariums",
            "Can lay thousands of eggs at once",
            "Some species migrate long distances",
            "Some fish have bioluminescent properties"
        ]
    },
    {
        'name': "lion",
        'hint': [
            "Known as the king of the jungle",
            "Has a majestic mane",
            "Hunts in packs or prides",
            "Roars loudly to communicate",
            "Found in Africa and parts of Asia",
            "Females do most of the hunting",
            "Can run at speeds up to 50 mph",
            "Spend most of their time resting and conserving energy"
        ]
    }
]


total_lives = 5

def guess_the_letter(attempts):
    global total_lives
    word = words[attempts]
    answer = word['name']
    print("Guess This: ")
    guess_blank = f'{"".join(["_"] * len(answer))}'
    print(guess_blank)
    hint1 = word['hint'].pop(0)
    hint2 = word['hint'].pop(0)
    print("Hint:")
    print("    - " + hint1)
    print("    - " + hint2 + "\n")
    counter = 0
    guess_list = list(guess_blank)

    while True:
        guess = input("Choose a letter ->")
        if guess != 'exit':
            if guess != answer[counter]:
                print("You got it wrong")
                total_lives -= 1
                print(f'Boat lives: {total_lives}')
                if total_lives == 1:
                    hint1 = word['hint'].pop(0)
                    hint2 = word['hint'].pop(0)
                    print("Hint:")
                    print("    - " + hint1)
                    print("    - " + hint2 + "\n")
            else:
                if guess == "exit":
                    return 0
                print(f"You got it right")
                print("Word after guess")
                guess_list[counter] = guess
                counter += 1
                print("".join(guess_list))
            if "".join(guess_list) == word['name']:
                print("Congratulations, you've guessed the word!")
                break
            if "_" not in guess_list:
                print("Congratulations, you've guessed the word!")
                break
            if total_lives == 0:
                print("Game Over. The word was: " + answer)
                return 0
        else:
            return 0

        
      

if __name__ == "__main__":
    attempts = 0
    response = input("Do you want to play? (y/n/exit)")
while response.lower() != 'n' and response.lower() != "exit":
    if guess_the_letter(attempts) == 0:
        break
    attempts += 1
    if total_lives == 0 or attempts >= len(words):
        print("Game over")
        break



    

    