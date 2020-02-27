import pandas as pd
from pathlib import Path

# Input parameters
category = 'Clothing'
filename = 'offers_corpus_english_v2_non_norm'

# Settings
inputfile = 'dataset/{}.json.gz'.format(filename)
outputpath = 'output/{}'.format(filename)
outputfile = '{}/{}.json.gz'.format(outputpath,category)
chunksize = 100000
Path(outputpath).mkdir(parents=True, exist_ok=True)

def category_filter(chunk):
    return chunk.category == category

chunk_list = []
# Each chunk is in df format
for chunk in pd.read_json(inputfile, compression='gzip', lines=True, chunksize=chunksize):
    # Once the data filtering and append the chunk to list (in memory)
    chunk_list.append(chunk.loc[category_filter(chunk)])

# Concat and store as json (gzip)
df_concat = pd.concat(chunk_list)
df_concat.to_json(outputfile, orient='records', lines=True, compression='gzip')