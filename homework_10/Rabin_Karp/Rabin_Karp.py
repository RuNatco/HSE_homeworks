def rabin_karp(text: str, pattern: str) -> int:
    """
    Ищем индекс первого вхождения паттерна в строку, иначе возвращаем -1
    """
    
    if not text or not pattern or len(pattern) > len(text):
        return -1

    base = 257
    mod = 1_000_000_007

    pat_len = len(pattern)
    txt_len = len(text)

    pattern_hash = 0
    window_hash = 0
    highest_power = 1

    for _ in range(pat_len - 1):
        highest_power = (highest_power * base) % mod

    for idx in range(pat_len):
        pattern_hash = (pattern_hash * base + ord(pattern[idx])) % mod
        window_hash = (window_hash * base + ord(text[idx])) % mod

    for start in range(txt_len - pat_len + 1):
        if pattern_hash == window_hash and text[start:start + pat_len] == pattern:
            return start

        if start < txt_len - pat_len:
            leading = (ord(text[start]) * highest_power) % mod
            window_hash = (window_hash - leading) % mod
            window_hash = (window_hash * base + ord(text[start + pat_len])) % mod

    return -1