def print_upper_words(list_of_words,list_of_letters):
     """Given list of words, and a list of letters print words that start with one of those letters.
    for example :
    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])

    Should print  HELLO", "HEY", "YO", and "YES"
    """
     letters = ""
     for word in list_of_words:
          for letter in list_of_letters:
               if word[0]==letter:
                 print(word.upper())   
        
         
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],["H","y"])
    