import numpy as np
import os
import pandas as pd

a = pd.read_csv('input.csv')
for i in range(0,len(a),2):
    #print(a.loc[i]['SMILES'])
    dfl = pd.DataFrame(data={'SMILES':[a.iloc[i,0]],'label':[a.iloc[i,1]]})
    dfr = pd.DataFrame(data={'SMILES':[a.iloc[i+1,0]],'label':[a.iloc[i+1,1]]})
    df = pd.concat([dfl,dfr],axis=0)
    df.to_csv(f'double{i}.csv',index=False)
    try:
        os.system(f'chemprop_train.exe --data_path double{i}.csv --save_dir "test{i}" \
                --dataset_type classification --split_sizes 0.5 0.5 0 --split_type scaffold_balanced \
                > output{i}.log 2>&1') 
        with open('readable_mols.txt','a') as f:
            f.write(f'{i}\t{a.iloc[i,0]}\n{i+1}\t{a.iloc[i+1,0]}\n')
    except IndexError as e:
        with open('kekulize_error.txt', 'a') as f:
            f.write(f'{i}\t{a.iloc[i,0]}\t{e}\n')
    except Exception as e:
        with open('valence_error.txt', 'a') as f:
            f.write(f'{i}\t{a.iloc[i,0]}\t{e}\n')


