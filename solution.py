import pandas as pd
import numpy as np


chat_id = 38897891  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import anderson_ksamp
    pval = anderson_ksamp([x, y]).pvalue
    res = pval < 0.06
    return res
