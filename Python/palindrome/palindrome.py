def is_palindrome(s):
   #hello 
    s = s.replace(" ", "").lower()
    return s == s[::-1]
