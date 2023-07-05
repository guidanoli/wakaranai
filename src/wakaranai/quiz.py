"""This module defines quizzes.
A quiz consists of questions that may contain several correct answers.
You may give only one answer to each question of a quiz.
"""

import random
from collections.abc import Callable

Question = str
Questions = list[Question]
QuestionFormatter = Callable[[Question], str]

Answer = str

AnswerKey = dict[Question, set[Answer]]
Answers = dict[Question, Answer]

Correction = dict[Question, bool]
CorrectionFormatter = Callable[[Question, bool, set[Answer], Answer], str]


def shuffle_questions(answer_key: AnswerKey) -> Questions:
    """Extract questions from an answer key and shuffle them"""
    questions = [q for q in answer_key]
    random.shuffle(questions)
    return questions


def ask_questions(questions: Questions, fmt: QuestionFormatter) -> Answers:
    """Get answers for questions from user input"""
    return {q: input(fmt(q)) for q in questions}


def check_answers(answer_key: AnswerKey, answers: Answers) -> Correction:
    """Check if answers are correct according to an answer key"""
    return {q: (answers[q] in answer_key[q]) for q in answer_key}


def print_correction(
        answer_key: AnswerKey, questions: Questions, answers: Answers,
        correction: Correction, fmt: CorrectionFormatter) -> None:
    """Print a correction of answers according to an answer key"""
    for q in questions:
        print(fmt(q, correction[q], answer_key[q], answers[q]))
