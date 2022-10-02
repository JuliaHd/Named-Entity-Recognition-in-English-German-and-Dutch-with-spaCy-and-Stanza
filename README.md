# <center>Named Entity Recognition in English, German, and Dutch with SpaCy and Stanza</center>

# About

"Named Entity Recognition in English, German, and Dutch with SpaCy and Stanza" is my Projektarbeit for my "Advanced NLP with Python" class at Heinrich Heine Universität Düsseldorf.

This project aims to compare the performance of NER with [spaCy](https://spacy.io/) (Honnibal et al., 2020) and [Stanza](https://stanfordnlp.github.io/stanza/) (Qi et al., 2020) in speed, accuracy (precision, recall, F1-score) and ease of implementation in translated text of English, German, and Dutch, using [Tatoeba](https://tatoeba.org/en/) (released under a CC-BY 2.0 FR license) as a corpus. The project uses spaCy's and Stanza's pretrained NER models for tagging and evaluation.

I uploaded a folder that contains my original results.

## Requirements
- Python 3.9.4
- Pandas 1.2.4
- spaCy 3.4.1 and its medium, large, and multi-language pipelines
- Stanza 1.4.1 and its pipelines

# Getting Started

## Install
- pip install the packages from requirements.txt.
    - the Stanza pipelines can be downloaded directly in `stanza_test.py`. If you have not used Stanza before please head there and comment in the download commands (and run the file).
- download the bz2 zip files which contain the corpus files. Unzip them into the same directory where you put the code.

Detailed installation instructions for spaCy can be found [here](https://spacy.io/usage) and for Stanza [here](https://stanfordnlp.github.io/stanza/installation_usage.html).

## Usage

If you installed everything correctly and you do not want to make any changes to the source code, you can simply run the `results.py` module. Unchanged, it will print the tagged sentences and their evaluation for German with spaCy on the medium module and the large module used for evaluation.

If you get an error message `FileNotFoundError: [Errno 2] No such file or directory:`, go to corpora.py and put in the absolute path of your directory where the corpus files go.

To change the tagging pipeline and evaluation used, you have to manually comment out the previous pipeline and its evaluation and comment in the pipeline and evaluation you want to use. All pipelines/ evaluation variables follow the same naming pattern and can be matched that way:

- Pipeline: xxx_yy_results_nlp_zz0
- Evaluation: xxx_yy_results_nlp_zz0_eval
- nlp_zz0 is irrelevant for Stanza since there is only one pipeline per language. Only use the language tag zz: xxx_yy_results_zz.
- xxx = ger, eng, nld
- sp = (spaCy); st = (Stanza)
- zz = language tag: de, en, nl, multi. 
- 0 = pipeline number. 2 (medium) or 3 (large). Does not exist for multi.

To use a different corpus, instantiate it in `corpora.py` then import it to `results.py`. It must be a list of sentences.

At the moment it is only possible to implement other spaCy and Stanza pipelines. This can be done in `spacy_test.py` and `stanza_test.py`.

In `spacy_test.py` spacy.load() the pipeline, like `spacy.load("de_core_news_sm")`. In `stanza_test.py` first download the language with `stanza.download('xx')`, then instantiate the pipeline with `stanza.Pipeline('xx', verbose=False, processors='tokenize, ner', use_gpu=True)`. Adjust the pipeline options as needed. Last, call the functions `named_entity_recognition_sp` (spaCy pipeline) or `named_entity_recognition_st` (Stanza pipeline) in `results.py` to tag your list of sentences with named entities. Then call `evaluate_ner_sp` (spaCy pipeline) or `evaluate_ner_st` (Stanza pipeline) to evaluate the results based on precision, recall, and F1-score. Keep in mind pipelines can only be evaluated with a spaCy pipeline as of now.

# References

Honnibal, M., Montani, I., Van Landeghem, S. & Boyd, A. (2020). spaCy: industrial-strength natural language    processing in Python. https://doi.org/10.5281/zenodo.1212303.

Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. D. (2020). Stanza: A python natural language processing toolkit for many human languages. In Association for Computational Linguistics (ACL) System Demonstrations. https://arxiv.org/abs/2003.07082

Tatoeba. (n.d.). Tatoeba: collection of sentences and translations. Retrieved September 29, 2022, from https://tatoeba.org/en/

