def looks_like_polish_surname(s):
    polish_suffixes = ('ski', 'cki')
    for x in polish_suffixes:
        if s.endswith(x):
            return True
    return False
