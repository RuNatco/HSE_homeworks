from typing import List


def _build_lps(pattern: str) -> List[int]:
    """
    Строим массив lps для шаблона. lps[i] — длина наибольшего собственного префикса,
    совпадающего с суффиксом подстроки pattern[:i+1].
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text: str, pattern: str) -> int:
    """
    Ищем индекс первого вхождения паттерна в строку. Если нет вхождения, возвращаем -1.
    """
    if not text or not pattern or len(pattern) > len(text):
        return -1

    lps = _build_lps(pattern)

    i = 0
    j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


