#!/usr/bin/env python3

from absl import app, flags, logging

import torch as th
import pytorch_lightning as pl
import numpy as np
import nlp
import transformers

FLAGS = flags.FLAGS

class IMDBSentimentClassifier(pl.lighteningModule):
    def __init__(self):
        super().__init__()
    def prepare_data(self):
        pass
    def forward(self, batch):
        pass
    def training_step(self, batch, batch_idx):
        pass
    def train_dataloader(self):
        pass

def main(_):
    logging.info('hello')

if __name__ == '__main__':
    app.run(main)


