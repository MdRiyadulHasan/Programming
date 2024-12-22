from typing import List 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict, deque
        if endWord not in wordList:
            return 0
        word_length = len(beginWord)
        pattern_map = defaultdict(list)
        wordSet = set(wordList)
        for word in wordSet:
            for i in range(word_length):
                pattern = word[:i]+"*"+word[i+1:]
                pattern_map[pattern].append(word)
        # print(pattern_map)
        queue = deque([(beginWord, 1)])
        visited = set(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(word_length):
                pattern = current_word[:i]+"*"+current_word[i+1:]
                for neighbor in pattern_map[pattern]:
                    if neighbor==endWord:
                        return level+1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level+1))
                pattern_map[pattern] = []
        return 0