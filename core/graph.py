from collections import deque
from itertools import permutations

from core.logs import logger
from core.strings import MISSING_PATH, ALGORITHM_STARTED


class Graph:
    def __init__(self, words):
        """
        Creates graph as dictionary with linked words
            :param list[str] words: list of string words
        """
        self.graph = self._make_graph_from_list(words)

    @staticmethod
    def _make_graph_from_list(words):
        """Returns dictionary with a list of words as values that have one distinct letter"""
        graph = {word: [] for word in words}

        for key_word, linked_word in permutations(words, 2):
            same_letter_number = sum(x == y for x, y in zip(key_word, linked_word))
            if same_letter_number == len(key_word) - 1:
                graph[key_word].append(linked_word)

        return graph

    def _bfs(self, start_word, end_word):
        """Breadth-first search until end_word with path"""
        paths = {key: [] for key in self.graph.keys()}
        paths[start_word] = [start_word]
        queue = deque([start_word])

        while queue:
            key_word = queue.popleft()
            for linked_word in self.graph[key_word]:
                if not paths[linked_word]:
                    queue.append(linked_word)
                    paths[linked_word] = [*paths[key_word], linked_word]
                    if linked_word == end_word:
                        return paths[end_word]
        return paths[end_word]

    @staticmethod
    def _make_result(words, start_word, end_word, path):
        """Logs result information to log file and returns the result"""
        if path:
            result = '\n'.join(path)
            logger.info("Success - Words: %s - Start word: '%s' - End word: '%s' - Path: %s",
                        words, start_word, end_word, path)
        else:
            result = MISSING_PATH
            logger.info("Failure - Words: %s - Start word: '%s' - End word: '%s'",
                        words, start_word, end_word)
        return result

    def find_path(self, start_word, end_word):
        """
        Finds the shortest path between two words
            :param str start_word: initial word of the path
            :param str end_word: end word of the path
            :return: shortest path
            :rtype: list[str]
        """
        logger.info(ALGORITHM_STARTED)
        return self._bfs(start_word, end_word)

    @classmethod
    def output(cls, words, start_word, end_word, result_file, path):
        """
        Writes result data to file
            :param list[str] words: list of words
            :param str start_word: initial word of the path
            :param str end_word: end word of the path
            :param str result_file: name of output file
            :param list[str] path: list of words
        """
        result = cls._make_result(words, start_word, end_word, path)
        with open(result_file, 'w') as file:
            file.write(result)
