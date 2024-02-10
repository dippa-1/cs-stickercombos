import json


def find_combinations(word, stickerList, stickerId=[], depth=0):
    if word == '':
        return stickerId
    
    if depth == 5:
        return
    
    for sticker in stickerList:
        # Extrahieren Sie die Buchstaben aus jedem Sticker-Text
        words = [x['letters'] for x in sticker['text']]

        # Durchlaufen Sie die extrahierten Buchstaben für jeden Sticker
        for text in words:
            text = text.lower().replace(' ', '')

            for i in range(len(text), 1, -1):
                if word.startswith(text[:i]):
                    new_word = word.replace(text[:i], '', 1)
                    stickerId.append(sticker)
                    find_combinations(new_word, stickerList, stickerId, depth + 1)
        

# Beispielaufruf
with open('data/stickerAll2.json', 'r', encoding='UTF-8') as f:
  stickerList = json.loads(f.read())
  word = "big dick"
  stickerId = []
  result = [find_combinations(word.lower().replace(' ', ''), stickerList)]
  print(result)