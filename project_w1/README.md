# Project W1：条件分岐＆関数の道具箱

## 目的
Week1で学んだ「関数・条件分岐・標準ライブラリ・assert」を使って、よく使うミニ関数を作る。土日に小さなプロジェクトとして公開できる形にする。

## 機能一覧（最小セット）
- `is_palindrome(s: str) -> bool`：回文判定（英数字のみ小文字化で判定）
- `ngram(s: str, n: int) -> list[str]`：文字n-gramのリスト
- `word_count_en(s: str) -> dict[str, int]`：英単語の出現回数
- `grade(score: float) -> str`：スコア→評価（A/B/C/D/F）
- `bmi_class(h: float, w: float) -> str`：BMI区分（身長[m], 体重[kg]）
- `gold_ratio() -> float` / `absolute(x: float) -> float`：モジュール練習用

## 入出力ルール
- 入力の型と単位をdocstringに明記。
- 例外が起きそうな場合はValueErrorなどをraise。

## テスト（ノート側）
- 各関数、最低3〜5件の `assert` を用意。
- 代表ケース + 境界値 + 例外系（可能なら）を含める。

## 使い方（Colab例）
```python
import utils_day5 as U
U.is_palindrome("Level")  # True
U.ngram("ABCDE", 3)       # ['ABC','BCD','CDE']
## 実行例（テキスト）
```python
import utils_day5 as U
U.is_palindrome("Able was I ere I saw Elba")  # True
U.ngram("TOKYO", 2)                           # ['TO','OK','KY','YO']
U.bmi_class(1.75, 95)                         # '肥満(2度)'

