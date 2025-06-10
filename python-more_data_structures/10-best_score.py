#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    current_hs = list(a_dictionary.values())[0]
    score_key = None
    for key in a_dictionary:
        if current_hs < a_dictionary[key]:
            score_key = key
        current_hs = a_dictionary.get(key)
    return score_key
