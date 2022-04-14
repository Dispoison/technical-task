import argparse

from core.logs import logger
from core.strings import (INPUT_FILE_NOT_FOUND, INPUT_FILE_IS_EMPTY, DIFFERENT_WORD_LENGTHS,
                          START_WORD_NOT_FOUND, END_WORD_NOT_FOUND, FILE_HAS_NO_EXTENSION)


class Parser:
    parser = argparse.ArgumentParser(description='Word path finder')
    parser.add_argument('dictionary_file', type=str,
                        help='The file name of a text file containing four letter words')
    parser.add_argument('start_word', type=str,
                        help='A four letter word (that you can assume is found '
                             'in the DictionaryFile file)')
    parser.add_argument('end_word', type=str,
                        help='A four letter word (that you can assume is found '
                             'in the DictionaryFile file)')
    parser.add_argument('result_file', type=str,
                        help='The file name of a text file that will contain the result')

    @classmethod
    def parse(cls):
        """
        Parses arguments, gets words from file and validates data
            :return: tuple of args and list of words
            :rtype: (argparse.Namespace, list[str])
        """
        args = cls.parser.parse_args()
        words = cls.get_words(args.dictionary_file)
        cls.validate(words, args.start_word, args.end_word, args.result_file)
        return args, words

    @staticmethod
    def get_words(dictionary_file):
        """
        Gets words from dictionary_file
            :param str dictionary_file: name of input file with words
            :return: list of words
            :rtype: list[str]
        """
        try:
            with open(dictionary_file) as file:
                words = [word.strip() for word in file.readlines()]
            return words
        except FileNotFoundError:
            logger.error(INPUT_FILE_NOT_FOUND)
            raise FileNotFoundError

    @staticmethod
    def validate(words, start_word, end_word, result_file):
        """
        Validates input data
            :param list[str] words: list of words
            :param str start_word: initial word of the path
            :param str end_word: end word of the path
            :param str result_file: name of output file
        """
        if not words:
            logger.error(INPUT_FILE_IS_EMPTY)
            raise ValueError

        if len(set(map(len, words))) != 1:
            logger.error(DIFFERENT_WORD_LENGTHS)
            raise ValueError

        if start_word not in words:
            logger.error(START_WORD_NOT_FOUND)
            raise ValueError

        if end_word not in words:
            logger.error(END_WORD_NOT_FOUND)
            raise ValueError

        if '.' not in result_file or not result_file.split('.')[-1]:
            logger.warning(FILE_HAS_NO_EXTENSION)
