import random

office_desc = ("\nUpon entering the first floor you see two offices. The door to one of the offices are unlocked and you enter. On the ground you see a bunch of pamphlets.")

key_desc = ("\nAs you turn around you see a piece of metal on the ground.")

pamphlet_info = "\nYou pick up the pamphlet and see a bunch of scrambled words written on it. Looking closely, you're able to see the words: "

pamphlet_sentence = ["This", "bank", "was", "founded", "during", "the", "Battle", "of", "Chickamauga."]

safe_desc = ("\nYou have arrived in the safe room. There are two safes that catch your eye. They are labelled safe 18 and safe 63. You may use your key to open them.")

safe_18 = ("\nYou search the safe numbered 18 and there is a paperweight from the past. after brushing away the dust, it reveals a year on the bottom. Unfortunately, the middle two digits are illegible, but you're able to pick ou. the first and last digits which are 1 and 3 respectively.")

safe_63 = ("The last 2 digits of the code are in front of you")

def office():
  """"
  Purpose: Collect a clue inside a pamphlet in the office and find a key to unlock safes.

  Preconditions: User is on the first floor
  Parameters: None
  Postconditions: The user receives a scrambled sentence containing a clue and a key to the safes. 

  """
  
  key = False
  print (office_desc)
  office_choice = input("\nWhat would you like to do? ")

  while office_choice != "pick up pamphlet":
    print ("\nNot a valid action")
    office_choice = input("\nWhat would you like to do? ")
  else:
    print (pamphlet_info)
    random.shuffle(pamphlet_sentence)
    print (pamphlet_sentence)
    print (key_desc)
    key_choice = input ("What would you like to do? ")
    while key_choice != "examine metal":
      print ("\nYou can't do that")
      key_choice = input ("\nWhat would you like to do? ")
    else:
      key = True
      print ("\nYou pick it up and it's a key. This might be useful later on...")
      return key


def safes (key):
  """
  Purpose: The purpose of this function is to return the clues for the safe that the user chooses if they have the key from the office.
  
  Preconditions: The user is in the safe room and has the key.
  Parameters: The value "key" must be true to run this function.
  Postconditions: The function a clue for the chosen safe as a string.
  """
  if key == False:
    return ("\nThe safes are locked!") 
  print (safe_desc)
  safe_choice = input("\nWhat would you like to do? ")
  while (safe_choice != "search safe 18") and (safe_choice != "search safe 63"):
    print ("\nYou can't do that.")
    safe_choice = input("\nWhat would you like to do? ")
  if safe_choice == "search safe 18":
    return (safe_18)
  elif safe_choice == "search safe 63":
    return (safe_63)
  else:
    return ("Not valid")
