def word_count(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def char_count(file_contents):
    erase_dupes = file_contents.lower()
    chars = {}
    for char in erase_dupes:
        
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
            
            
    return chars