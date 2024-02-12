import re
s = "A man, a plan, a canal: Panama"
clean_str = re.sub(r'[^A-Za-z0-9]', '', s.lower())
if clean_str == clean_str[::-1]:
    print('PALINDROME')
else:
    print('NON PALINDROME')
#cleaned_  = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
print(clean_str)

#re.sub() is a method in Python's re module that is used for string substitution using regular expressions. Its primary purpose is to search for a specified pattern (regular expression) in a string and replace occurrences of that pattern with a specified replacement.
# re.sub(pattern, replacement, string, count=0, flags=0)