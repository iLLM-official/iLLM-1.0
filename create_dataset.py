import random

sentences = [
    "Hi, how are you?",
    "Today is a great day for experimenting with AI.",
    "Let's build our own model!",
    "Python is a great language for machine learning.",
    "AI is advancing very quickly."
]

with open("iLLM-1.0_dataset.txt", "w", encoding="utf-8") as f:
    for _ in range(10000):
        f.write(random.choice(sentences) + "\n")

print("Dataset created: iLLM-1.0_dataset.txt")