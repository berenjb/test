import pandas as pd
import numpy as np

# -- Create Dummy Data -- #

def create_col_a():
    foo = ['a', 'b', 'c', 'd', 'e']
    return(np.random.choice(foo))

def create_col_b():
    foo = [0,1]
    return(np.random.choice(foo))

df = pd.DataFrame({"a_": [create_col_a() for i in range(0,200)],
                   "b_": [create_col_b() for i in range(0,200)]})


# -- Create Stratified Folds -- #

from sklearn.cross_validation import StratifiedKFold
label = df.pop('b_')

skf = StratifiedKFold(label,n_folds=5)

for train, test in skf:
    print("{},{}".format(train,test))

print("Newly Added Line...")



