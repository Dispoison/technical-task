import pytest

from core.parser import Parser
from core.graph import Graph
from tests.conftest import (parser_get_words_data, parser_get_words_error_data,
                            parser_validate_errors_data, parser_validate_warning_data,
                            make_graph_from_list_data, find_path_data, output_data)


class TestParser:
    @staticmethod
    @pytest.mark.parametrize('input_text, words', parser_get_words_data)
    def test_get_words(tmp_path, input_text, words):
        folder = tmp_path / 'DictionaryFile.txt'
        folder.touch()
        folder.write_text(input_text)

        result = Parser.get_words(str(folder))
        assert result == words

    @staticmethod
    @pytest.mark.parametrize('input_file, expected_log', parser_get_words_error_data)
    def test_get_words_error(tmp_path, caplog, input_file, expected_log):
        with pytest.raises(FileNotFoundError):
            Parser.get_words(input_file)
        assert expected_log in caplog.text

    @staticmethod
    @pytest.mark.parametrize('words, start_word, end_word, result_file, expected_log',
                             parser_validate_errors_data)
    def test_validate_errors(caplog, words, start_word, end_word, result_file, expected_log):
        with pytest.raises(ValueError):
            Parser.validate(words, start_word, end_word, result_file)
        assert expected_log in caplog.text

    @staticmethod
    @pytest.mark.parametrize('words, start_word, end_word, result_file, expected_log',
                             parser_validate_warning_data)
    def test_validate_warning(caplog, words, start_word, end_word, result_file, expected_log):
        Parser.validate(words, start_word, end_word, result_file)
        assert expected_log in caplog.text


class TestGraph:
    @staticmethod
    @pytest.mark.parametrize('words, expected_graph', make_graph_from_list_data)
    def test_make_graph_from_list(words, expected_graph):
        graph = Graph._make_graph_from_list(words)
        assert graph == expected_graph

    @staticmethod
    @pytest.mark.parametrize('words, start_word, end_word, expected_path', find_path_data)
    def test_find_path(words, start_word, end_word, expected_path):
        graph = Graph(words)
        path = graph.find_path(start_word, end_word)
        assert path == expected_path

    @staticmethod
    @pytest.mark.parametrize('words, start_word, end_word, path, expected_result', output_data)
    def test_output(tmp_path, words, start_word, end_word, path, expected_result):
        folder = tmp_path / 'ResultFile.txt'
        folder.touch()

        Graph.output(words, start_word, end_word, str(folder), path)
        with open(folder) as file:
            assert file.read() == expected_result
