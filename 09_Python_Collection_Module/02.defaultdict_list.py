from collections import defaultdict
data = [
    ('Alice', 90),
    ('Bob', 85),
    ('Alice', 92),
    ('Bob', 88),
    ('Charlie', 95)
]

# defaultdict with list as the default factory
scores_by_name = defaultdict(list)
for name, score in data:
    scores_by_name[name].append(score)
for name, scores in scores_by_name.items():
    print(f'{name}: {scores}')
# print(scores_by_name)