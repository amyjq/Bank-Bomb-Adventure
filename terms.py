terms_and_conditions = ("TERMS AND CONDITIONS"+
"\n\nAKNE is engaged in software development and for good and valuable consideration set forth herein, makes available to you this game." +
"\n\n Section 1. Acceptance of terms and conditions" +
"\n \tAcceptance of these Terms creates an agreement between you and AKNE and regulates the use of the game. By playing this game, you accept these Terms and Conditions. AKNE reserves the right at any time to modify these Terms."+
"\n \tPLEASE READ THESE TERMS CAREFULLY BEFORE STARTING OUR GAME." +
"\n\nSection 2. Ownership and license" +
"\n\tAKNE hereby grants you a non-exclusive, non-transferable, non-sublicensable, access to our game, for your non-commercial entertainment use only, provided that you are in compliance with these Terms." +
"\n\nSection 3. Game Performance"+
"\n\tIMPORTANT NOTICE: YOU HEREBY ACKNOWLEDGE YOUR RESPONSIBILITY FOR ANY INTERNET CONNECTION FEES THAT ARE INCURRED WHEN ACCESSING OUR SERVICE. You understand that AKNE's game may not be consistent across all browsers and that the performance of our game may vary."+
"\n\nSection 4. Gaming Policy"+
"\n\t You agree that your use of the service should be lawful and that you will comply with the usage rules." +
"\n\nSection 5. Legal stuff"+
"\n\tThe bank was founded in 1863. You will probably never read this until you finish the game, and that's why this is hidden here. A side note: this may or may not be the passcode for the bomb."+
"\n\nSection 6. Health Advice" +
"\n\tThis game should only take 5-10 min, but in the event that it takes  longer,  take breaks every 20 minutes by looking 20m away for 20 seconds!" +
"\n\nSection 7. Disclaimers and limitation of liability"+
"\n\tIn no event will AKNE be liable to you or any third party for any special, direct, indirect, incidental, punitive or consequential damages whatsoever." +
"\n\nSection 8. General"+
"\n\tThese Terms, constitute the entire agreement between you and AKNE with respect to your use of the Service." +
"\n\tBY ENTERING \"YES\" YOU EXPRESSLY ACKNOWLEDGE AND AGREE THAT YOU HAVE READ THESE TERMS AND UNDERSTAND ALL RIGHTS, OBLIGATIONS, TERMS AND CONDITIONS SET FORTH HEREIN. BY AGREEING AND/OR CONTINUING TO USE THE SERVICE YOU EXPRESSLY CONSENT TO BE BOUND BY THESE TERMS AND CONDITIONS AND GRANT AKNE THE RIGHTS SET FORTH HEREIN.")


def terms_agree ():
  agreement = input ("\nDO YOU AGREE TO THE TERMS? (YES/NO) ")
  while (agreement!= "YES") and (agreement!= "yes"):
     print ("You cannot play the game without agreeing to the terms.")
     agreement = input ("\nDO YOU AGREE TO THE TERMS? (YES/NO) ")
  return ("Great! You're all set up to play!")
