import util

file_path = 'module-1\Week-2\P1_data.txt'
word_statistic = {}

with open(file_path, 'r') as f:
    sentence = f.read()
    # sentence = util.preprocess_text(sentence)
print(type(sentence))
print(sentence)


words = util.preprocess_text(sentence)

for w in words:
    if w in word_statistic:
        word_statistic[w] += 1
    else:
        word_statistic[w] = 1
        
print(word_statistic)
