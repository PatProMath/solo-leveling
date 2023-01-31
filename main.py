print('''
*******************************************************************************

         -     -                 .      :
         -     -     -                  |          -
   -           -     -    .      .      |    -     -     -
         -     -     -    |      .      |    -     -     -
   -     -     -     -    |      :      |    -     -     -
   -     -     -     -   .|     _|_     |.         -     -
   -     -     -       ._-|             |-_.       -     -
   -     -     -     ._-  |     .       |  -_.     -     -
-.--.--.--.--.--. _ _-_ _ |   E-1-2-3   | _ _-_ _ .--.--.--.--.--.-
 |  |  |  |  |  |`.| | | ||   _______   || | | |.'|  |  |  |  |  |
8888888888888888L_|`.88888|  |   |   |  |88888.'|_J8888888888888888
       |:     `888L_|`.|  |  |   |   |  | :|.'|_J888'    :|
       |:       `888L_|`. |  |   |   |: | .'|_J888'      :|
       |:        |`888L_|`.  |   |   |  .'|_J888'        :|
_______<:________|:_`888L_|) |   |   | (|_J888':|________:|________
       |:        |:   `888L. |___|___| .J888'  :|        :|
       |:        |:     `88|/_________\|88'    :|        :|
 __..--       _.-'        ,|L_________J|.      `-._      ``--..__
'         _.-'            |/___________\|          `-._          ``
                        .c|L___________J|c.            `-.
                      .' |/_____________\| `.
                    .'|  |L_____________J|  |`.
                  .'  | _/               \_ |  `.
                .'|   _//                 \\_   |`.
              .'  | _///                   \\\_ |  `.
          _______________________________________________
        .'                                               `.
      .'                                                   `.
    .'                                                       `.
___/ Dimensional Level F. Defeat Dungeon Boss to level up to E \___

*******************************************************************************
''')
print("Welcome to Solo Leveling! Your mission is to level up.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You are in a level F dungeon. Instruction: Defeat the dungeon's boss to go to level E. Dungeon's boss: Hobgoblin (Level  F-10).")
print("")
print("WARNING! \n  The hobglobin may have globins as his tribesmen. \n  These guys smell nasty and are persistent in their greed.")
choice1 = input("Choose your weapon. Type \"sword\" or \"spear\".  \n  ").lower()

if choice1 == "sword":
  print("Good choice of weapon for close-range combat! You slay most of them and scale up by XP to F-8. Reach F-10 to take on the hobglobin.")
  choice2 = input("You have gained a reward in a box. There are two boxes in the player's screen, blue and red. Choose one: \"Red\" or \"Blue\" \n  ").lower()
  if choice2 == "red":
    scale = 11
    print(f"Congratulations! You have won Strength, Luck and Speed points. You scale up to F-{scale} with these points.")
    choice3 = input("Would you like to take a break now? 'Wait' or 'Rush' \n  ").lower()
    if choice3 == "wait":
      print("You choose to wait. You decide to strategize and plan. You also gain some mana cores from the corpses of the defeated globins. Your survival in the dungeon for the half-day gives you intelligence and agility points too.")
      scale += 2
      print(f"You are at F-{scale}. Intelligence point of 1 gives you an insight!  \n  INSIGHT: You realize the the count of the defeated globins and mana cores do not add up. There might have been an escapee. Trap ahead.")
      print("")
      print("You overcome trap perfectly and kill minions. Intelligence: +2 | Agility: +1.")
      scale += 3
      print(f"You defeat the Hobglobin after 10 minutes. Your XP is increased by 5! Congrats, you leveled up to E-{int(scale/8)}.")
      print("")
      print(f"PLAYER'S POINTS \n  XP - 14 \n  Strength - 4 \n  Luck - 1 \n  Stealth - 1 \n  Intelligence - 3 \n  Agility - 2 \n \n Scale - {scale}")
    else:
      print("You rush to the boss' room and fall into a trap laid by boss' minion globins. Turns out one escaped you before and made plans with the others.")
      print("You are sorely prepared. You avoid the trap by luck, but 5 goblins surround you! Squat! Boss defeats you with a big hammer. Game Over!")
  else:
    scale = 9
    print(f"You get some points in Strength. Now, you are at scale F-{scale}.")
    choice3 = input("Hmm, would like to face the dungeon boss now? \"Now\" or \"Later\". \n  ").lower()
    if choice3 == "later":
      scale += 2
      print("You decide to strategize and plan. You also gain some mana cores from the corpses of the defeated globins. Your survival in the dungeon for the half-day increases your intelligence and luck points too.")
      print(f"You are currently at F-{scale}. Good luck. You sense a trap ahead when you see some globins by chance. ")
      choice4 = input("Attack 'Head-on' or 'One first' \n  ").lower()
      if choice4 == "one first":
        print("Underdog, you pick them off one by one! You gain more points. XP: +2 | Intelligence: +2 | Strength: +3")
        scale += 8
        print("You also gain stealth points and agility points. You are past F-15")
        scale += 5
        print(f"You defeat the minions and face boss. You defeat the boss after 15 minutes. You gain 5 more XP and level up to E-{int(scale/8)}.")
        print("")
        print(f"PLAYER'S POINTS \n  XP - 14 \n  Strength - 4 \n  Luck - 1 \n  Stealth - 1 \n  Intelligence - 3 \n  Agility - 2 \n \n Scale - {scale}")
      else: 
        print("You are All Surrounded! You lose. Game Over.")
    else:
      print("Hasty feet fall into traps! Luck isn't enough. You are injured defeating the boss and his minions. You bleed to death. Game Over!")
elif choice1 == "spear":
  print("You throw the spear at one of the globins, but another crawls on you and bites off your ear. No weapon in hand for defence against the hoard! You lose.")
else:
  print("You put in an unavailable weapon. You are transported to a volcano and burnt by lava. Game Over!")