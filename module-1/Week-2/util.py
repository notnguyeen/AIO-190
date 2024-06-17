def preprocess_text(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('.', '').replace(',', '')
    sentence = sentence.split()
    # sentence = ' '.join(sentence)
    return sentence

