#!/usr/bin/python3

import os
minimize = False
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
        file_scores[file][seed] = score
        if score == -1: continue
        if not seed in best_scores: best_scores[seed] = score
        if minimize: best_scores[seed] = min(best_scores[seed], score)
        else: best_scores[seed] = max(best_scores[seed], score)

keys = sorted(list(best_scores.keys()))
print('   '.join(str(k)+':'+str(best_scores[k]) for k in keys))

for f in sorted(file_scores):
    if len(file_scores[f]) == 0: continue
    score = 0
    for seed in file_scores[f]:
        if file_scores[f][seed] == -1: continue
        if minimize: score += best_scores[seed] / file_scores[f][seed]
        else: score += file_scores[f][seed] / best_scores[seed]
    print(f, score, '...', score * len(best_scores) / len(file_scores[f]))

