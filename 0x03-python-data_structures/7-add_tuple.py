#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    listTuple_a = list(tuple_a)
    listTuple_b = list(tuple_b)
    if len(listTuple_a) < 2:
        for i in range(len(listTuple_a), 2):
            listTuple_a[i].append(0)
    if len(listTuple_b) < 2:
        for i in range(len(listTuple_b), 2):
            listTuple_b.append(0)
    nList = [listTuple_a[0] + listTuple_b[0], listTuple_b[1] + listTuple_a[1]]
    ntuple = tuple(nList)
    return (ntuple)
