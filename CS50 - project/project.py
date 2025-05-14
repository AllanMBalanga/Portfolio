import requests
import html
import random
from tkinter import *
from tkinter import messagebox

main_frame = None
difficulty_var = None
type_var = None
question_count_var = None
questions = None
current_question = 0
score = 0


def setup_widgets():
    global main_frame, difficulty_var, type_var, question_count_var

    for widget in main_frame.winfo_children():                                                                      # Clear frame
        widget.destroy()

    Label(main_frame, text="Quiz Game \nUsing Tkinter & Open Trivia Database\n(OpenTDB) API", font=("Arial", 24, "bold"), bg="#B1DDC6").pack(pady=10)                         # Title

    Label(main_frame, text="Difficulty:", font=("Arial", 14), bg="#B1DDC6").pack(pady=5)                                  # difficulty

    difficulty_var = StringVar(value="easy")
    difficulty_frame = Frame(main_frame, bg="#B1DDC6")
    difficulty_frame.pack(pady=5)

    Radiobutton(difficulty_frame, text="Easy", variable=difficulty_var, value="easy", bg="#B1DDC6").pack(side=LEFT, padx=10)          # easy

    Radiobutton(difficulty_frame, text="Medium", variable=difficulty_var, value="medium", bg="#B1DDC6").pack(side=LEFT, padx=10)      # medium

    Radiobutton(difficulty_frame, text="Hard", variable=difficulty_var, value="hard", bg="#B1DDC6").pack(side=LEFT, padx=10)          # hard

    Label(main_frame, text="Quiz Type:", font=("Arial", 14), bg="#B1DDC6").pack(pady=5)                                   # quiz type

    type_var = StringVar(value="multiple")
    type_frame = Frame(main_frame, bg="#B1DDC6")
    type_frame.pack(pady=5)

    Radiobutton(type_frame, text="Multiple Choice", variable=type_var, value="multiple", bg="#B1DDC6").pack(side=LEFT, padx=10)        # multiple

    Radiobutton(type_frame, text="True/False", variable=type_var, value="boolean", bg="#B1DDC6").pack(side=LEFT, padx=10)              # boolean


    Label(main_frame, text="Number of Questions (Max 50):", font=("Arial", 14), bg="#B1DDC6").pack(pady=5)                       # questions

    question_count_var = StringVar(value="5")
    Entry(main_frame, textvariable=question_count_var, width=5, font=("Arial", 12)).pack(pady=5)                                 # no. of questions

    Button(main_frame, text="Start Quiz", command=start_quiz, font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=20)



def start_quiz():
    global questions, current_question, score
    try:
        difficulty = difficulty_var.get()
        quiz_type = type_var.get()
        question_count = int(question_count_var.get())

        if question_count <= 0:
            messagebox.showerror("Invalid Input", "Please enter a valid number of questions")
            return

        if question_count > 50:
            messagebox.showerror("Invalid Input", "Maximum number is 50")
            return

        questions = fetch_questions(difficulty, quiz_type, question_count)

        score = 0                                   # Reset score and question counter
        current_question = 0

        show_question()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number")
    except Exception as e:
        messagebox.showerror("Invalid Input", f"Could not start quiz: {str(e)}")


def fetch_questions(difficulty, quiz_type, count):
    params = {
        "amount": count,
        "difficulty": difficulty,
        "type": quiz_type
    }

    response = requests.get(url="https://opentdb.com/api.php", params=params)
    data = response.json()

    if quiz_type == "multiple":
        return multiple_choice(data["results"])
    else:
        return true_false(data["results"])


def multiple_choice(data):
    quiz = []
    for item in data:
        question = html.unescape(item["question"])
        answer = html.unescape(item["correct_answer"])
        incorrect = [html.unescape(ans) for ans in item["incorrect_answers"]]

        options = [answer] + incorrect
        random.shuffle(options)

        quiz.append({
            "question": question,
            "answer": answer,
            "options": options
        })

    return quiz


def true_false(data):
    quiz = []
    for item in data:
        question = html.unescape(item["question"])
        correct_answer = html.unescape(item["correct_answer"])

        quiz.append({
            "question": question,
            "answer": correct_answer,
            "options": ["True", "False"]
        })

    return quiz


def show_question():
    global main_frame, questions, current_question

    for widget in main_frame.winfo_children():
        widget.destroy()

    progress_text = f"Question {current_question + 1} of {len(questions)}"
    Label(main_frame, text=progress_text, font=("Arial", 12), bg="#B1DDC6").pack(pady=5)


    Label(main_frame, text=f"Score: {score}", font=("Arial", 12), bg="#B1DDC6").pack(pady=5)


    question = questions[current_question]["question"]
    question_label = Label(main_frame, text=question, wraplength=400, font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
    question_label.pack(fill=X, pady=10)

    options_frame = Frame(main_frame, bg="#B1DDC6")
    options_frame.pack(pady=10)

    for option in questions[current_question]["options"]:
        Button(options_frame, text=option, width=30, wraplength=300, command=lambda opt=option: check_answer(opt)).pack(pady=5)


def check_answer(selected_answer):
    global current_question, score

    correct_answer = questions[current_question]["answer"]

    if selected_answer == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "✅ Correct!")
    else:
        messagebox.showinfo("Wrong", f"🚨 The correct answer is: {correct_answer}")

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_result()


def show_result():
    messagebox.showinfo("Quiz Complete",
                        f"Your final score: {score}/{len(questions)}")

    setup_widgets()


def main():
    global main_frame

    window = Tk()
    window.title("Quiz Trivia")
    window.config(padx=20, pady=20, bg="#B1DDC6")

    main_frame = Frame(window, bg="#B1DDC6")
    main_frame.pack(fill=BOTH, expand=True)
    setup_widgets()

    window.mainloop()


if __name__ == "__main__":
    main()
