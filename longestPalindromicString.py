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
      end = LCV + 1                                                                          # Sets the value of end
      
      #print(f"{LCV}: {letter} with substring {s[LCV: LCV+1]}")
      
      while end + 1 <= len(s):                                                               # While Loop
         
         end += 1
         
         #print(f"Looking at substring {s[LCV: end]}")
         
         if s[LCV: end] not in palindromic.keys():                                           # If the substring isn't in the dictionary
            palindromic[s[LCV: end]] = isPalindrome(s[LCV: end])                             # Sets the value in the dictionary
            
         theSubstring = s[LCV: end] if palindromic[s[LCV: end]] and len(s[LCV: end]) > len(theSubstring) else theSubstring
         
   
   return theSubstring                                                        # sub string returned to the user


def isPalindrome(s):                                                          # Checking if a substring is a palindrome
   
   reversion = s[::-1]                                                        # Reverses the passed string
   
   #print(f"Comparing {reversion} and {s}: {reversion == s}")
   
   return reversion == s                                                      # Returns whether the two strings are the same

def main():

   s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
   
   print(f"The longest one is {longestOne(s)}")


main()