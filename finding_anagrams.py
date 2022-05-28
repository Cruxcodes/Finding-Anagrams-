
# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# This is the function to check if both values are anagrams
def find_anagram(word, anagram):
    word_len = 0
    while word_len < len(anagram):
        if word.__contains__(anagram[word_len]) and len(word) == len(anagram):
            return True
        else:
            return False
            break
        word_len = word_len+1

# This is the section to collect inputs from the user
firstWord = input('Please input the first word:\n')
secondWord = input('Please input the second word for comparison:\n')

# First instance for the anagram function to run
print('The words being anagrams are',find_anagram(firstWord, secondWord))

# Asks if the user wants to re-run the code
re_run = input('\nWould u like to check other values: (y to continue)')
while re_run == 'y':
    # Runs as the use inputs y
    firstWord = input('Please input the first word:\n')
    secondWord = input('Please input the second word for comparison:\n')
    print('The words being anagrams are', find_anagram(firstWord, secondWord))
    re_run = input('\nWould u like to check other values: (y to continue)')
