#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
import json
import threading

app = Flask(__name__)
CORS(app)

all_stickers = None
with open('data/stickerAll2.json', 'r') as f:
  all_stickers = json.load(f)
  
sticker_iterator = iter(all_stickers)
sticker_semaphore = threading.Semaphore()

def find_combinations(word, stickerList, stickerId, prefix='', depth=0):
    # Basisfall: Wenn das Präfix das gegebene Wort ergibt, geben Sie es aus
    if word == '':
        counter += 1
        #print('{}: {}'.format(counter, stickerId))
        return stickerId
    
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
                stickerId.append(sticker)
                return find_combinations(word, stickerList, stickerId, '', depth + 1)
                
            
            elif word.lower() in new_prefix.lower():
                i = 0
                
                for x in new_prefix.lower():
                    if i < len(word) and x == word[i]:
                        i += 1
                    else:
                        break
                
                word = word[i:]
                stickerId.append(sticker)
                return find_combinations(word, stickerList, stickerId, new_prefix, depth + 1)
            
# def calculate_combinations(all_stickers, word):
#   combinations = [get_stickers_starting_with(all_stickers, word)]
#   return combinations

# def get_stickers_starting_with(all_stickers, starting_with):
#   return list(filter(lambda s: s['letters'].lower().startswith(starting_with), all_stickers))

@app.route('/suggest/<word>', methods=['GET'])
def get_suggestion(word):
  print(f'GET /suggest/{word}')
  result_list = []
  find_combinations(word, all_stickers, result_list)
  return result_list

@app.route('/label/next', methods=['GET'])
def get_next_label():
  print('GET /label/next')
  sticker_semaphore.acquire()
  try:
    sticker = next(sticker_iterator)
    sticker_semaphore.release()
    return sticker
  except StopIteration:
    sticker_semaphore.release()
    return 'No more stickers', 404

if __name__ == '__main__':
    app.run(debug=True)
