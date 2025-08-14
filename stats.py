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

def sort_on(items):
    return items["num"]

def sort_dic(chars):
    char_list = []
    for char, num in chars.items():
        new_dict = {"char" : char, "num" : num}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
