import re

# Load the knowledge base file
with open("project_knowledge.txt", "r") as f:
    KNOWLEDGE = f.read().lower()

def find_answer(question):
    question = question.lower()
    keywords = re.findall(r'\w+', question)

    best_sentence = ""
    best_score = 0

    for sentence in KNOWLEDGE.split("."):
        s = sentence.strip()
        if not s:
            continue

        score = sum(1 for w in keywords if w in s)

        if score > best_score:
            best_score = score
            best_sentence = s

    if best_sentence:
        return best_sentence + "."

    return ("I don't have information about that yet. "
            "Try asking about our materials, dimensions, gyroscope mechanism, "
            "suspension, or how we meet the project constraints.")

def chatbot_loop():
    print("Eco Velocity Chatbot Ready! Ask anything about our project.")
    while True:
        q = input("\nProfessor: ")
        if q.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", find_answer(q))

if __name__ == "__main__":
    chatbot_loop()

