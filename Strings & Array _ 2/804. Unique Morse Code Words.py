from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
        'a': ".-",   'b': "-...", 'c': "-.-.", 'd': "-..",  'e': ".",    
        'f': "..-.", 'g': "--.",  'h': "....", 'i': "..",   'j': ".---", 
        'k': "-.-",  'l': ".-..", 'm': "--",   'n': "-.",   'o': "---",  
        'p': ".--.", 'q': "--.-", 'r': ".-.",  's': "...",  't': "-",    
        'u': "..-",  'v': "...-", 'w': ".--",  'x': "-..-", 'y': "-.--", 
        'z': "--.."
        }
        transformation = set()
        for word in words:
            morse_word = "".join(morse_dict[char] for char in word)

            transformation.add(morse_word)
        return len(transformation)