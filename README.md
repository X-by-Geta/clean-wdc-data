# Extracting data from the WDC Product Data Corpus

This library can be used to extract a specific product category from the [WDC Product Data Corpus and Gold Standard for Large-Scale Product Matching - Version 2.0][0] dataset. It also does some preliminary parsing and cleaning.

## Run using docker

```sh
docker build -t clean-wdc-dataset .
docker run --rm -m 4g -it -v ${PWD}:/home/ clean-wdc-dataset
```

Or download the [dataset][1] and place it in the `dataset\` folder.

## Files

- `extract_category.py`
  - Can be used to extract one Category subset, e.g. Clothing
- `clean_dataset.py`
  - Script to clean up the data
  - Strip html, whitespace
  - Only keep strings with locale `@en`
- `stats.py`
  - Displays some stats about the Category subset
- `run.sh`
  - Downloads the dataset, runs `extract_category`, `clean_dataset` and `stats`

[0]: http://webdatacommons.org/largescaleproductcorpus/v2/index.html
[1]: http://data.dws.informatik.uni-mannheim.de/largescaleproductcorpus/data/v2_nonnorm/offers_corpus_english_v2_non_norm.json.gz