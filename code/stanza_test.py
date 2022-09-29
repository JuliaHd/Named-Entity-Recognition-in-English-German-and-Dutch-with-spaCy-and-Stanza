"""Identifies named entities and then evaluates them with Stanza.

Uses a given Stanza pipeline to locate and tag named entities in a list of
sentences. If called, the module can calculate the precision, recall, and
F1-score of the previous annotation, using a spaCy pipeline.

Requires the packages "spacy", "stanza", and "time".

Example:
    example_lang_sent = ["I like London.", "His name is Peter Parker."]
    example_results = named_entity_recognition_st(example_lang_sent, nlp_en)
    example_results_eval = evaluate_ner_st(example_results, nlp_en3)

Attributes:
    start_time_all (float): Tracks CPU time across the entire module.
    nlp_de (Pipeline): The German Stanza pipeline. Processors can be adjusted.
    nlp_en (Pipeline): The English Stanza pipeline. Processors can be adjusted.
    nlp_nl (Pipeline): The Dutch Stanza pipeline. Processors can be adjusted.
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
import stanza
import time

from spacy.training import Example
from spacy.scorer import Scorer

start_time_all = time.process_time()

#stanza.download('de')  # Only use if German pipeline is not installed yet.
#stanza.download('en')  # Only use if English pipeline is not installed yet.
#stanza.download('nl')  # Only use if Dutch pipeline is not installed yet.

nlp_de = stanza.Pipeline('de', verbose=False, processors='tokenize, ner', use_gpu=True) 
nlp_en = stanza.Pipeline('en', verbose=False, processors='tokenize, ner', use_gpu=True) 
nlp_nl = stanza.Pipeline('nl', verbose=False, processors='tokenize, ner', use_gpu=True)

# spaCy

# German
nlp_de2 = spacy.load("de_core_news_md")
nlp_de3 = spacy.load("de_core_news_lg")

# English
nlp_en2 = spacy.load("en_core_web_md")
nlp_en3 = spacy.load("en_core_web_lg")

# Dutch
nlp_nl2 = spacy.load("nl_core_news_md")
nlp_nl3 = spacy.load("nl_core_news_lg")

# Multi-language
nlp_multi = spacy.load("xx_ent_wiki_sm")

#example_lang_sent = ["I like London.", "His name is Peter Parker."]

results = []
def named_entity_recognition_st(lang_sent, nlp_model):
    """Locates and tags named entities.

    Args:
        lang_sent (list[str]): A list of sentences.
        nlp_model (Language): An NLP model that matches the language of
            lang_sent. Use a Stanza model.

    Returns:
        list[tuple]: A list of trained sentences in tuples of the format 
            [('Sentence.', [[start_char, end_char, 'entity_type']])]

    """

    try:
        in_docs = [stanza.Document([], text=d) for d in lang_sent]  # Wrap each sentence in lang_sent in stanza.Document object.
        out_docs = nlp_model(in_docs)
        for sent in out_docs:
            #print(sent.text)  # Print all sentences.
            sentences = str(sent.text)
            entities = []
            for ent in sent.ents:
                entities.append([ent.start_char, ent.end_char, ent.type])
                results.append([sentences, entities])
            #print(results)
        result_tuples = [tuple(x) for x in results]
        #print(result_tuples)
        return result_tuples
        
    except Exception as e: print(e)

#example_results = named_entity_recognition_st(example_lang_sent, nlp_en)

def evaluate_ner_st(examples, nlp_model):
    """Evaluates accuracy in precision, recall, and F1-score with spaCy model.

    The spaCy NLP model evaluates the accuracy of the tags in the 
    previously-tagged/ trained sentences.

    Args:
        examples (list[tuple]): List of tagged tuples in the format 
            [('Sentence.', [[start_char, end_char, 'ENTITY_TYPE']])].
        nlp_model (Language): The NLP model used for evaluation. It must match
            the language of examples. Use a spaCy model.

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

#example_results_eval = evaluate_ner_st(example_results, nlp_en3)

end_time_all = time.process_time()
print("Time: ", end_time_all - start_time_all)  

print("Stanza successful.")
