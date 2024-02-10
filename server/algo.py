import json

counter = 0

def find_combinations(word, stickerList, prefix='', depth=0, stickerId=''):
    global counter # Zugriff auf die globale Variable

    # Basisfall: Wenn das Präfix das gegebene Wort ergibt, geben Sie es aus
    if word.lower() in prefix.lower():
        counter += 1
        print('{}: {} | {} | {}'.format(counter, word, prefix, stickerId))
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
            
            # Wenn das neue Präfix ein Präfix des gegebenen Wortes ist,
            # rufen Sie die Funktion rekursiv mit dem neuen Präfix auf
            if new_prefix.lower().startswith(word.lower()):
                find_combinations(word, stickerList, new_prefix, depth + 1, sticker['name'])
            
            # Wenn der aktuelle Sticker-Text ein Teilstring des gegebenen Wortes ist,
            # rufen Sie die Funktion rekursiv mit dem neuen Präfix auf
            if new_prefix.lower() in word.lower():
                find_combinations(word, stickerList, new_prefix, depth + 1, sticker['name'])

# Beispielaufruf
with open('data/stickerAll2.json', 'r', encoding='UTF-8') as f:
  stickerList = json.loads(f.read())
  word = "Good Evil"
  find_combinations(word, stickerList)