def minion_game(s):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    try:
        for i in range(len(s)):
            if s[i] in vowels:
                kevin += (len(s)-i)
            else:
                stuart += (len(s)-i)

        if kevin > stuart:
            print("Kevin", kevin)
        elif kevin < stuart:
            print("Stuart", stuart)
        else:
            print("Draw")
    except:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    
'''
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string,
.
Both players have to make substrings using the letters of the string
.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string
.
'''
