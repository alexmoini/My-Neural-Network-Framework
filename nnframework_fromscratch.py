# -*- coding: utf-8 -*-
"""NNFramework_fromScratch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KkJYXUFV5VhkdOvy802zNMM9EPdg_lqi
"""

import numpy as np
import matplotlib as plt
import sys

"""# The Neuron"""

X = [ # init inputs of batch size 3 from 4 seperate neurons (3,4)
          [1,2,3,2.5],
          [2,5,-1,2],
          [-1.5,2.7,3.3,-.8],
          ]
np.random.seed(0)
# dense layer class
class layer_dense:
  def __init__(self, n_inputs, n_neurons):
    # randomly initialize weights and biases
    self.weights = .10 * np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros((1, n_neurons))
  def forward(self, inputs):
    # output inputs dot weights + bias for each individual neuron
    self.output = np.dot(inputs, self.weights) + self.biases

class relu_activation:
  def forward(self, inputs):
    # relu: if input is < 0, return 0, if larger, return input
    # this is used to delinearize neural networks, neural networks CANNOT fit
    # an unknown NONLINEAR function with completely linear layers, however with non-linear
    # activations, neural networks have been proven to be able to fit ANY function, linear or not
    self.output = np.maximum(0, inputs)
class softmax_activation:
  def forward(self, inputs):
    # softmax is an exponentiation then normalization of an input
    # this is important because with just a relu or linear function
    # certain problems arise. ie. with a relu function, negatives become
    # clipped to zero, so in a classification network, one output could be
    # -.99 and the other be -.1. A relu would output both as 0, so how can
    # some sort of post processing step get the correct prediction? or even
    # worse, how could the neural network run back propagation? the loss function
    # would be just as sensitive to both clipped inputs.
    exponentiate_input = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))
    normalize_input = exponentiate_input / np.sum(exponentiate_input, axis 1, keepdims = True))
    self.output = probabilities
class loss_function
  def calculate_loss(self, outputs, y):
    losses = self.forward(output, y)
    batch_loss = np.mean(losses)
    return batch_loss

class categorical_crossentropy(loss_function):
  def forward(self, y_pred, y_hat):
    samples = len(y_pred)
    clipped_pred = np.clip(y_pred, 1e-7, 1-1e-7)

# Activation functions