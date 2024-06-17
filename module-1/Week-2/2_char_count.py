import util

sentence = input('Words to check: ')
character = util.preprocess_text(sentence)

character_statistic = {}

print(character)

for character in sentence:
    if character in character_statistic:
        character_statistic[character] += 1
    else:
        character_statistic[character] = 1
        
print(character_statistic)