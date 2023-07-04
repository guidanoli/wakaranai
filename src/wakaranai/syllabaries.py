"""This module defines the syllabaries of the Japanese language.
Hiragana and katakana are defined as dictionaries whose keys are
kana and whose values are their rōmaji equivalent.
If a kana has more than one rōmaji equivalent, then the value
is a set of strings instead of a string."""

import random
from typing import NewType
from dataclasses import dataclass
from colorama import Fore

HIRAGANA = {
    'あ': 'a',
    'い': 'i',
    'う': 'u',
    'え': 'e',
    'お': 'o',
    'か': 'ka',
    'き': 'ki',
    'く': 'ku',
    'け': 'ke',
    'こ': 'ko',
    'さ': 'sa',
    'し': {'shi', 'si'},
    'す': 'su',
    'せ': 'se',
    'そ': 'so',
    'た': 'ta',
    'ち': {'chi', 'ti'},
    'つ': {'tsu', 'tu'},
    'て': 'te',
    'と': 'to',
    'な': 'na',
    'に': 'ni',
    'ぬ': 'nu',
    'ね': 'ne',
    'の': 'no',
    'は': 'ha',
    'ひ': 'hi',
    'ふ': {'fu', 'hu'},
    'へ': 'he',
    'ほ': 'ho',
    'ま': 'ma',
    'み': 'mi',
    'む': 'mu',
    'め': 'me',
    'も': 'mo',
    'や': 'ya',
    'ゆ': 'yu',
    'よ': 'yo',
    'ら': 'ra',
    'り': 'ri',
    'る': 'ru',
    'れ': 're',
    'ろ': 'ro',
    'わ': 'wa',
    'を': 'wo',
    'ん': 'n',
}

KATAKANA = {
    'ア': 'a',
    'イ': 'i',
    'ウ': 'u',
    'エ': 'e',
    'オ': 'o',
    'カ': 'ka',
    'キ': 'ki',
    'ク': 'ku',
    'ケ': 'ke',
    'コ': 'ko',
    'サ': 'sa',
    'シ': {'shi', 'si'},
    'ス': 'su',
    'セ': 'se',
    'ソ': 'so',
    'タ': 'ta',
    'チ': {'chi', 'ti'},
    'ツ': {'tsu', 'tu'},
    'テ': 'te',
    'ト': 'to',
    'ナ': 'na',
    'ニ': 'ni',
    'ヌ': 'nu',
    'ネ': 'ne',
    'ノ': 'no',
    'ハ': 'ha',
    'ヒ': 'hi',
    'フ': {'fu', 'hu'},
    'ヘ': 'he',
    'ホ': 'ho',
    'マ': 'ma',
    'ミ': 'mi',
    'ム': 'mu',
    'メ': 'me',
    'モ': 'mo',
    'ヤ': 'ya',
    'ユ': 'yu',
    'ヨ': 'yo',
    'ラ': 'ra',
    'リ': 'ri',
    'ル': 'ru',
    'レ': 're',
    'ロ': 'ro',
    'ワ': 'wa',
    'ヲ': 'wo',
    'ン': 'n',
}

Syllabary = NewType('Syllabary', dict[str, str])


@dataclass
class SyllabaryTest:
    syllabary: Syllabary
    syllables: list[str]


def generate_test(syllabary: Syllabary) -> SyllabaryTest:
    syllables = list(syllabary.keys())
    random.shuffle(syllables)
    return SyllabaryTest(syllabary, syllables)


@dataclass
class SyllabaryTestResult:
    test: SyllabaryTest
    answers: Syllabary


def apply_test(test: SyllabaryTest) -> SyllabaryTestResult:
    answers = {}
    for syllable in test.syllables:
        answers[syllable] = input('{}? '.format(syllable))
    return SyllabaryTestResult(test, answers)


def show_test_result(test_result: SyllabaryTestResult) -> None:
    syllabary = test_result.test.syllabary
    for syllable, answer in test_result.answers.items():
        correct_answer = syllabary[syllable]

        if isinstance(correct_answer, set):
            correct_answer_str = '/'.join(correct_answer)
            is_answer_correct = (answer in correct_answer)
        else:
            correct_answer_str = correct_answer
            is_answer_correct = (answer == correct_answer)

        if is_answer_correct:
            print(Fore.GREEN + f'{syllable} -- {correct_answer_str}')
        elif answer == "":
            print(Fore.RED + f'{syllable} -- {correct_answer_str}')
        else:
            print(
                Fore.YELLOW +
                f'{syllable} -- {correct_answer_str} (guessed "{answer}")')
