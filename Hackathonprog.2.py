import time

nam = input("What is your name?\n")
if nam == "":
    nam = "Alice"
print("Hello " + nam + ", welcome to our game. You have to make decisions correctly in order to suceed. You will be given a series of questions in which you are expected to respond with either one of the inputs as it is spelled in the question to continue your journey. Good Luck!!\n")


def game(name):
    lives = 3
    time.sleep(1)
    print("")
    print(".")
    time.sleep(1)
    print("  .")
    time.sleep(1)
    print("    .")
    time.sleep(1)
    print("      .")
    print(name[0] + "     .")
    print("      o")
    time.sleep(1)
    print(name[0] + "     ")
    print("      o")
    time.sleep(1)
    print("\n      o")
    time.sleep(3)
    print("You fell into the hole with the rabbit...")
    for i in range(50):
        print('\n')
    #so here is the layout  of how questions should be arranged
    print(name + " " + " walks down the path and stumbles upon a toad, should they pick it up or should they let it rest?\n")
    prompt = input("Grab or Leave: ")
    if prompt.lower()[0] == "g":
        print("The toad was poisonous!" + " " + name + " " + " looks frantically for help. A mysterious cat offers help.")
        response = input("Accept or Ignore: ")
        if response.lower()[0] == "a":
            print("The cat leads you to a lovely house. The doors swing open." + " " + name + " " + " enters the house and is greeted with a charming tea party.")
            choice = input("Join in or Leave: ")
            if choice.lower()[0] == "j":
                print(name + " drinks the magical tea. ") #
        else:
            print(name + " dies")
            print("Game Over")
        
    else:
        print(name + " " + "keeps walking")
        print(name + " " + "is lost in a forest." + " " + name + " " + "finds a path that is divided into 3 smaller paths." )
        direction=input("Right or Left or Straight: ")
        if direction.lower()[0]== "r":
            print(name + " " + "falls in a river, and lost a life.")
            lives = lives - 1
        elif direction.lower()[0]== "l":
            print(name + " " + "finds a shiny Charizard. They decide to stay in Wonderland and become a pokémon master")
        else:
            print(name + " " + "found a way out of the forest! ")
            time.sleep(2)
            print("You find a path and keep walking down, you pass a garden of flowers that laughs at you as you walk past. You see a pair of scissors on the ground next to them, what do you do?")
            pickup=input("Pickup or Leave: ")
            if pickup.lower()[0]=="p":
                print(name + " " + " attacks the flowers. The attack was not very effective." + " " + name + " " + " gets poisoned by flowers")
                lives=lives-0.5
            else:
                print(name + " " + " stays calm and ignores the flowers, and finds a desert")
                time.sleep(3)
                print(" You have been traversing the desert for 2 days without any water. You see two figures in the distance, one blue and one red. Which one do you go to?")
                mirage=input("RedMirage or BlueMirage:")
                if mirage.lower()[0]=="r":
                    print(name + " " + "has found a magicarp, (╥﹏╥)." + " " + name + "and the magicarp die together in the desert due to heatstroke")
                else:
                    print(name + " " + "has found a Gyarados in an oasis, ♡⸜(˶˃ ᵕ ˂˶)⸝♡. Gyarados uses Hydro Punp on" + " " + name + "." + " "  + "It was very effective")
                    lives=lives+1
                    time.sleep(5)
                    print("You have been traversing in the desert whith Gyarados when you see a blue streak in the horizon. It's a blue hedgehog named Sonic.")
                    print("Sonic has challenged you to a yu-gi-oh card game. Do you accept?(Yes or No)")                 
                    accept=input("Yes or No:")
                    if accept.lower()[0]=="y":
                        print(name + " " + "has been engaged in an intense game of Yu-Gi-Oh! and has 1 life point left (ó﹏ò｡). Should you draw a card and hope its strong or do you hope that your deck is strong enough?")
                        duel=input("Draw or Fight:")
                        if duel.lower()[0]=="f":
                            print(name + " " + "dramaticaly gets blown away as they lose their last life point." + " " + name + " " + "does not have plot armor and dies")
                            lives=lives-2
                        else:
                            print(name + " " + "drew number 99 Utopia Dragonar." + " " + name + " " + "wins the duel and gets Sonic to help them escape Wonderland")
                            time.sleep(7)
                            print("Sonic has carried" + " " + name + "all across the desert and they find a giant white gate, a giant black gate, and a small metal door, all floating in the middle of the desert. Which one will you chose?")
                            door=input("White or Black or Metal:")
                            if door.lower()[0]=="b":
                                print(name + " " + "has opened a door they shouldn't have. Insided the door are Obelisk The Tormenter, The Winged Dragon of Ra, and Slifer The Sky Dragon." + " " + name + "got molly whopped. and losses all their lives")
                                lives=0
                            elif door.lowerr()[0]=="m":
                                print(name + " " + "has been teleported to a random beach!" + " " + name + " thinks they are finnaly back home when they run into Kenjaku, Jogo, Hanami, and Mahito. You are beyond cooked")
                                lives=0
                            else:
                                print(name + " " + "opens the white door and finds a floating girl called paimon." + " " + name + " likes it in Tyvat and decides to stay")
                                print("Game Completed")
                                
                                                 
                                           
                                                 
                                     
                                           
                                           
                          
                          
                          
                          
                        
                
            


        





game(nam)
