from nltk.tag import tnt
from nltk.corpus import indian
import nltk
from nltk.tree import Tree

#tokenization
from indicnlp.tokenize import indic_tokenize

#text="आजचे  वर्तमान उद्याचा	इतिहास आहे ."

#text="ती पाच क्रमांक खाली गेली आहे ."

text=""" सनातनवाद्यांनी व प्रतिगाम्यांनी समाज रसातळाला नेला असताना या अंधारात बाळशास्त्री जांभेकर
यांनी माध्यमातून पहिली ज्ञानज्योत तेववली , प्रतिपादन नटसम्राट प्रभाकर पणशीकर यांनी केले."""
print(text)
s=indic_tokenize.trivial_tokenize(text)
print(s)


#posTagging
def marathi_model():
    train_data = indian.tagged_sents('marathi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger

#keywordExtraction
def get_keywords(pos):
    grammar = r"""NP:{<NN.*>}"""
    chunkParser = nltk.RegexpParser(grammar)
    chunked = chunkParser.parse(pos)
    continuous_chunk = set()
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.add(named_entity)
                current_chunk = []
            else:
                continue
    return (continuous_chunk)

model = marathi_model()
new_tagged = (model.tag(nltk.word_tokenize(text)))
print(new_tagged)
print()
print("====KEYWORDS===")
print(get_keywords(new_tagged))
