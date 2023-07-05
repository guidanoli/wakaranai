"""This module defines quizzes.
A quiz consists of questions that may contain several correct answers.
You may give only one answer to each question of a quiz.
"""

import random
from typing import NewType
from collections.abc import Callable

Question = NewType('Question', str)
Questions = NewType('Questions', list[Question])
QuestionFormatter = NewType('QuestionFormatter', Callable[[Question], str])

Answer = NewType('Answer', str)

AnswerKey = NewType('AnswerKey', dict[Question, set[Answer]])
Answers = NewType('Answers', dict[Question, Answer])

Correction = NewType('Correction', dict[Question, bool])
CorrectionFormatter = NewType('CorrectionFormatter', Callable[[
                              Question, bool, set[Answer], Answer], str])


def shuffle_questions(answer_key: AnswerKey) -> Questions:
    questions = [q for q in answer_key]
    random.shuffle(questions)
    return questions


def ask_questions(questions: Questions, fmt: QuestionFormatter) -> Answers:
    answers = {}
    for q in questions:
        answers[q] = input(fmt(q))
    return answers


def check_answers(answer_key: AnswerKey, answers: Answers) -> Correction:
    correction = {}
    for q in answer_key:
        correction[q] = (answers[q] in answer_key[q])
    return correction


def print_correction(
        answer_key: AnswerKey, questions: Questions, answers: Answers,
        correction: Correction, fmt: CorrectionFormatter) -> None:
    for q in questions:
        print(fmt(q, correction[q], answer_key[q], answers[q]))
