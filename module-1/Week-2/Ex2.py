import util

sentence = input('Word to check: ')
sentence = util.preprocess_text(sentence)

character_statistic = {}

print(sentence)

for character in sentence:
    if character in character_statistic:
        character_statistic[character] += 1
    else:
        character_statistic[character] = 1
        
print(character_statistic)