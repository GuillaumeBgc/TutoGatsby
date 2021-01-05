from spacy.lang.en import English

nlp = English()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Criar uma lista de padrões de correspondência para o PhraseMatcher
patterns = [nlp(person) for person in people]
