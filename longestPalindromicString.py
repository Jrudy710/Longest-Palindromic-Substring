# This is a program that will be used to compute the longest palindromic substring when given a string s

def longestOne(s):                                                                           # Method Block
   
   # Create an empty dictionary to store whether a substring is or isn't a palindrome
   palindromic = {}                                                                          # Defines an empty dictionary
   
   start, end = 0, 0                                                                         # Defines start and end
   
   theSubstring = ""                                                                         # Defines theSubstring to be returned
   
   if isPalindrome(s):                                                                       # If the string is a palindrome then we are done
      return s                                                                               # Returns the string to the user
   
   for LCV, letter in enumerate(s):                                                          # Looping through the string
      
      # For the instance that there is only a one character string passed to the method
      if letter not in palindromic.keys():                                                   # Checking to see if the item is in the dictionary
         palindromic[letter] = True                                                          # Adding the key to the dictionary
         
         theSubstring = letter if len(letter) > len(theSubstring) else theSubstring          # Sets the value of theSubstring
      
      # Then we need to expand the palindromic substring 
      start = LCV                                                                            # Sets the current value of start
      end = start + 1                                                                        # Sets the current value of end
      
      #print(f"{LCV}: {letter} with substring {s[LCV: LCV+1]}")
      endExpansion = True                                                                    # Sets the value of endExpansion
      
      while start >= 0 and end + 1 != len(s):                                                     # While Loop      
         
         if endExpansion:                                                                    # If statement
            end += 1                                                                         # Adds to the value of end
            endExpansion = False                                                             # Sets the value of endExpansion
         
         else:                                                                               # Else statement
            start -= 1                                                                       # Subtracts from the value of start
            endExpansion = True                                                              # Sets the value of endExpansion
         
         print(f"Looking at substring {s[start: end]}")
         if s[start: end] not in palindromic.keys():                                         # If the substring isn't in the dictionary
            palindromic[s[start: end]] = isPalindrome(s[start: end])                         # Sets the value in the dictionary
            
         theSubstring = s[start: end] if palindromic[s[start: end]] and len(s[start: end]) > len(theSubstring) else theSubstring
         
   
   return theSubstring                                                        # sub string returned to the user


def isPalindrome(s):                                                          # Checking if a substring is a palindrome
   
   reversion = s[::-1]                                                        # Reverses the passed string
   
   print(f"Comparing {reversion} and {s}: {reversion == s}")
   
   return reversion == s                                                      # Returns whether the two strings are the same

def main():

   s = "adam"
   
   print(f"The longest one is {longestOne(s)}")


main()