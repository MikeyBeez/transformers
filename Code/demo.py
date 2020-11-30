#!/usr/bin/env python3

from absl import app, flags, logging

import torch as th
import pytorch_lightning as pl

import nlp
import transformers

FLAGS = flags.FLAGS

def main(_):
    logging.info('hello')

if __name__ == '__main__':
    app.run(main)


