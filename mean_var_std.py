import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    m = np.array(list).reshape(3, 3)

    m_mean = [m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), m.mean()]
    m_variance = [m.var(axis=0).tolist(), m.var(axis=1).tolist(), m.var()]
    m_standard_deviation = [m.std(axis=0).tolist(), m.std(axis=1).tolist(), m.std()]
    m_max = [m.max(axis=0).tolist(), m.max(axis=1).tolist(), m.max()]
    m_min = [m.min(axis=0).tolist(), m.min(axis=1).tolist(), m.min()]
    m_sum = [m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), m.sum()]
    
    calculations = {
        'mean': m_mean,
        'variance': m_variance,
        'standard deviation': m_standard_deviation,
        'max': m_max,
        'min': m_min,
        'sum': m_sum
    }

    return calculations