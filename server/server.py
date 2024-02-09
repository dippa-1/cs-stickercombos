#!/usr/bin/env python3

from flask import Flask, jsonify
import json

app = Flask(__name__)

data = None
with open('data.json', 'r') as f:
  data = json.load(f)

# Endpoint to get all todos
@app.route('/suggest/<word>', methods=['GET'])
def get_todos(word):
  print(word)
  return data

if __name__ == '__main__':
    app.run(debug=True)
