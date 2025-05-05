import secrets
import string
import random

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_sets = []
    guaranteed = []

    if use_upper:
        char_sets.append(string.ascii_uppercase)
        guaranteed.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        char_sets.append(string.ascii_lowercase)
        guaranteed.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        char_sets.append(string.digits)
        guaranteed.append(secrets.choice(string.digits))
    if use_symbols:
        char_sets.append(string.punctuation)
        guaranteed.append(secrets.choice(string.punctuation))

    if not char_sets:
        raise ValueError("Нужно выбрать хотя бы один тип символов")

    if length < len(guaranteed):
        raise ValueError(f"Минимальная длина должна быть не менее {len(guaranteed)} символов")

    all_chars = ''.join(char_sets)
    remaining = [secrets.choice(all_chars) for _ in range(length - len(guaranteed))]

    # Собираем все символы и перемешиваем
    password_chars = guaranteed + remaining
    random.shuffle(password_chars)

    return ''.join(password_chars)
