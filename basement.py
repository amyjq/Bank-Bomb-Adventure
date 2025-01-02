from termcolor import colored

#basement 
guards_desc = ("\nYou see two guards, one has the nameplate 'Hakekate' the other has the nameplate 'Berbohong'. Which one would you like to talk to? One tells the truth, and one tells a lie but you may only talk to one of them.")

vault_desc = ("\nYou enter the vault room and notice a bomb right in the middle of it. This is it. Your final obstacle in order to become a security guard at this bank!")

win_desc = ("\nCongratulations! You have finished the game and are now on your way to become a security guard at the marvelous AKNE Bank. It was a long journey but at least now you have your dream job. We hope you enjoyed the game.")

lose_desc = ("\nBOOM! The bomb has 'exploded' and you have failed your mission. Try again next time.")

#assuming the user inputs an integer
def bomb_defuse ():
  """
  The purpose of this function is to explode the bomb or defuse it depending on what the user inputs as the passcode.
  Preconditions: floor = -1 and user has talked to guards and has entered the vault. 
  Parameters: There are none.
  Postconditions: After the user inputs the passcode if it is correct returns a string with the win message in green. If they guess the passcode incorrectly 3 times the bomb 'explodes' and the function returns the lose message.
  """
  tries = 3
  while tries>0:
    passcode = input("What is the passcode to defuse the bomb? ")
    if len(passcode) == 4 and (passcode.isdigit()):
      if passcode != "1863":
        tries -= 1
        print ("That's not the right passcode. You have", str(tries), "tries left.")
      else:
        return colored(win_desc, 'green')
    else:
      print ("The passcode is of length 4 and is all digits. Please try again.")
      tries = tries
  return colored(lose_desc, 'red')

#guards
def guard_truth (): 
  """
  To print the clues of the guards and then to have the guards step aside and allow access to the vault.
  Preconditions: User is in the basement and floor = -1.
  Paramenters: None.
  Postconditions: Returns a string that says "The guards step aside and allow you to pass."
  """
  global vault_open
  print (guards_desc)
  guard_choice = input("\nWhich guard would you like to talk to? \n")
    
  while (guard_choice != "Hakekate") and (guard_choice!= "Berbohong"):
    print("Not a valid guard. Check your spelling.") 
    guard_choice = input("\nWhich guard would you like to talk to? \n")
  
  if guard_choice == "Hakekate": 
    print ("\"Did you read the terms and conditions? They might be important to solve your mission and section 5 may be worth revisiting.\"")

  elif guard_choice == "Berbohong":
    print ("100 + 1763 = 1900. The bank was founded in 1900.") 
  
  return ("The guards step aside and allow you to pass.")