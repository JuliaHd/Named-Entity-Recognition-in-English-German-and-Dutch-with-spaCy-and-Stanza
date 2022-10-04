"""Exports a list of sentences from a corpus file per language.

Opens the three corpus.tsv files (e.g. deu_sentences.tsv) used in this project
and strips them of their index numbering and language tags before appending
every sentence in the corpus to an empty list. Do not do anything but execute
this module.

Requires "csv".

Attributes:
    ger_sent (list): Final list of German sentences.
    eng_sent (list): Final list of English sentences.
    nld_sent (list): Final list of Dutch sentences.
    german (TextIOWrapper): The German .tsv file, unchanged.
    tsv__ger_file (_reader): An iterable reader object of the original German
        .tsv file.
    ger_removed (list[str]): List of German sentences without index numbers or
        language tags.
    english (TextIOWrapper): The English .tsv file, unchanged.
    tsv__eng_file (_reader): An iterable reader object of the original English
        .tsv file.
    eng_removed (list[str]): List of English sentences without index numbers
        or language tags.
    dutch (TextIOWrapper): The Dutch .tsv file, unchanged.
    tsv__nld_file (_reader): An iterable reader object of the original Dutch
        .tsv file.

"""

import csv

ger_sent = []
eng_sent = []
nld_sent = []

with open(r"./deu_sentences.tsv", encoding="utf-8") as german:  # Put in the file path. If you get a FileNotFoundError please put in the absolute path.
    tsv__ger_file = csv.reader(german, delimiter="\t")
    for line_ger in tsv__ger_file:
        ger_removed = line_ger[2:]  # Remove index number and language tag from list.
        ger_sent.extend(ger_removed)
    #print(len(ger_sent))

with open(r"./eng_sentences.tsv", encoding="utf-8") as english:
    tsv__eng_file = csv.reader(english, delimiter="\t")
    for line_eng in tsv__eng_file:
        eng_removed = line_eng[2:]  # Remove index number and language tag from list.
        eng_sent.extend(eng_removed)
    #print(len(eng_sent))

with open(r"./nld_sentences.tsv", encoding="utf-8") as dutch:
    tsv__nld_file = csv.reader(dutch, delimiter="\t")
    for line_nld in tsv__nld_file:
        nld_removed = line_nld[2:]  # Remove index number and language tag from list.
        nld_sent.extend(nld_removed)
    #print(len(nld_sent))

print("All corpus files successfully read.")
