import json

counter = 0

def find_combinations(word, stickerList, stickerId, prefix='', depth=0):
    global counter # Zugriff auf die globale Variable

    # Basisfall: Wenn das Präfix das gegebene Wort ergibt, geben Sie es aus
    if word == '':
        counter += 1
        #print('{}: {}'.format(counter, stickerId))
        return
    
    # Basisfall: Wenn die maximale Tiefe erreicht ist, stoppen Sie die Rekursion
    if depth == 5:
        return
    
    # Durchlaufen Sie die Liste der Sticker
    for sticker in stickerList:
        # Extrahieren Sie die Buchstaben aus jedem Sticker-Text
        words = [x['letters'] for x in sticker['text']]

        # Durchlaufen Sie die extrahierten Buchstaben für jeden Sticker
        for text in words:

            # Präfix + aktueller Sticker-Text
            new_prefix = prefix + text
            
            if word.lower().startswith(new_prefix.lower()):
                i = 0
                
                for x in new_prefix.lower():
                    if x == word[i]:
                        i += 1
                    else:
                        break
                
                word = word[i:]
                stickerId.append(sticker['name'])
                return find_combinations(word, stickerList, stickerId, '', depth + 1)
                
            
            elif word.lower() in new_prefix.lower():
                i = 0
                
                for x in new_prefix.lower():
                    if i < len(word) and x == word[i]:
                        i += 1
                    else:
                        break
                
                word = word[i:]
                stickerId.append(sticker['name'])
                return find_combinations(word, stickerList, stickerId, new_prefix, depth + 1)

# Beispielaufruf
with open('data/stickerAll2.json', 'r', encoding='UTF-8') as f:
  stickerList = json.loads(f.read())
  word = "big dick".replace(' ', '')
  stickerId = []
  find_combinations(word, stickerList, stickerId)
  print(stickerId)