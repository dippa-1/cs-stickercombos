#!/usr/bin/env python3

from flask import Flask
import json

app = Flask(__name__)

all_stickers = None
with open('data/stickerAll.json', 'r') as f:
  all_stickers = json.load(f)

def calculate_combinations(all_stickers, word):
  combinations = [get_stickers_starting_with(all_stickers, word)]
  return combinations

def get_stickers_starting_with(all_stickers, starting_with):
  return list(filter(lambda s: s['letters'].lower().startswith(starting_with), all_stickers))

@app.route('/suggest/<word>', methods=['GET'])
def get_suggestion(word):
  print(f'GET /suggest/{word}')
  return calculate_combinations(all_stickers, word)

if __name__ == '__main__':
    app.run(debug=True)
