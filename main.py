word = list('hello')
vowels = 'aeiou'
l_ind = 0
r_ind = len(word) - 1
while l_ind < r_ind:
    if word[l_ind] in vowels and word[r_ind] in vowels:
        word[l_ind], word[r_ind] = word[r_ind], word[l_ind]
        l_ind += 1
        r_ind -= 1
    elif word[l_ind] not in vowels:
        l_ind += 1
    else:
        r_ind -= 1
print(''.join(word))