import json

def find_combinations(word, stickerList, depth=0, used_stickers=None):
    if word == '':
        return used_stickers
    
    if depth == 5:
        return None
    
    if used_stickers is None:
        used_stickers = []

    possible_combinations = []
    
    for sticker in stickerList:
        words = [x['letters'] for x in sticker['text']]

        for text in words:
            text = text.lower().replace(' ', '')

            for i in range(len(text), 1, -1):
                if word.startswith(text[:i]):
                    new_word = word.replace(text[:i], '', 1)
                    new_used_stickers = used_stickers + [sticker]
                    result = find_combinations(new_word, stickerList, depth + 1, new_used_stickers)
                    if result is not None:
                        possible_combinations.append(result)

    if possible_combinations:
        return possible_combinations
    else:
        return None

# Beispielaufruf
with open('data/stickerAll2.json', 'r', encoding='UTF-8') as f:
    stickerList = json.loads(f.read())
    word = "big dick"
    result = find_combinations(word.lower().replace(' ', ''), stickerList)
    if result:
        for combination in result:
            print(combination)
    else:
        print("Keine passenden Kombinationen gefunden.")