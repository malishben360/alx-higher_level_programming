#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tpl_a = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        tpl_a = (0, 0)
    else:
        tpl_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 1:
        tpl_b = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        tpl_b = (0, 0)
    else:
        tpl_b = (tuple_b[0], tuple_b[1])

    return (tpl_a[0] + tpl_b[0], tpl_a[1] + tpl_b[1])
