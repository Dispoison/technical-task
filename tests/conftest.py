from core.strings import (INPUT_FILE_NOT_FOUND, INPUT_FILE_IS_EMPTY, DIFFERENT_WORD_LENGTHS,
                          START_WORD_NOT_FOUND, END_WORD_NOT_FOUND, FILE_HAS_NO_EXTENSION)

parser_get_words_data = [
    ('Spin\nSpit\nSpat\nSpot\nSpan', ['Spin', 'Spit', 'Spat', 'Spot', 'Span']),
]

parser_get_words_error_data = [
    ('', INPUT_FILE_NOT_FOUND)
]

parser_validate_errors_data = [
    ([], 'Start', 'End', 'ResultFile.txt', INPUT_FILE_IS_EMPTY),
    (['Word', 'World'], 'Word', 'World', 'ResultFile.txt', DIFFERENT_WORD_LENGTHS),
    (['Word'], 'MissingWord', 'Word', 'ResultFile.txt', START_WORD_NOT_FOUND),
    (['Word'], 'Word', 'MissingWord', 'ResultFile.txt', END_WORD_NOT_FOUND),
]

parser_validate_warning_data = [
    (['Word'], 'Word', 'Word', 'ResultFile', FILE_HAS_NO_EXTENSION),
]

make_graph_from_list_data = [
    (['Spin', 'Spit', 'Spat', 'Spot', 'Span'],
     {'Spin': ['Spit', 'Span'], 'Spit': ['Spin', 'Spat', 'Spot'], 'Spat': ['Spit', 'Spot', 'Span'],
      'Spot': ['Spit', 'Spat'], 'Span': ['Spin', 'Spat']}),
    (['Spin', 'Soon'], {'Spin': [], 'Soon': []}),
]

find_path_data = [
    (['Word', 'Draw'], 'Word', 'Draw', []),
    (['Word'], 'Word', 'Word', ['Word']),
    (['Spin', 'Spit', 'Spat', 'Spot', 'Span'], 'Spin', 'Spot', ['Spin', 'Spit', 'Spot']),
    (['Park', 'Cark', 'Care', 'Cire', 'Lark', 'Lare', 'Lire', 'Fire'], 'Park', 'Fire',
     ['Park', 'Cark', 'Care', 'Cire', 'Fire']),
    (['firE', 'Park', 'Fark', 'Fare', 'Fire', 'park', 'parE', 'farE'], 'Park', 'firE',
     ['Park', 'park', 'parE', 'farE', 'firE']),
]

output_data = [
    (['Spin', 'Spit', 'Spat', 'Spot', 'Span'], 'Spin', 'Spot', ['Spin', 'Spit', 'Spot'],
     'Spin\nSpit\nSpot'),
    (['Park', 'Fire'], 'Park', 'Fire', [], 'No Way!')
]
