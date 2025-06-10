#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    score_key, current_hs = list(a_dictionary.items())[0]
    for key in a_dictionary:
        if current_hs < a_dictionary[key]:
            current_hs = a_dictionary.get(key)
            score_key = key
    return score_key
