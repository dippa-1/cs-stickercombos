#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
import json
import threading
from flask import request
import os
from algo import create_starts_with_index, find_combinations
import numpy as np

app = Flask(__name__)
CORS(app)

all_stickers = []
if os.path.exists('data/stickerAll2.json'):
  with open('data/stickerAll2.json', 'r') as f:
    all_stickers = json.load(f)

labeled_data = []
if os.path.exists('data/labeledData.json'):
  with open('data/labeledData.json', 'r') as f:
    labeled_data = json.load(f)
  
unlabeled_data = list(filter(lambda s: 'name' not in s or s['name'] not in [sticker['name'] for sticker in labeled_data], all_stickers))
sticker_iterator = iter(unlabeled_data)
sticker_semaphore = threading.Semaphore()

index = {}
with open('index.json', 'r') as f:
  index = json.load(f)

def find_deepest_arrays(arr, result=None):
    """
    Recursively find the deepest arrays in a given numpy array and collect them.

    Parameters:
    - arr: numpy array of arbitrary dimensionality.
    - result: list to collect the deepest arrays. Should be None when called by user.

    Returns:
    - A list of the deepest arrays.
    """
    if result is None:
        result = []

    # Check if the array is of the lowest dimension (i.e., no more nested arrays)
    if arr.ndim == 1:
        result.append(arr)
    else:
        # Iterate through each item in the array and dive deeper
        for sub_arr in arr:
            find_deepest_arrays(sub_arr, result)

    return result

stickers_dict = {}
for sticker in all_stickers:
  stickers_dict[sticker['name']] = sticker

@app.route('/suggest/<word>', methods=['GET'])
def get_suggestion(word):
  print(f'GET /suggest/{word}')
  word = word.lower().replace(' ', '')
  result = find_combinations(word, index)
  arr = np.array(result)

  # with open('res.json', 'w') as f3:
  #   json.dump(result, f3, indent=2)

  deepest = np.array(find_deepest_arrays(arr))
  # with open('res-np.json', 'w') as f3:
  #   json.dump(deepest.tolist(), f3, indent=2)
    
  randoms = np.random.choice(len(deepest), 20)
  stickers = [list(map(lambda s: stickers_dict[s], deepest[i])) for i in randoms]
  
  # with open('res-final.json', 'w') as f3:
  #   json.dump(stickers, f3, indent=2)

  return stickers

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

@app.route('/label/<name>', methods=['GET'])
def get_label_data(name):
  print(f'GET /label/{name}')
  try:
    sticker = next(filter(lambda s: s['name'] == name, all_stickers))
    return sticker
  except StopIteration:
    return 'Sticker not found', 404

@app.route('/label/<name>', methods=['PUT'])
def create_label(name):
  print(f'PUT /label/{name}')
  data = request.get_json()
  if 'labels' not in data or 'rotation' not in data:
    return 'Invalid request', 400
  labels = data['labels']
  rotation = data['rotation']
  
  print(f'Creating label for {name} with labels {labels} and rotation {rotation}')
  try:
    new_label_data = next(filter(lambda s: s['name'] == name, all_stickers))
    new_label_data['text'] = list(map(lambda l: {'letters': l, 'rotation': rotation}, labels))
    labeled_data.append(new_label_data)
    with open('data/labeledData.json', 'w') as f:
      json.dump(labeled_data, f, indent=2)
    return 'Label created successfully', 201
  except StopIteration:
    return 'Sticker not found', 404

if __name__ == '__main__':
    app.run(debug=True)
