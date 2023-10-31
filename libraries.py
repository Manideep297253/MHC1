import os
import pickle
from flask import Flask, render_template, request

# load trained model and count vectorizer from disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# load tfidf vectorizer
filename = 'finalized_vectorizer.sav'
loaded_vectorizer = pickle.load(open(filename, 'rb'))
