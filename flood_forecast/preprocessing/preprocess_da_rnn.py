from typing import Tuple
import typing
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from typing import List
from flood_forecast.da_rnn.custom_types import TrainData
    
def format_data(dat, targ_column:List[str]) -> Tuple[TrainData, StandardScaler]:
    proc_dat = dat.as_matrix()
    mask = np.ones(proc_dat.shape[1], dtype=bool)
    dat_cols = list(dat.columns)
    for col_name in targ_column:
        mask[dat_cols.index(col_name)] = False
    feats = proc_dat[:, mask].astype(float)
    targs = proc_dat[:, ~mask].astype(float)
    return TrainData(feats, targs)

def make_data(csv_path:str, target_col:List[str], test_length:int)->TrainData:
    """
    """
    final_df = pd.read_csv(csv_path)
    print(final_df.shape[0])
    total = len(final_df.index)-test_length
    final_df = final_df[:total]
    height_df = final_df[[target_col[0], 'precip', 'temp']]
    if len(target_col>1):
        # Restrict target columns to height and cfs
        height_df = final_df[[target_col[0], target_col[1], 'precip', 'temp']]
    height_df.columns = [target_col, 'precip', 'temp']
    preprocessed_data2 = format_data(height_df, target_col)
    return preprocessed_data2


