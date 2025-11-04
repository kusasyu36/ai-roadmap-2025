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

# Project W1: Text Utilities on Real Data

- **目的**: Week1の関数（`is_palindrome`, `ngram`, `word_count_en`, `grade`, `bmi_class`）を実データに適用
- **データ**: Kaggle SMS Spam（uciml/sms-spam-collection-dataset, `spam.csv`）/ 自前テキスト
- **依存**: Python標準, `week01_python_basics/utils_day5.py`
- **ノート**: [`nb_project_w1.ipynb`](./nb_project_w1.ipynb)

## 実行例（スクリーンショット）
![run](./images/run_example.png)

## 簡易ベンチマーク（word_count_en の集計）
| 行数 | 時間(ms) |
|----:|---------:|
| 100 |   12.4   |
| 500 |   49.8   |
| 1,000 | 92.7   |
| 2,000 | 185.3  |

## 使い方（Colab）
```python
!wget -q -O utils_day5.py https://raw.githubusercontent.com/<YOUR_USER>/ai-roadmap-2025/main/week01_python_basics/utils_day5.py
import utils_day5 as U




