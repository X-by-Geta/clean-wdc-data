import pandas as pd

# Input parameters
category = 'Clothing'
dataset = 'offers_corpus_english_v2_non_norm'

datafilepath = 'output/{}'.format(dataset)
datafilename = '{}/{}.json.gz'.format(datafilepath, category)
datafilename_clean = '{}/{}_clean.json.gz'.format(datafilepath, category)

df = pd.read_json(datafilename, compression='gzip', lines=True)
df_clean = pd.read_json(datafilename_clean, compression='gzip', lines=True)

print('Statistics for: "{}"-"{}"'.format(dataset, category))
print('------------------------')
print('Total: {}'.format(df.id.count()))
with_description = df[df.description.notnull()].copy()
print('With description: {}'.format(with_description.id.count()))
with_at = with_description[with_description.description.str.contains("\"@", regex=False)]
print('With a locale marker: {}'.format(with_at.id.count()))
with_at_en = with_at[with_at.description.str.contains('@en', regex=False)]
print('With locale marker @en in description: {}'.format(with_at_en.id.count()))
print('Clean: {}'.format(df_clean.id.count()))