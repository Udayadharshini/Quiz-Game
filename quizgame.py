import random
from questions import questions  # import questions from questions.py

score = 0
points_per_question = 20

# Welcome message
print("🎉 WELCOME TO QUIZ 🎉")
print("Choose Category:\n1. GK\n2. Python\n3. AI")
choice = input("Enter choice (1-3): ")

if choice == "1":
    category = "GK"
elif choice == "2":
    category = "Python"
elif choice == "3":
    category = "AI"
else:
    print("Invalid choice")
    exit()

# Pick 5 random questions
selected = random.sample(questions[category], 5)

# Ask questions
for num, q in enumerate(selected, start=1):
    print(f"\nQ{num}: {q['question']}")
    for opt in q["options"]:
        print(opt)
    ans = input("Your Answer: ").lower()
    if ans == q["answer"]:
        score += points_per_question
        print(f"✅ Correct! Current Score: {score}/{num*points_per_question}")
    else:
        print(f"❌ Wrong! Current Score: {score}/{num*points_per_question}")

# Final Score
total_score = len(selected) * points_per_question
print("\n🎯 Quiz Finished!")
print(f"Your Final Score: {score}/{total_score}")

if (score / total_score) * 100 >= 60:
    print("✅ You Passed!")
else:
    print("❌ You Failed!")