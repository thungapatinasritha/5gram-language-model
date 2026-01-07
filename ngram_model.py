from collections import defaultdict
import random

def build_ngrams(text, n=5):
    words = text.lower().split()
    model = defaultdict(list)

    for i in range(len(words) - n):
        key = tuple(words[i:i + n - 1])
        model[key].append(words[i + n - 1])

    return model


def generate_text(model, seed, length=30):
    output = seed.lower().split()

    for _ in range(length):
        key = tuple(output[-4:])
        if key in model:
            output.append(random.choice(model[key]))
        else:
            break

    return " ".join(output)
