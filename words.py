import csv
import os

def get_words_from_file(file_path):
    words_list = []
    with open(os.path.join(file_path), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for word in reader:
            words_list.append(word)
    return words_list[0]

vocabulary_lists_files = os.listdir('./vocabulary_lists')

existing_words = []
for file in vocabulary_lists_files:
    existing_words.append(get_words_from_file(os.path.join('./vocabulary_lists', file)))
existing_words = sum(existing_words, [])

unlearable_list = get_words_from_file('./unlearnable.csv')
tentative_list = get_words_from_file('./tentative.csv')

new_word_list = list(set(tentative_list) - set(unlearable_list) - set(existing_words))

with open('./learnable.csv', 'w') as learnable_file:
    count = 0
    for word in new_word_list:
        if count >= 500:
            learnable_file.write('\n --500-- \n')
            count = 0
        learnable_file.write(word)
        learnable_file.write(',')
        count = count + 1

print(f'Existing Words:{len(existing_words)}\nUnlearnable Words:{len(unlearable_list)}\nTentative List:{len(tentative_list)}\nNew Words:{len(new_word_list)}')

#last comma at the end of csv being read as blank word
#auto make files of 500 words