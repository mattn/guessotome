#!/usr/bin/env python3

import json
from flask import Flask, request
from guesslang import Guess

app = Flask(__name__)
guess = Guess()

def main():
  app.run()

@app.route('/', methods=['POST'])
def index():
  print(request.form['text'])
  return json.dumps({"lang": guess.language_name(request.form['text'])})

if __name__ == '__main__':
  main()

