from accepted import *
from basement import *
from descriptions import *
from first import *
from lobby import *
from terms import *

print (terms_and_conditions)
print (terms_agree())

#introduction
print ("\nHello!\n", intro_desc)
print ("\nYou have a journal to keep track of clues you find around the bank. On all floors at anytime, you can type 'read journal' to read the clues you have collected and 'store clue' to add a clue to your journal.")
print ("\nHINT: some of the desk clerks speak in GIBBERISH - use the atm machine to understand what they're saying.")
print ("\nHere are the commands you can type in to explore the main floor:")

for i in range(len(main_floor_accept)):
  print ("-" + main_floor_accept[i])

print ("\nHere are the commands you can access on any floor:")
for i in range(len(all_accept)):
  print ("-" + all_accept[i])
print ("\nPlease note that you cannot use some of these commands in the elevator.")


floor = 0 #set initial floor as 0
player_journal = {}
journalkeys = list(player_journal.keys())
vault_open = False

key = False
guards = True

print (floor_desc[floor])

while True:
  #main floor
  if floor == 0:
    command = input("\nYou are on the main floor. What would you like to do? ")

    if command == "store clue":
      index = len(player_journal) + 1
      clue_added = input("what clue did you find? ")
      player_journal[str(index)] = clue_added
      print ("The clue is stored at clue #", index,"To read it, type 'read journal'. To translate the clue, go to the atm machine.")

    elif command == "read journal": #bug
      print (player_journal)

    elif command == "go to atm":
      print (atm_desc)
      while True:
        translateclue = input("\nWould you like to translate a clue? (YES/NO) ")
        if translateclue == "YES":
          cluenumber = list(player_journal.keys())
          read_clue = input("Clue number: ")
          if read_clue.isdigit():
            if int(read_clue) > len(player_journal) or int(read_clue) < 0:
              print ("This clue # doesn't exist in your journal.")
            else:
              read_clue = int(read_clue) - 1
              key = cluenumber[read_clue]
              print (decode_gibberish(player_journal[key]))
              break
          else:
            print ("You have to input a clue #")
        elif translateclue == "NO":
          print ("ok")
          break
        else:
          print ("Not a valid command.")

    elif command == "talk to clerks":
      print (desks_desc)
      print ("\n")
      print (talk_clerks())

    elif command == "go to fountain":
      print (fountain_desc)
      fountain_action = input("\nIf you would like to take a closer look at one of the coins, enter 'zoom in'.")
      if fountain_action == "zoom in":
        print (coin_desc)

    elif command == "go to elevator":
      #elevator actions available
      while True:
        print (elevator_desc)
        print ("\nHere are the commands you can use in the elevator:")
        for i in range (len(elevator_accept)):
           print ("-" + elevator_accept[i])
        elevator_action = input("What would you like to do? ")
        if elevator_action == "use elevator":
          floor = input("\nWhat floor do you want to go to? Buttons: 0 (main floor), 1 (first floor) and -1 (basement). If you want to stay on your current floor and exit the elevator, type the floor number you are on right now. ")
          if floor == "0" or floor == "-1" or floor == "1":
            floor = int(floor)
            break
          else:
            print ("Not a valid floor.")
        elif elevator_action == "view painting":
          print (painting_desc)
        else:
          print ("Not a valid action.")

    elif command == "view terms":
      print (terms_and_conditions)

    else:
      print ("That is not a valid command. Try again!")

  #first floor
  elif floor == 1:
    print (floor_desc[1])

    print ("\nHere are the commands you can type in to explore the first floor:")
    for i in range (len(floor_1_accept)):
      print ("-" + floor_1_accept[i])

    command = input("What would you like to do? ")

    if command == "read journal":
      print (player_journal)

    elif command == "store clue":
      index = len(player_journal) + 1
      clue_added = input("what clue did you find? ")
      player_journal[str(index)] = clue_added
      print ("The clue is stored at clue #", index,"To read it, type 'read journal'.")

    elif command == "go to elevator":
      while True:
        print (elevator_desc)
        print ("\nHere are the commands you can use in the elevator:")
        for i in range (len(elevator_accept)):
           print ("-" + elevator_accept[i])
        elevator_action = input("What would you like to do? ")
        if elevator_action == "use elevator":
          floor = input("\nWhat floor do you want to go to? Buttons: 0 (main floor), 1 (first floor) and -1 (basement). \nIf you want to stay on your current floor and exit the elevator, \ntype the floor number you are on right now. ")
          if floor == "0" or floor == "-1" or floor == "1":
            floor = int(floor)
            break
          else:
            print ("Not a valid floor.")
        elif elevator_action == "view painting":
          print (painting_desc)

    elif command == "go to office":
      key = office()

    elif command == "go to safes":
      print (safes(key))

    elif command == "view terms":
      print (terms_and_conditions)

    else:
      print ("\nNot a valid action. Please try again.")

  #basement
  elif floor == -1:
    print (floor_desc[-1])
    print ("\nHere are the commands you can type in to explore the basement:")
    for i in range(len(basement_accept)):
      print ("-" + basement_accept[i])

    command = input("\nWhat would you like to do? ")

    if command == "read journal":
      print (player_journal)

    elif command == "store clue":
      index = len(player_journal) + 1
      clue_added = input("what clue did you find? ")
      player_journal[str(index)] = clue_added
      print ("The clue is stored at clue #", index,"To read it, type 'read journal'.")

    elif command == "go to elevator":
      while True:
        print (elevator_desc)
        print ("\nHere are the commands you can use in the elevator:")
        for i in range (len(elevator_accept)):
           print ("-" + elevator_accept[i])
        elevator_action = input("What would you like to do? ")
        if elevator_action == "use elevator":
          floor = input("\nWhat floor do you want to go to? \nIf you want to stay on your current floor and exit the elevator, \ntype the floor number you are on right now. ")
          if floor == "0" or floor == "-1" or floor == "1":
            floor = int(floor)
            break
          else:
            print ("Not a valid floor.")
        elif elevator_action == "view painting":
          print (painting_desc)


    elif command == "talk to guards" and guards == True:
      print (guard_truth())
      vault_open = True
      guards = False
      basement_accept.append ('go to vault room')
      basement_accept.remove ('talk to guards')
      print ("\nYou have a new command available but \"talk to guards\" is no longer available. Here is the updated list of commands:")
      for i in range(len(basement_accept)):
        print ("-" + basement_accept[i])

    elif (command == "go to vault room") and (vault_open == True):
      print (vault_desc)
      print (bomb_defuse())
      break

    elif command == "view terms":
      print (terms_and_conditions)

    else:
      print ("\nNot a valid action. Please try again.")
