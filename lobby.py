#NOTE: This is actually the main floor but repl.it doesn't allow this to be called main floor

gibberish = {"a":"a","b":"a","c":"b","d":"c","e":"d","f":"e","g":"f","h":"g","i":"h","j":"i","k":"j","l":"k","m":"l","n":"m","o":"n","p":"o","q":"p","r":"q","s":"r","t":"s","u":"t","v":"u","w":"v","x":"w","y":"x","z":"y"} #dictionary
atmkeys = list(gibberish.keys())

def decode_gibberish (clue):
  """
  The purpose of this function is to unscramble the clues that are written in a shifted alphabet gibberish language. 

  Preconditions:
  clue is a string containing the clue the user has collected. 

  Parameters:
  clue: string of letters, numbers or spaces

  Postconditions:
  Outputs the translated clue sentence in normal alphabet. 
  """
  
  decrypted = ""
  for i in range(len(clue)):
    if clue[i] in atmkeys:
      key = clue[i]
      value = gibberish[key]
      decrypted += value
    elif clue[i].isdigit():
      decrypted += clue[i]
    elif clue[i] == ",":
      decrypted += clue[i]
    else:
      decrypted += " "
  return decrypted


def talk_clerks ():
  """
  The purpose of this function is to provide clues to the user based on which clerk the user asks. 

  Preconditions:
  User has inputed the command 'talk to clerks' in main.

  Parameters:
  This function doesn't take in any Parameters

  Postconditions:
  Outputs the desk clerk's clue that was asked. 
  """

  peopleclues = ("All of the clues in the main floor are written in gibberish, store them in your journal and use the ATM machine to translate them.", "zpv xjmm xbou up usbwfm uispvhi uif gmppst jo uijt psefs: nbjo gmpps, gjstu gmpps, cbtfnfou.", "uif fmfwbups nbz ibwf bopuifs qvsqvtf uibo usbwfmmjoh.") #tuple
  while True:
    name = input("Who would you like to talk to? \nIf you want to continue exploring the main floor type 'go back' ")
    if name == "Bob":
      return ("Bob's clue is: " + peopleclues[0])
    elif name == "Joe":
      return ("Joe's clue is: " + peopleclues[1])
    elif name == "Jeff":
      return ("Jeff's clue is: " + peopleclues[2])
    elif name == "go back":
      break
    else:
      return "\nThis person isn't here."