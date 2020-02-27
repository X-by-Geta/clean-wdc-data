import pandas as pd
from bs4 import BeautifulSoup
from ftfy import fix_text
import re

# Input parameters
category = 'Clothing'
dataset = 'offers_corpus_english_v2_non_norm'

datafilepath = 'output/{}'.format(dataset)
datafilename = '{}/{}.json.gz'.format(datafilepath, category)
cleanfilename = '{}/{}_clean.json.gz'.format(datafilepath, category)

df = pd.read_json(datafilename, compression='gzip', lines=True)

# Remove category column
df.drop('category', inplace=True, axis=1)
# Description is required
df = df[df.description.notnull()]
# Only keep English descriptions
df = df[df.description.str.contains('@en', regex=False)]

def remove_html_from_text(text):
    if text is None:
        return None
    
    # Remove html
    return BeautifulSoup(text, 'html.parser').get_text()

# Unwrap '\"text\"@en' to 'text'
# Only unwraps first string and discards the rest
def unwrap_text(text, start = "\"", end = "\"@en"):
    if text is None:
        return None

    start = text.find(start) + len(start)
    end = text.find(end)
    if (end == -1 or end < start):
        return text
    else:
        return text[start:end]

def remove_whitespace_from_text(text):
    if text is None or text == "Null":
        return None

    # Get rid of tabs
    text = re.sub('\t', ' ', text)
    # Get rid of duplicate whitespace
    text = re.sub(' {2,}', ' ', text)
    # Get rid of duplicate newlines
    text = re.sub('\n ', '\n', text)
    return re.sub('\n+', '\n', text).strip()

def has_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

def has_bracket(text):
    return '{' in text

def clean(text, remove_html = True, unwrap = True, remove_whitespace = True):
    if text is None:
        return None
    
    if has_cyrillic(text):
        return None

    if has_bracket(text):
        return None

    # Remove html
    if remove_html == True:
        result = remove_html_from_text(text)
    # Unwrap string
    if unwrap == True:
        result = unwrap_text(result)
    # Remove whitespace
    if remove_whitespace == True:
        result = remove_whitespace_from_text(result)
    # Run fix_text
    if result is not None:
        result = fix_text(result)
    return result

# Clean title, description, brand columns
df.title = [clean(title) for title in df.title]
df.description = [clean(description) for description in df.description]
df.brand = [clean(brand) for brand in df.brand]

# Ignore descriptions with multiple separate strings
# df = df[df.description.str.count("@en") == 1]

df = df[df.description.notnull()]

df.to_json(cleanfilename, orient='records', lines=True, compression='gzip')