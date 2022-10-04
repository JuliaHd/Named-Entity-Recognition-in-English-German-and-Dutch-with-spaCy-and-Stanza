# <center>Named Entity Recognition in English, German, and Dutch with SpaCy and Stanza</center>

# About

"Named Entity Recognition in English, German, and Dutch with SpaCy and Stanza" is my project work for my "Advanced NLP with Python" class at Heinrich-Heine-Universität Düsseldorf.

This project aims to compare the performance of Named Entity Recognition (NER) with [spaCy](https://spacy.io/) (Honnibal et al., 2020) and [Stanza](https://stanfordnlp.github.io/stanza/) (Qi et al., 2020) in speed, accuracy (precision, recall, F1-score) and ease of implementation in translated text of English, German, and Dutch, using [Tatoeba](https://tatoeba.org/en/) (released under a CC-BY 2.0 FR license) as a corpus. The project uses spaCy's and Stanza's pretrained NER models for tagging and evaluation.

I uploaded a "Results Table" PDF that contains my original results as well as csv files that contain all tagging results.

## Requirements
- Python 3.9.4
- see requirements.txt

# Getting Started

## Install
- pip install the packages in requirements.txt.
- the Stanza pipelines can be downloaded directly in `stanza_test.py`. If you have not used Stanza before please head there and comment in the download commands (and run the file).

Detailed installation instructions for spaCy can be found [here](https://spacy.io/usage) and for Stanza [here](https://stanfordnlp.github.io/stanza/installation_usage.html).

## Usage

If you installed everything correctly and you do not want to make any changes to the source code, you can simply run the `results.py` module. The module will print the tagged sentences and their evaluation for German with spaCy on the medium module (tagger) and the large module (evaluation).

If you get an error message `FileNotFoundError: [Errno 2] No such file or directory:`, go to `corpora.py` and put in the absolute path of the corpus files.

To change the tagging pipeline and evaluation used, you have to manually comment out the previous pipeline and its evaluation and comment in the pipeline and evaluation you want to use. All pipelines/ evaluation variables follow the same naming pattern and can be matched that way:

- Pipeline: spaCy: xxx_sp_results_nlp_zz0; Stanza: xxx_st_results
- Evaluation: spaCy: xxx_yy_results_nlp_zz0_eval; Stanza: xxx_st_results_eval/xxx_st_results_multi_eval
- xxx = ger, eng, nld
- sp = (spaCy); st = (Stanza)
- zz = language tag: de, en, nl, multi. 
- 0 = pipeline number. 2 (medium) or 3 (large). Does not exist for multi.

## Adding a new corpus

To use a different corpus, instantiate it in `corpora.py`, then import it to `results.py`. It must be a list of sentences.

## Adding a new pipeline

At the moment it is only possible to implement other spaCy and Stanza pipelines. This can be done in `spacy_test.py` and `stanza_test.py`.

### spaCy
1. Pip install the spaCy pipeline of choice.
2. In `spacy_test.py` spacy.load() the pipeline, like `spacy.load("de_core_news_sm")` (and assign it a variable).
3. Call the function `named_entity_recognition_sp` with your variable in `results.py` to tag your list of sentences with named entities.
4. Call `evaluate_ner_sp` with the results from the previous function and the desired evaluation pipeline to get the precision, recall, and F1-score. Keep in mind `named_entity_recognition_sp`'s results can only be evaluated with a spaCy pipeline as of now.

### Stanza
1. In `stanza_test.py` download the language with `stanza.download('xx')`, xx being the [language code](https://stanfordnlp.github.io/stanza/available_models.html).
2. Instantiate the pipeline with `stanza.Pipeline('xx', verbose=False, processors='tokenize, ner', use_gpu=True)` (and assign it a variable). Adjust the pipeline options as needed. The pipeline options can be found in Stanza's [documentation](https://stanfordnlp.github.io/stanza/pipeline.html).
3. Call the function `named_entity_recognition_st` with your variable in `results.py` to tag your list of sentences with named entities.
4. Call `evaluate_ner_st` with the results from the previous function and the desired evaluation pipeline to get the precision, recall, and F1-score. Keep in mind `named_entity_recognition_st`'s results can only be evaluated with a spaCy pipeline as of now.
5. (Optional) If you want to evaluate a Stanza pipeline with a new spaCy pipeline follow the spaCy instructions above but instantiate the pipeline in `stanza_test.py` instead of `spacy_test.py`.

# References

Honnibal, M., Montani, I., Van Landeghem, S. & Boyd, A. (2020). spaCy: industrial-strength natural language    processing in Python. https://doi.org/10.5281/zenodo.1212303.

Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. D. (2020). Stanza: A python natural language processing toolkit for many human languages. In Association for Computational Linguistics (ACL) System Demonstrations. https://arxiv.org/abs/2003.07082.

Tatoeba. (n.d.). Tatoeba: collection of sentences and translations. Retrieved September 29, 2022, from https://tatoeba.org/en/.
