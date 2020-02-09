print("Adventure begins")
print("\nYou are adventurer Tim and you plan to defeat the Dark Lord of your relm.")
Question_one = print("\t What do you do?:")
One = print("\t1.Go to the shop and spend all your money on gear and none on food and supplies.")
Two = print("\t2. Leave home without a weapon and armor.")
user_input = input()

 
if user_input == "1":
    import random
    r = random.randint(1,2)
    if r == 1:
        print("A week has passed and you are starving")
        Question_two = print("\t What do you do?:")
        One = print("\t1. You fight a wild boar.")
        Two = print("\t2. You forage some wild berries.")
        user_input = input()
        if user_input == "1":
                Question_three = print("\t What do you do?:")
                One = print("\t1. You attack")
                Two = print("\t2. You block")
                user_input = input()
                if user_input == "1":
                    print("You kill the boar and collect meat you can eat and sell.")
                    print("You gain enought money from selling the meat to buy new gear.")
                    print("You leveled up to Level 2.")
                    Question_five = print("\t What do you do?:")
                    One = print("\t1. Continue?")
                    Two = print("\t2. Quit")
                    user_input = input()
                    if user_input == "1":
                        print("You continue on your adventure")
                        print("You go straight to the Dark Lord's castle")
                        print("You battle the minions slowly leveling up to level 10 when you confront the Dark Lord")
                        Question_five = print("\t What do you do?:")
                        One = print("\t1. You battle him knowing you are underleveled")
                        Two = print("\t2. You fee")
                        user_input = input()
                        if user_input == "1":
                            print("Since you are extremely underleveled you lose and die")
                            print("Game over")
                        elif user_input == "2":
                            print("You flee but the Dark Lord's castle but yu are blocked by the Dark Lord's strongest general")
                            print("Game over")

                if user_input == "2":
                    print("The boar charges you and kills you.")
                    print("Game over")
        if user_input == "2":
            print("The berries were poisonous and you die.")
            print("Game over")
    elif r == 2:
        print("You find a group a recently failed adventurers")
        Question_four = print("\t What do you do?:")
        One = print("\t1. You kill them and steal their gear.")
        Tow = print("\t2. You ask them for their gear kindly.")
        user_input = input()
        if user_input == "1":
            print("You accidently leave a survivor and the Royal Guard of the relm catch your crime and execute you.")
            print("Game over")
        elif user_input == "2":
            print("They gift you the gear and you promise to defeat the Dark Lord for them.")
            print("You level up to level 2")
            Question_five = print("\t What do you do?:")
            One = print("\t1. Continue?")
            Two = print("\t2. Quit")
            user_input = input()
            if user_input == "1":
                print("You continue your adventure for another year and become level 50")
                print("The Dark Lord, wary of your strenth, strenthens his army.")
                Question_five = print("\t What do you do?:")
                One = print("\t1. Continue training to become stonger")
                Two = print("\t2. Charge the Dark Lord's castle")
                user_input = input()
                if user_input == "1":
                    print("You level up to level 100 and is able to completely overwhelme the Dark Lord and all of his army")
                    print("The failed adventurers appear to you as their true forms, dieties, that blessed you with legendary equipment and they are here now to make you into a new diety.")
                    Question_five = print("\t What do you do?:")
                    One = print("\t1. Accept and become a diety")
                    Two = print("\t2. Deny and become the hero of the relm")
                    user_input = input()
                    if user_input == "1":
                        print("You are now a new diety of the relm")
                        print("Game fin")
                    elif user_input == "2":
                        print("You become a hero with riches and fortune")
                        print("Game fin")
                    else:
                        print(r)
                elif user_input == "2":
                    print("You charge in overconfindently and get overwhelmed by the Dark Lord's army")
                    print("Game over")
    else:
        print(r)
elif user_input == "2":
    import random 
    r = random. randint(1,2)
    if r == 1:
        print("You confront a slime monster and die")
        print("Game over")
    elif r == 2:
        print("A wise, old knight sees you and give you his old gear and some supplies.")
        print("You level up to level 2.")
        Question_five = print("\t What do you do?:")
        One = print("\t1. Continue?")
        Two = print("\t2. Quit")
        user_input = input()
        if user_input == "1":
            print("You confront a slime monster and it attacks.")
            Question_six = print("\t What do you do?:")
            One = print("\t1. You attack")
            Two = print("\t2. You block")
            user_input = input()
            if user_input == "1":
                print("You attack and the slime catches your blade and kills you.")
                print("Game over")
            elif user_input == "2":
                print("You block and notice the slime's weakness and you kill it by burning it.")
                print("You level up to level 3.")
                Question_five = print("\t What do you do?:")
                One = print("\t1. Continue?")
                Two = print("\t2. Quit")
                user_input = input()
                if user_input == "1":
                    print("You adventure for another month and gain 7 levels.")
                    print("You are now level 10")
                    print("You encounter the Dark Lord's strongest general.")
                    Question_five = print("\t What do you do?:")
                    One = print("\t1. Battle him.")
                    Two = print("\t2. Flee Cowardly.")
                    user_input = input()
                    if user_input == "1":
                        print("He begins to attack")
                        Question_five = print("\t What do you do?:")
                        One = print("\t1. Match his attack")
                        Two = print("\t2. Parry")
                        user_input = input()
                        if user_input == "1":
                            print("He is too fast and kills you before you could damage him.")
                            print("Game over")
                        elif user_input == "2":
                            print("You parry and counterattack.")
                            print("You mortally wound him")
                            Question_five = print("\t What do you do?:")
                            One = print("\t1. Spare him")
                            Two = print("\t2. Finish him")
                            user_input = input()
                            if user_input == "1":
                                print("You turn your back and he recovers and follows you, eventually finding you and killing you")
                                print("Game over")
                            elif user_input == "2":
                                print("You finish him and gain the coordinates for the Dark Lord's palace")
                                print("You level up 10 times to level 20")
                                Question_five = print("\t What do you do?:")
                                One = print("\t1. Continue?")
                                Two = print("\t2. Quit")
                                user_input = input()
                                if user_input == "1":
                                    print("You arrive at the Dark Lord's castle")
                                    print("You defeat all the guards and face the Dark Lord himself")
                                    Question_five = print("\t What do you do?:")
                                    One = print("\t1. You charge blindly")
                                    Two = print("\t2. You wait for his attack")
                                    user_input = input()
                                    if user_input == "1":
                                        print("You fall into a trap and die")
                                        print("Game over")
                                    elif user_input == "2":
                                        print("You block his attack and begin to trade blows")
                                        print("You see and opening")
                                        Question_five = print("\t What do you do?:")
                                        One = print("\t1. Thrust your sword into his heart")
                                        Two = print("\t2. Slice at his hip")
                                        user_input = input()
                                        if user_input == "1":
                                            print("His chestplate is too strong in your sword shatters leaving you defenceless")
                                            print("Game over")
                                        elif user_input == "2":
                                            print("You slice between the plates of armor and bring the Dark Lord to his knees. You put your blade to his throat.")
                                            print("He takes off his helmet and reveals that he is your father")
                                            Question_five = print("\t What do you do?:")
                                            One = print("\t1. Kill him and save the Whole relm")
                                            Two = print("\t2. Don't kill him, give up and allow the Dark Lord conquer the relm")
                                            user_input = input()
                                            if user_input == "1":
                                                print("You lop off his head and you relish in your victory, but the Dark Lord's power tempts you.")
                                                print("You take to place as the new Dark Lord")
                                                print("Game Fin")
                                            elif user_input == "2":
                                                print("You spare him and the Dark Lord takes over the relm")
                                                print("You become his right hand man")
                                                print("Game fin")
                                            else:
                                                print(r)
                    elif user_input == "2":
                        print("You run and he stabs you in the back killing you")
                        print("Game over")

"""
                        if user_input == "2":
                            print("He stabs you in the back and you die.")
                            print("Game over")
                else:
                    print(r)

elif user_input == "3":
    import random 
    r = random. randint(1,4)
    if r == 1:
        print("You go for your dad but he knocks you out. Game over :(")
    elif r == 2:
        print("Your parents take the knife and call the hospital because they say you’re insane. Game over :(")
    elif r == 3:
        print("You kill your mom, then your dad kills you. Game over :(")
    elif r == 4:
        print("You successfully kill both your parents and escape")
    else:
        print(r)
elif user_input == "4":
    import random 
    r = random. randint(1,3)
    if r == 1:
        print("You can go if you finish your homework")
    elif r == 2:
        print("Your parents will bring you and your friends paintballing instead")
    elif r == 3:
        print("You can go, but your family disowns you if you do")
    else:
        print(r)
 
"""
"""
   print("You land awkwardly so you will have a limp for rest of game") or
   print("You land perfectly and leave in your car") or
   print("You land on your neck and die") or
   print("You can't get the window open")
else:
   print("Test")
"""