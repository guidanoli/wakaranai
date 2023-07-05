わからない (wakaranai) literally means "I don't understand" in Japanese.
It is a phrase worth learning, specially if you plan to visit Japan anytime soon.
If you'd like to learn more than just a couple of key phrases,
it might be useful to learn hiragana and katakana as well.
This Python package, called `wakaranai`, helps non-Japanese speakers
learn these two syllabaries by generating and applying random tests.

## Usage

If you ever feel like practicing your Japanese, simply run the following command.
You must choose to practice either hiragana or katakana.

```sh
python -m wakaranai {hiragana,katakana}
```

You will be prompted with characters from the selected kana in random order,
and you must answer with their correct romanizations.
The accepted romanizations are: Hepburn, Nihon-shiki, and Kunrei-shiki.
Obsolete syllables such as ゐ and ヰ are ignored.

```
お? o
た? ta
わ? re
...
```

After all characters have been prompted, the results will be displayed.
Wrong answers are accompanied by the correct answer(s).

```
お --> o ✓
た --> ta ✓
わ --> re ✗ (correct: wa)
...
```
