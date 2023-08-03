def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_list = []

    for ch in sentence.lower():
        if ch not in alpha_list:
            alpha_list.append(ch)

    for i in range(len(alpha_list)):
        if alpha_list[i] in alphabet:
            alphabet = alphabet[:alphabet.find(alpha_list[i])] + alphabet[alphabet.find(alpha_list[i])+1:]
    
    if alphabet:
        return False
    return True