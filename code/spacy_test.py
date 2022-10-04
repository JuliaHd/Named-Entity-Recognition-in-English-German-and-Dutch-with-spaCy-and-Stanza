"""Identifies named entities and then evaluates them with spaCy.

Uses a given spaCy pipeline to locate and tag named entities in a list of
sentences. If called, the module can calculate the precision, recall, and
F1-score of the previous annotation.

Requires the package "spacy" and "time".

Example:
    example_lang_sent = ["I like London.", "His name is Peter Parker."]
    example_results = named_entity_recognition_sp(example_lang_sent, nlp_en2)
    example_results_eval = evaluate_ner_sp(example_results, nlp_en3)

Attributes:
    start_time_all (float): Tracks CPU time across the entire module.
    nlp_de2 (Language): German medium-size pipeline in spaCy. Second out of 
        four pipelines for German.
    nlp_de3 (Language): German large pipeline in spaCy. Third out of four 
        pipelines for German.
    nlp_en2 (Language): English medium-sized pipeline in spaCy. Second out of
        four pipelines for English.
    nlp_en3 (Language): English large pipeline in spaCy. Third out of four
        pipelines for English.
    nlp_nl2 (Language): Dutch medium-sized pipeline in spaCy. Second out of
        three pipelines for Dutch.
    nlp_nl3 (Language): Dutch large pipeline in spaCy. Third out of three
        pipelines for Dutch.
    nlp_multi (Language): Multi-language pipeline in spaCy focused on named 
        entity recognition.
    example_lang_sent (list[str]): Example format of to-be-annotated sentences.
    results (list): List that results from named_entity_recognition_sp are 
        appended to.
    example_results (list[tuple]): Example of named_entity_recognition_sp
        application.
    example_results_eval (Dict[str, Any]): Example of evaluate_ner_sp 
        application.
    end_time_all (float): Tracks CPU time. Used to calculate total run-time of
        this module.

"""

import spacy
import time

from spacy.training import Example
from spacy.scorer import Scorer

start_time_all = time.process_time()

# German
#nlp_de1 = spacy.load("de_core_news_sm")
nlp_de2 = spacy.load("de_core_news_md")
nlp_de3 = spacy.load("de_core_news_lg")

# English
#nlp_en1 = spacy.load("en_core_web_sm")
nlp_en2 = spacy.load("en_core_web_md")
nlp_en3 = spacy.load("en_core_web_lg")
#nlp_en4 = spacy.load("en_core_web_trf")

# Dutch
#nlp_nl1 = spacy.load("nl_core_news_sm")
nlp_nl2 = spacy.load("nl_core_news_md")
nlp_nl3 = spacy.load("nl_core_news_lg")

# Multi-language
nlp_multi = spacy.load("xx_ent_wiki_sm")

#example_lang_sent = ["I like London.", "His name is Peter Parker."]

results = []
def named_entity_recognition_sp(lang_sent, nlp_model):
    """Locates and tags named entities.

    Args:
        lang_sent (list[str]): A list of sentences.
        nlp_model (Language): An NLP model that matches the language of
            lang_sent.

    Returns:
        list[tuple]: A list of trained sentences in tuples of the format 
            [('Sentence.', [[start_char, end_char, 'entity_type']])].

    """

    try:
        for sentence in lang_sent:
            doc = nlp_model(sentence)
            entities = []
            for ent in doc.ents:
                entities.append([ent.start_char, ent.end_char, ent.label_])
                results.append([sentence, entities])
        #print(results)
        result_tuples = [tuple(x) for x in results]
        return result_tuples

    except Exception as e: print(e)

#example_results = named_entity_recognition_sp(example_lang_sent, nlp_en2)
#print(example_results)

def evaluate_ner_sp(examples, nlp_model):
    """Evaluates accuracy in precision, recall, and F1-score.

    The spaCy NLP model evaluates the accuracy of the tags in the 
    previously-tagged/ trained sentences.

    Args:
        examples (list[tuple]): List of tagged tuples in the format 
            [('Sentence.', [[start_char, end_char, 'ENTITY_TYPE']]), (...)].
        nlp_model (Language): The NLP model used for evaluation. It must match
            the language of examples.

    Returns:
        Dict[str, Any]: The precision, recall, and F1-score in total and per
            entity type as well as the tokenization accuracy. Other categories
            receive None.

    Raises:
        UserWarning: [W030] Some entities could not be aligned in the text.

    """

    try:
        scorer = Scorer()
        examples_list = []
        for input_, annot in examples:
            doc = nlp_model.make_doc(str(input_))  # Creates spaCy Doc which contains predictions.
            example = Example.from_dict(doc, {"entities": annot})  # Example object which is the gold standard.
            example.predicted = nlp_model(input_)  # NLP model makes predictions on the input.
            examples_list.append(example)        
        return scorer.score(examples_list)  # Calculates the score of example_list.

    except Exception as e: print(e)

#example_results_eval = evaluate_ner_sp(example_results, nlp_en3)
#print(example_results_eval)

end_time_all = time.process_time()
print("Time: ", end_time_all - start_time_all)  

print("SpaCy successful.")

# named entity labels by language:
# German: LOC, MISC, ORG, PER
# English: CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART
# Dutch: CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART
# Multi-language: LOC, MISC, ORG, PER

#print(spacy.explain("LOC"))

# LOC: Non-GPE locations, mountain ranges, bodies of water
# MISC: Miscellaneous entities, e.g. events, nationalities, products or works of art
# ORG: Companies, agencies, institutions, etc.
# PER: Named person or family.

# CARDINAL: Numerals that do not fall under another type
# DATE: Absolute or relative dates or periods
# EVENT: Named hurricanes, battles, wars, sports events, etc.
# FAC: Buildings, airports, highways, bridges, etc.
# GPE: Countries, cities, states
# LANGUAGE: Any named language
# LAW: Named documents made into laws.
# MONEY: Monetary values, including unit
# NORP: Nationalities or religious or political groups
# ORDINAL: "first", "second", etc.
# PERCENT: Percentage, including "%"
# PERSON: People, including fictional
# PRODUCT: Objects, vehicles, foods, etc. (not services)
# QUANTITY: Measurements, as of weight or distance
# TIME: Times smaller than a day
# WORK_OF_ART: Titles of books, songs, etc.
