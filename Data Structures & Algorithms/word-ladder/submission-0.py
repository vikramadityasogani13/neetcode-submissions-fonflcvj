class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern_map =  defaultdict(list)
        all_words = wordList + [beginWord]
        word_len = len(beginWord)

        for word in all_words:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, steps  = queue.popleft()

            if word == endWord:
                return steps
            
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]

                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

                pattern_map[pattern] = []
        return 0