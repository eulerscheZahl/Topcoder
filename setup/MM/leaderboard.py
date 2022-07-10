#!/usr/bin/python3
 
import os
best_scores = {}
file_scores = {}

for file in os.listdir('scores/'):
    if not file.endswith('.txt'): continue
    file_scores[file] = {}
    with open('scores/' + file) as f:
        lines = f.readlines()
    for line in lines:
        if not "Seed = " in line: continue
        l = line[line.index("Seed = "):]
        l = l.replace('= ', '').replace(', ', ' ').split(' ')
        seed = int(l[1])
        score = float(l[3])
        if not seed in best_scores: best_scores[seed] = score
        best_scores[seed] = max(best_scores[seed], score)
        #best_scores[seed] = min(best_scores[seed], score)
        file_scores[file][seed] = score

for f in sorted(file_scores):
    if len(file_scores[f]) == 0: continue
    score = 0
    for seed in file_scores[f]:
        score += file_scores[f][seed] / best_scores[seed]
        #score += best_scores[seed] / file_scores[f][seed]
    print(f, score, '...', score * len(best_scores) / len(file_scores[f]))

