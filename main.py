from core.graph import Graph
from core.parser import Parser


def main(args, words):
    graph = Graph(words)
    path = graph.find_path(args.start_word, args.end_word)
    graph.output(words, args.start_word, args.end_word, args.result_file, path)


if __name__ == '__main__':
    args, words = Parser.parse()
    main(args, words)
