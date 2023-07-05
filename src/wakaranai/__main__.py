from . import kana, quiz

from argparse import ArgumentParser

from colorama import Fore

KANA_CHOICES = {
    "hiragana": kana.HIRAGANA,
    "katakana": kana.KATAKANA,
}

parser = ArgumentParser(
    prog="wakaranai",
    description="An educational tool for learning hiragana and katakana")
parser.add_argument('-v', '--version', action='version', version="0.0.1")
parser.add_argument(
    'kana', choices=KANA_CHOICES.keys(),
    help="the kana you'd like to practice")


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
    answer_key = KANA_CHOICES[args.kana]
    questions = quiz.shuffle_questions(answer_key)
    answers = quiz.ask_questions(questions, question_fmt)
    correction = quiz.check_answers(answer_key, answers)
    quiz.print_correction(
        answer_key,
        questions,
        answers,
        correction,
        correction_fmt)


if __name__ == '__main__':
    main()
