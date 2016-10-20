#!/usr/bin/env python

import random


def make_trigrams(word_list):
    '''Return a dictionary of trigrams.
    word_list: a list of single words, in order, from a text'''
    trigrams = {}
    for x in range(len(word_list[:-2])):
        bigram = " ".join(word_list[x:x+2])
        if bigram in trigrams:
            trigrams[bigram].append(word_list[x+2])
        else:
            trigrams[bigram] = [word_list[x+2]]
    return trigrams


def read_file(file_name):
    '''Read an input file.
    Return a list of all words in the file.
    file_name: string of file name, including file path if not in current directory'''
    with open(file_name, "r") as input_file:
        skip_front_matter(input_file)
        all_words = []
        for line in input_file:
            # skip end of book
            if line.startswith("End of the Project Gutenberg EBook"):
                break
            else:
                all_words += line.rstrip().split()
    return all_words


def skip_front_matter(f):
    '''Skip over the front matter in the book
    f: an open file object'''
    end_front_matter = " XII. The Adventure of the Copper Beeches"
    for line in f:
        if line.startswith(end_front_matter):
            break


def write_trigram_text(trigram_dict, length):
    '''Return a text produced from trigrams.
    trigram_dict: a dictionary of trigrams,
                key is a bigram, value is a list of the third trigram element
    length: length of the output text'''
    output_words = []
    first_bigram = random.choice(list(trigram_dict.keys()))
    output_words += first_bigram.split()
    for n in range(2, length - 2):
        last_bigram = " ".join(output_words[n-2:n])
        if last_bigram in trigram_dict:
            next_word = random.choice(trigram_dict[last_bigram])
            output_words.append(next_word)
        else:
            write_trigram_text(trigram_dict, n)
    return " ".join(output_words)

if __name__ == "__main__":
    all_words = read_file("holmes.txt")
    trigrams = make_trigrams(all_words)
    final_text = write_trigram_text(trigrams, 300)
    print(final_text)
