import pickle
import numpy as np
import pandas as pd
from pprint import pprint

resdict = dict()

def add(filename):
    with open(filename, 'rb') as f:
        resdict.update(pickle.load(f))
    print('added')
    
def dump(filename):
    with open(filename, 'wb') as f:
        pickle.dump(resdict, f)
    print('dumped')

def check():
    print('len: {}'.format(len(resdict)))
