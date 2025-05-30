# skill_extractor.py
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")
skills_df = pd.read_csv("full_tech_skills_list.csv")
valid_skills = set(skills_df['skill'].str.lower().str.strip())

def extract_skills_from_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    return sorted(set(token for token in tokens if token in valid_skills))




# from transformers import pipeline

# # Load a named entity recognition pipeline
# ner = pipeline("ner", grouped_entities=True, model="dslim/bert-base-NER")

# def extract_skills_from_text(text):
#     entities = ner(text)
#     skills = [e['word'] for e in entities if e['entity_group'] == 'MISC']  # OR customize to your dataset
#     return list(set(skill.strip() for skill in skills))
