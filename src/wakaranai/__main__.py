from . import romaji, quiz

from argparse import ArgumentParser

from colorama import Fore

ROMAJI = {
    "hiragana": romaji.HIRAGANA,
    "katakana": romaji.KATAKANA,
}

parser = ArgumentParser(
    prog="wakaranai",
    description="An educational tool for learning hiragana and katakana")
parser.add_argument('-v', '--version', action='version', version="0.0.1")
parser.add_argument(
    'kana', choices=ROMAJI.keys(),
    help="the kana to be covered by the quiz")


def question_fmt(question: str) -> str:
    return f'{question}? '


def color(c: str, s: str) -> str:
    return c + s + Fore.RESET


def red(s: str) -> str:
    return color(Fore.RED, s)


def green(s: str) -> str:
    return color(Fore.GREEN, s)


def correction_fmt(
        question: str, is_correct: bool, correct_answers: set[str],
        answer: str) -> str:
    if is_correct:
        return f'{question} --> ' + green(f'{answer} ✓')
    else:
        correct_answers_str = ' or '.join(correct_answers)
        addendum = f' (correct: {correct_answers_str})'
        if answer:
            return f'{question} --> ' + red(f'{answer} ✗') + addendum
        else:
            return f'{question} --> ' + red('(blank) ✗') + addendum


def main() -> None:
    args = parser.parse_args()
    answer_key = ROMAJI[args.kana]
    questions = quiz.shuffle_questions(answer_key)
    answers = quiz.ask_questions(questions, question_fmt)
    correction = quiz.check_answers(answer_key, answers)
    print()
    quiz.print_correction(
        answer_key,
        questions,
        answers,
        correction,
        correction_fmt)


if __name__ == '__main__':
    main()
