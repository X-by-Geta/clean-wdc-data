#!/bin/sh
datasetdir="/home/dataset"
[ ! -d "$datasetdir" ] && mkdir -p "$datasetdir"
wget -nc http://data.dws.informatik.uni-mannheim.de/largescaleproductcorpus/data/v2_nonnorm/offers_corpus_english_v2_non_norm.json.gz -O "${datasetdir}/offers_corpus_english_v2_non_norm.json.gz"

python "/home/extract_category.py"
python "/home/clean_dataset.py"
python "/home/stats.py"
