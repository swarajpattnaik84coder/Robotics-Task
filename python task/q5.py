#anagram

def brute_force_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if brute_force_anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")