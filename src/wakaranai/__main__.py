from . import syllabaries

from argparse import ArgumentParser

SYLLABARIES = {
    "hiragana": syllabaries.HIRAGANA,
    "katakana": syllabaries.KATAKANA,
}

parser = ArgumentParser(
    prog="wakaranai",
    description="An educational tool for learning hiragana and katakana")
parser.add_argument('-v', '--version', action='version', version="0.0.1")
parser.add_argument(
    'syllabary', choices=SYLLABARIES.keys(),
    help="the syllabary you'd like to practice")


def main():
    args = parser.parse_args()
    syllabary = SYLLABARIES[args.syllabary]
    test = syllabaries.generate_test(syllabary)
    test_result = syllabaries.apply_test(test)
    syllabaries.show_test_result(test_result)


if __name__ == '__main__':
    main()
