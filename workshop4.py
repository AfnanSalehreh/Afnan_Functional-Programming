import math
from functools import reduce


# ---------- 1. summation (เวอร์ชันแก้ไขแล้ว มี step และ fn เป็น default argument) ----------
def summation(lower, upper, step=1, fn=lambda x: x):
    """รวมค่า fn(i) ของทุกตัวเลขในช่วง lower ถึง upper โดยเดินทีละ step"""
    total = 0
    i = lower
    while i <= upper:
        total += fn(i)
        i += step
    return total


# ---------- 2. displayRange (recursive) ----------
def displayRange(lower, upper):
    """แสดงตัวเลขตั้งแต่ lower ถึง upper โดยใช้ recursion"""
    if lower > upper:  # base case
        return
    print(lower, end=" ")
    displayRange(lower + 1, upper)  # recursive case


# ---------- 3. Mapping: ค่าสัมบูรณ์ของตัวเลขใน numbers ----------
def abs_values(numbers):
    return list(map(abs, numbers))


# ---------- 4. Filtering: เลือกเฉพาะจำนวนบวก (ใช้ lambda) ----------
def positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))


# ---------- 5. Reducing: รวมลิสต์ของสตริงเป็นสตริงเดียว ----------
def join_words(words):
    return reduce(lambda acc, w: acc + w, words, "")


if __name__ == "__main__":
    numbers = [-5, 3, -2, 0, 8, -1, 7]
    words = ["Functional", "Programming", "is", "fun"]

    print("--- summation ---")
    print("summation(1, 10)             =", summation(1, 10))
    print("summation(1, 100, 2, sqrt)   =", summation(1, 100, 2, math.sqrt))

    print("\n--- displayRange (recursive) ---")
    displayRange(1, 10)
    print()

    print("\n--- mapping (absolute values) ---")
    print(abs_values(numbers))

    print("\n--- filtering (positive numbers, lambda) ---")
    print(positive_numbers(numbers))

    print("\n--- reducing (join strings) ---")
    print(join_words(words))