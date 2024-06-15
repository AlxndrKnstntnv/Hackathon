import spacy
import subprocess

subprocess.run('! python -m spacy train config.cfg --output ./output --paths.train ./new_train.spacy --paths.dev ./new_dev.spacy', check=True)