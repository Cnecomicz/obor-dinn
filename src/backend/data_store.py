from yaml import safe_load

with open("data/backend/words.yaml", "r") as file:
    WORDS_CACHE = safe_load(file)