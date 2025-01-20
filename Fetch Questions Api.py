import json

# File containing the filtered questions
INPUT_FILE = "filtered_questions_data.json"

def load_questions(file_path):
    """Load questions from the JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []

def find_answer_by_question_id(questions, question_id):
    """Find the answer text for the given question_id."""
    for question in questions:
        if str(question.get("question_id")) == str(question_id):
            answers = question.get("answers", [])
            if answers:
                return answers[0].get("answer_text")
    return None

def main():
    """Main function for interactive question lookup."""
    questions = load_questions(INPUT_FILE)

    if not questions:
        print("No questions available.")
        return

    while True:
        user_input = input("Enter question ID (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Exiting...")
            break

        if not user_input.isdigit():
            print("Invalid input. Please enter a numeric question ID.")
            continue

        question_id = int(user_input)
        answer = find_answer_by_question_id(questions, question_id)

        if answer:
            print(f"Answer for question ID {question_id}: {answer}")
        else:
            print(f"No correct answer found for question ID {question_id}.")

if __name__ == "__main__":
    main()
