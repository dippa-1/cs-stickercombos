#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
import json
import threading

app = Flask(__name__)
CORS(app)

all_stickers = None
with open('data/stickerAll.json', 'r') as f:
  all_stickers = json.load(f)
  
sticker_iterator = iter(all_stickers)
sticker_semaphore = threading.Semaphore()

def calculate_combinations(all_stickers, word):
  combinations = [get_stickers_starting_with(all_stickers, word)]
  return combinations

def get_stickers_starting_with(all_stickers, starting_with):
  return list(filter(lambda s: s['letters'].lower().startswith(starting_with), all_stickers))

@app.route('/suggest/<word>', methods=['GET'])
def get_suggestion(word):
  print(f'GET /suggest/{word}')
  return calculate_combinations(all_stickers, word)

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
