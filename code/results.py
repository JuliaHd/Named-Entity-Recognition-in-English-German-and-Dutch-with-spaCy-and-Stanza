"""Prints results.

Imports and executes functions from spacy_test.py and stanza_test.py on
lists from corpora.py. If desired, the results of named_entity_recognition_sp/
named_entity_recognition_st can be exported to a .csv file with pandas. This 
file is purely for legibility and should not be used before further editing.

This module requires "pandas", "time", "csv", "spacy", and "stanza".

Example:
    Follow the naming of the variables and run one pipeline and its evaluation at a
    time. Otherwise, the results will be skewed::
    
        ger_sp_results_nlp_de2 = named_entity_recognition_sp(ger_sent[:163111], nlp_de2)
        print(ger_sp_results_nlp_de2)  # Optional.
        ger_sp_results_nlp_de2_eval = evaluate_ner_sp(ger_sp_results_nlp_de2, nlp_de3)
        print(ger_sp_results_nlp_de2_eval)
        export_to_csv(ger_sp_results_nlp_de2)  # Optional.

Attributes:
    start_time_all (float): Tracks CPU time across the entire module.
    start_time_ger (float): Tracks CPU time for German.
    ger_sp_results_nlp_de2 (list[tuple]): List of tagging results for German
        with the spaCy medium pipeline.
    ger_sp_results_nlp_multi (list[tuple]): List of tagging results for German
        with the spaCy multi-language pipeline.
    ger_sp_results_nlp_de2_eval (Dict[str, Any]): Dictionary of the evaluation
        results for German with the spaCy large pipeline used for evaluation.
    ger_sp_results_nlp_multi_eval (Dict[str, Any]): Dictionary of the 
        evaluation results for German with the spaCy large pipeline used for
        evaluation.
    end_time_ger (float): Tracks CPU time. Used to calculate total run-time of
        German.
    start_time_eng (float): Tracks CPU time for English.
    eng_sp_results_nlp_en2 (list[tuple]): List of tagging results for English
        with the spaCy medium pipeline.
    eng_sp_results_nlp_multi (list[tuple]): List of tagging results for English
        with the spaCy multi-language pipeline.
    eng_sp_results_nlp_en2_eval (Dict[str, Any]): Dictionary of the evaluation
        results for English with the spaCy large pipeline used for evaluation.
    eng_sp_results_nlp_multi_eval (Dict[str, Any]): Dictionary of the 
        evaluation results for English with the spaCy large pipeline 
        used for evaluation.
    end_time_eng (float): Tracks CPU time. Used to calculate total run-time of
        English.
    start_time_nld (float): Tracks CPU time for Dutch.
    nld_sp_results_nlp_nl2 (list[tuple]): List of tagging results for Dutch
        with the spaCy medium pipeline.
    nld_sp_results_nlp_multi (list[tuple]): List of tagging results for Dutch
        with the spaCy multi-language pipeline.
    nld_sp_results_nlp_nl2_eval (Dict[str, Any]): Dictionary of the evaluation
        results for Dutch with the spaCy large pipeline used for evaluation.
    nld_sp_results_nlp_multi_eval (Dict[str, Any]): Dictionary of the 
        evaluation results for Dutch with the spaCy large pipeline used for
        evaluation.
    end_time_nld (float): Tracks CPU time. Used to calculate total run-time of
        Dutch.
    end_time_spacy (float): Tracks CPU time. Used to calculate total run-time
        of spaCy.
    ger_st_results (list[tuple]): List of tagging results for German with
        Stanza.
    ger_st_results_eval (Dict[str, Any]): Dictionary of the evaluation results
        for German with the spaCy large pipeline used for evaluation.
    ger_st_results_multi_eval (Dict[str, Any]): Dictionary of the evaluation
        results for German with the spaCy multi-language pipeline used for 
        evaluation.
    eng_st_results (list[tuple]): List of tagging results for English with
        Stanza.
    eng_st_results_eval (Dict[str, Any]): Dictionary of the evaluation results
        for English with the spaCy large pipeline used for evaluation.
    eng_st_results_multi_eval (Dict[str, Any]): Dictionary of the evaluation
        results for English with the spaCy multi-language pipeline used for 
        evaluation.
    nld_st_results (list[tuple]): List of tagging results for Dutch with
        Stanza.
    nld_st_results_eval (Dict[str, Any]): Dictionary of the evaluation results
        for Dutch with the spaCy large pipeline used for evaluation.
    nld_st_results_multi_eval (Dict[str, Any]): Dictionary of the evaluation
        results for English with the spaCy multi-language pipeline used for 
        evaluation.
    end_time_all (float): Tracks CPU time. Used to calculate total run-time of
        Stanza and the module.
    
"""

import pandas as pd
import time

from corpora import ger_sent, eng_sent, nld_sent
from spacy_test import *
from stanza_test import *

def export_to_csv(result):
    """Exports annotation results to a .csv file.

    Args:
        result (list[tuple]): The result from named_entity_recognition_sp/
            named_entity_recognition_st.

    Returns:
        df (DataFrame): A DataFrame of the results from the functions mentioned
            above, separated into two columns: the sentence and the entity type
            plus position. Only for legibility of the results.

    """
    df = pd.DataFrame(result, columns=["sentence", " entity type + position"])
    df.to_csv(r"./results.csv", index=False, header=True, mode="a", encoding="utf-8-sig")
    return df

start_time_all = time.process_time()

print()
print("spaCy:")

print("German:")
start_time_ger = time.process_time()
print("Tagging German...")
ger_sp_results_nlp_de2 = named_entity_recognition_sp(ger_sent[:163111], nlp_de2)
#ger_sp_results_nlp_multi = named_entity_recognition_sp(ger_sent[:163111], nlp_multi)
print(ger_sp_results_nlp_de2)
#print(ger_sp_results_nlp_multi)

print("Evaluating German...")
ger_sp_results_nlp_de2_eval = evaluate_ner_sp(ger_sp_results_nlp_de2, nlp_de3)
#ger_sp_results_nlp_multi_eval = evaluate_ner_sp(ger_sp_results_nlp_multi, nlp_de3)
print(ger_sp_results_nlp_de2_eval)
#print(ger_sp_results_nlp_multi_eval)

#export_to_csv(ger_sp_results_nlp_de2)
#export_to_csv(ger_sp_results_nlp_multi)

end_time_ger = time.process_time()
print("Time: ", end_time_ger - start_time_ger)  

print()

print("English:")
start_time_eng = time.process_time()
print("Tagging English...")
#eng_sp_results_nlp_en2 = named_entity_recognition_sp(eng_sent[:163111], nlp_en2)
#eng_sp_results_nlp_multi = named_entity_recognition_sp(eng_sent[:163111], nlp_multi)
#print(eng_sp_results_nlp_en2)
#print(eng_sp_results_nlp_multi)

print("Evaluating English...")
#eng_sp_results_nlp_en2_eval = evaluate_ner_sp(eng_sp_results_nlp_en2, nlp_en3)
#eng_sp_results_nlp_multi_eval = evaluate_ner_sp(eng_sp_results_nlp_multi, nlp_en3)
#print(eng_sp_results_nlp_en2_eval)
#print(eng_sp_results_nlp_multi_eval)

#export_to_csv(eng_sp_results_nlp_en2)
#export_to_csv(eng_sp_results_nlp_multi)

end_time_eng = time.process_time()
print("Time: ", end_time_eng - start_time_eng)  

print()

print("Dutch:")
start_time_nld = time.process_time()
print("Tagging Dutch...")
#nld_sp_results_nlp_nl2 = named_entity_recognition_sp(nld_sent, nlp_nl2)
#nld_sp_results_nlp_multi = named_entity_recognition_sp(nld_sent, nlp_multi)
#print(nld_sp_results_nlp_nl2)
#print(nld_sp_results_nlp_multi)

print("Evaluating Dutch...")
#nld_sp_results_nlp_nl2_eval = evaluate_ner_sp(nld_sp_results_nlp_nl2, nlp_nl3)
#nld_sp_results_nlp_multi_eval = evaluate_ner_sp(nld_sp_results_nlp_multi, nlp_nl3)
#print(nld_sp_results_nlp_nl2_eval)
#print(nld_sp_results_nlp_multi_eval)

#export_to_csv(nld_sp_results_nlp_nl2)
#export_to_csv(nld_sp_results_nlp_multi)

end_time_nld = time.process_time()
print("Time: ", end_time_nld - start_time_nld)  

end_time_spacy = time.process_time()
print("Time: ", end_time_spacy - start_time_all)  

print("SpaCy done.")


print()


print("Stanza:")

print("German:")
start_time_ger = time.process_time()
print("Tagging German...")
#ger_st_results = named_entity_recognition_st(ger_sent[:163111], nlp_de)
#print(ger_st_results)

print("Evaluating German...")
#ger_st_results_eval = evaluate_ner_st(ger_st_results, nlp_de3)
#ger_st_results_multi_eval = evaluate_ner_st(ger_st_results, nlp_multi)
#print(ger_st_results_eval)
#print(ger_st_results_multi_eval)

#export_to_csv(ger_st_results)

end_time_ger = time.process_time()
print("Time: ", end_time_ger - start_time_ger)  

print()

print("English:")
start_time_eng = time.process_time()
print("Tagging English...")
#eng_st_results = named_entity_recognition_st(eng_sent[:163111], nlp_en)
#print(eng_st_results)

print("Evaluating English...")
#eng_st_results_eval = evaluate_ner_st(eng_st_results, nlp_en3)
#eng_st_results_multi_eval = evaluate_ner_st(eng_st_results, nlp_multi)
#print(eng_st_results_eval)
#print(eng_st_results_multi_eval)

#export_to_csv(eng_st_results)

end_time_eng = time.process_time()
print("Time: ", end_time_eng - start_time_eng)  

print()

print("Dutch:")
start_time_nld = time.process_time()
print("Tagging Dutch...")
#nld_st_results = named_entity_recognition_st(nld_sent, nlp_nl)
#print(nld_st_results)

print("Evaluating Dutch...")
#nld_st_results_eval = evaluate_ner_st(nld_st_results, nlp_nl3)
#nld_st_results_multi_eval = evaluate_ner_st(nld_st_results, nlp_multi)
#print(nld_st_results_eval)
#print(nld_st_results_multi_eval)

#export_to_csv(nld_st_results)

end_time_nld = time.process_time()
print("Time: ", end_time_nld - start_time_nld)  

print()

print("Stanza done.")

end_time_all = time.process_time()
print("Time: ", end_time_all - start_time_all)  
