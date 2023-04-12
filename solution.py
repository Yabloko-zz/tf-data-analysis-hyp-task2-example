import pandas as pd
import numpy as np


chat_id = 38897891  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import cramervonmises_2samp
    stat, p = cramervonmises_2samp(x, y)
    res = p < 0.06
    return res
