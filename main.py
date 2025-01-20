import requests
import json

# Correct API base URL
BASE_URL = "https://api.fs-quiz.eu/2/question/"

# Output file
OUTPUT_FILE = "filtered_questions_data.json"

# Function to fetch data for a specific question ID
def fetch_question(question_id):
    url = f"{BASE_URL}{question_id}"
    try:
        response = requests.get(url, headers={"Accept": "application/json"})
        if response.status_code == 404:
            print(f"Question ID {question_id} not found (404).")
            return None
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching question {question_id}: {e}")
        return None

# Function to filter answers where is_correct is True
def filter_correct_answers(question_data):
    if not question_data:
        return None
    question_data["answers"] = [answer for answer in question_data.get("answers", []) if answer.get("is_correct")]
    return question_data

# Main function to fetch and filter all questions
def fetch_and_filter_questions(start_id, end_id):
    filtered_questions = []

    for question_id in range(start_id, end_id + 1):
        print(f"Fetching question ID: {question_id}")
        data = fetch_question(question_id)
        if data:
            filtered_data = filter_correct_answers(data)
            if filtered_data:
                filtered_questions.append(filtered_data)

    return filtered_questions

# Fetch and filter questions from 1 to 1000
if __name__ == "__main__":
    questions = fetch_and_filter_questions(1, 1000)

    # Save to JSON file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

    print(f"Filtered data saved to {OUTPUT_FILE}")
