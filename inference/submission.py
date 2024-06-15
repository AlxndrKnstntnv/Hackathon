import json
import spacy
from spacy.tokens import DocBin

with open('./test.json', encoding='UTF8') as file:
    data = json.load(file)

nlp = spacy.load('./output/model-last')

def get_list_of_entities(text):
  doc = nlp(text)

  target_entities = []

  for ent in doc.ents:
    target_entities.append(ent.text)
  return target_entities

result = []

for el in data:
  dct = {}
  dct['id'] = el['id']
  dct['title'] = el['title']
  dct['skills'] = get_list_of_entities(el['desc'])
  result.append(dct)

with open('submission.json', 'w') as f:
    json.dump(result, f, indent=4)