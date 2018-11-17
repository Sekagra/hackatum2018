#!/usr/bin/env python3
from random import randint
from random import shuffle
import re


tasks = [["1F603","1F604","1F606"],["1F618","1F61A","1F60D"],["1F61C","1F61D","1F60B"],["1F60F","1F612","1F60C"],["1F620","1F621","1F623"],["1F629","1F62A","1F628"],["1F631","1F632","1F635"],["1F638","1F639","1F63B"],["1F63C","1F63D","1F63F"],["1F640","1F638","1F63A"],["1F648","1F649","1F64A"],["1F64B","1F646","1F645"],["1F64B","1F64D","1F64E"],["270A","270B","270C"],["2733","2734","2744"],["1F683","1F684","1F685"],["1F689","1F687","1F683"],["1F693","1F695","1F697"],["1F699","1F691","1F69A"],["1F6A2","1F6A4","1F680"],["1F6BC","1F6BA","1F6B9"],["1F21A","1F22F","1F232"],["1F232","1F234","1F235"],["1F236","1F237","1F238"],["1F251","1F251","1F21A"],["2194","2195","2196"],["2648","264C","2650"],["3297","3299","2B55"],["1F304","1F305","1F307"],["1F313","1F314","1F311"],["1F319","1F31B","1F314"],["1F337","1F339","1F33A"],["1F33C","1F33B","1F338"],["1F33E","1F33F","1F33C"],["1F342","1F343","1F341"],["1F359","1F35A","1F35B"],["1F35C","1F35D","1F35B"],["1F366","1F367","1F368"],["1F37A","1F37B","1F379"],["1F389","1F388","1F38A"],["1F3B5","1F3B6","1F3B4"],["1F3E0","1F3E1","1F3E2"],["1F3E3","1F3E5","1F3E2"],["1F3E8","1F3EB","1F3EC"],["1F423","1F424","1F425"],["1F423","1F424","1F425"],["1F43B","1F43C","1F43A"],["1F479","1F47A","1F620"]]


def generate_random_sequence(length):
    global tasks
    seq = []
    while len(seq) < length:
        task = tasks[randint(0, len(tasks)-1)]
        if task not in seq:
            seq.append(task)
    return seq


def output_as_tex_table(sequence):
    table =  "\\begin{table}[htpb]" + "\n"
    table += "  \centering" + "\n"
    table += "  \\begin{tabular}{p{60mm} | c}" + "\n"
    table += "      \\textbf{Task} & \\textbf{Solution} \\\\" + "\n"
    table += "      \\hline" + "\n"
    for t in sequence:
        solution = t[0]
        shuffle(t)
        table += "      {\\Huge \\emoji[ios]{" + str(t[0])  + "}} {\\Huge \\emoji[ios]{" + str(t[1]) + "}} {\\Huge \\emoji[ios]{" + str(t[2])  + "}} & {\\Huge \\emoji[ios]{" + str(solution) + "}} \\\\" + "\n"

    table += "   \end{tabular}" + "\n"
    table += "\end{table}" + "\n"
    print(table)
    return table

def find_missing():
    global tasks
    for ta in tasks:
        for t in ta:
            with open("/home/obo/Documents/hackatum2018/defusedoc/latex-emoji/listing.txt", "r") as f:
                data = f.read()
                findings = re.search(t, data)
                if findings is None:
                    print(t)

def output_as_tex_file():
    pass

#find_missing()
#exit()
randseq = generate_random_sequence(15)
output_as_tex_table(tasks[0:20])
output_as_tex_table(tasks[20:])