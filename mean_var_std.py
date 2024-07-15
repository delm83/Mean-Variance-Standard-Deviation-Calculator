import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    numparray = np.array(list)
    numpmatrix = numparray.reshape(3, 3)
    mean = [numpmatrix.mean(axis=0).tolist(), numpmatrix.mean(axis=1).tolist(), numpmatrix.mean().tolist()]
    var = [numpmatrix.var(axis=0).tolist(), numpmatrix.var(axis=1).tolist(), numpmatrix.var().tolist()]
    stddeviation = [numpmatrix.std(axis=0).tolist(), numpmatrix.std(axis=1).tolist(), numpmatrix.std().tolist()]
    max = [numpmatrix.max(axis=0).tolist(), numpmatrix.max(axis=1).tolist(), numpmatrix.max().tolist()]
    min = [numpmatrix.min(axis=0).tolist(), numpmatrix.min(axis=1).tolist(), numpmatrix.min().tolist()] 
    sum = [numpmatrix.sum(axis=0).tolist(), numpmatrix.sum(axis=1).tolist(), numpmatrix.sum().tolist()] 
    calculations = {'mean': mean, 'variance': var, 'standard deviation': stddeviation, 'max': max, 'min': min, 'sum': sum}
    return calculations