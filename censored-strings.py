"""
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s.
Luckily, I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, 
return the original uncensored string.
"""

def uncensor(txt, vowels):
    for c in vowels: 
        txt = txt.replace("*", c, 1)
    return txt
    
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
