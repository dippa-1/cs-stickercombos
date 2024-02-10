import json

def find_combinations(word, stickerList, stickerId=[], depth=0):
    if word == '':
        return stickerId
    
    if depth == 5:
        return None
    
    for sticker in stickerList:
        words = [x['letters'] for x in sticker['text']]

        for text in words:
            text = text.lower().replace(' ', '')

            for i in range(len(text), 1, -1):
                if word.startswith(text[:i]):
                    new_word = word.replace(text[:i], '', 1)
                    stickerId.append(sticker)
                    result = find_combinations(new_word, stickerList, stickerId, depth + 1)
                    if result is not None:
                        return result
                    else:
                        stickerId.pop()
    return None

# Beispielaufruf
with open('data/stickerAll2.json', 'r', encoding='UTF-8') as f:
    stickerList = json.loads(f.read())
    word = "big dick"
    stickerId = []
    result = find_combinations(word.lower().replace(' ', ''), stickerList)
    print(result)