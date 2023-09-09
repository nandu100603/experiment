def is_palindrome(s):
   #hello all
    s = s.replace(" ", "").lower()
    return s == s[::-1]
