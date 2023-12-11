def word_frequency(sentence):
    frequency_dict = {}
    words = sentence.lower().split()
    
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict
    pass

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)