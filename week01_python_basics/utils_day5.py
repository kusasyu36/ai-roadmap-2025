"""
utils_day5.py : Week1の道具箱（関数/if/モジュール/assert練習）
"""

from __future__ import annotations
import re
import math
from collections import Counter
from typing import List, Dict

__all__ = [
    "is_palindrome",
    "ngram",
    "word_count_en",
    "grade",
    "bmi_class",
    "gold_ratio",
    "absolute",
]

def is_palindrome(s: str) -> bool:
    """
    英数字のみを取り出して小文字化し、前後一致で回文判定。
    例: "Level" -> True, "Hello" -> False
    """
    if not isinstance(s, str):
        raise ValueError("s は str にしてください")
    t = re.sub(r"[^0-9A-Za-z]", "", s).lower()
    return t == t[::-1]

def ngram(s: str, n: int) -> List[str]:
    """
    文字列 s を連続 n 文字で切り出してリストで返す。
    例: ngram("ABCDE", 3) -> ["ABC","BCD","CDE"]
    """
    if not isinstance(s, str):
        raise ValueError("s は str にしてください")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n は正の整数にしてください")
    if n > len(s):
        return []
    return [s[i:i+n] for i in range(len(s) - n + 1)]

def word_count_en(s: str) -> Dict[str, int]:
    """
    英語のみ想定の簡易カウント。単語を小文字化して集計。
    簡易ルール: [A-Za-z]+ (' を含む単語も一応許可)
    """
    if not isinstance(s, str):
        raise ValueError("s は str にしてください")
    tokens = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", s.lower())
    return dict(Counter(tokens))

def grade(score: float) -> str:
    """
    0-100想定のスコア→評価。A>=90, B>=80, C>=70, D>=60, F<60
    """
    try:
        x = float(score)
    except Exception as e:
        raise ValueError("score は数値にしてください") from e
    if x < 0 or x > 100:
        raise ValueError("score は 0〜100 を想定します")
    if x >= 90: return "A"
    if x >= 80: return "B"
    if x >= 70: return "C"
    if x >= 60: return "D"
    return "F"

def bmi_class(h: float, w: float) -> str:
    """
    BMI区分（厚労省の一般的区分）:
      <18.5: 痩せ
      18.5–25: 普通体重
      25–30: 肥満(1度)
      30–35: 肥満(2度)
      35–40: 肥満(3度)
      >=40: 肥満(4度)
    入力: h=身長[m], w=体重[kg]
    """
    try:
        h = float(h); w = float(w)
    except Exception as e:
        raise ValueError("h, w は数値にしてください") from e
    if h <= 0 or w <= 0:
        raise ValueError("h, w は正の値にしてください")
    bmi = w / (h * h)
    if bmi < 18.5:
        return "痩せ(低体重)"
    if bmi < 25:
        return "普通体重"
    if bmi < 30:
        return "肥満(1度)"
    if bmi < 35:
        return "肥満(2度)"
    if bmi < 40:
        return "肥満(3度)"
    return "肥満(4度)"

def gold_ratio() -> float:
    """黄金比 φ = (1 + sqrt(5)) / 2"""
    return (1.0 + math.sqrt(5.0)) / 2.0

def absolute(x: float) -> float:
    """abs(x) の自前実装（練習用）"""
    try:
        x = float(x)
    except Exception as e:
        raise ValueError("x は数値にしてください") from e
    return x if x >= 0 else -x
