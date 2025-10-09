def group_anagram(array):
    if len(array) <= 1:
        return [array]
    anagrams = {}
    for word in array:
        sorted_word = ''.join(sorted(str(word)))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    for key in anagrams:
        anagrams[key].sort()
    return sorted(list(anagrams.values()), key=len)