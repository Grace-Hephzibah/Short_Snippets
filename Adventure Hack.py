import time

def text_render(text):
    for i in text:
        print(i, end = "")
        time.sleep(.02)
    print()


text_render("Welcome to this Simple Text Based Adventure")
text_render("What is your name? ")
name = input()
text_render("What is your age? ")
age = int(input())

health = 10

if age >= 18:
    text_render("You are old enough to play!")

    text_render("Do you want to play? ")
    wants_to_play = input().lower()
    
    if wants_to_play == "yes":
        text_render("You are staring with " + str(health) + " health")
        text_render("Let's play!")

        left_or_right = text_render("First choice... Left or Right (left/right)? ")
        left_or_right = input()
        if left_or_right == "left":
            text_render("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")
            ans = input()

            if ans == "around":
                text_render("You went around and reached the other side of the lake.")
            elif ans == "across":
                text_render("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            text_render("You notice a house and a river. Which do you go to (river/house)? ")
            ans = input()
            if ans == "house":
                text_render("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    text_render("You now have 0 health and you lost the game...")
                else:
                    text_render("You have survived... You win!")

            else:
                text_render("You fell in the river and lost...")


        else:
            text_render("You fell down and lost...")

    else:
        text_render("Cya...")
else:
    text_render("You are not old enough to play...")












