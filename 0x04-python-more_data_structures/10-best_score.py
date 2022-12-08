#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_k = ""
    best_v = 0
    for k, v in a_dictionary.items():
        if v > best_v or len(a_dictionary) ==0:
            best_k = k
            best_v = v
    return best_k
