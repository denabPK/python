quiz = {
    "What is the capital of India?": "Delhi",
    "Which language is used for AI?": "Python",
    "2 + 2 = ?": "4"
}

score = 0

for q, a in quiz.items():
    ans = input(q + " ")
    if ans.lower() == a.lower():
        score += 1

print("Your Score:", score, "/", len(quiz))
