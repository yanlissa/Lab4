import string

def check_password_strength(password: str) -> tuple[str, int]:
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Слабый"
    elif score <= 4:
        return "Средний"
    else:
        return "Сильный"