def lengthOfLongestSubstring(s: str):
    substrings = {}
    prev = ''
    longest = 0

    if s == '':
        return 0

    for letter in s:
        if letter not in prev:
            prev += letter
            substrings[prev] = len(prev)
        else:
            substrings[prev] = len(prev)
            prev = letter

    for key, value in substrings.items():
        if value > longest:
            longest = value

    return longest


print(lengthOfLongestSubstring('ca'))
print(lengthOfLongestSubstring('dvdf'))
