# Quiz Game using Tkinter & OpenTDB API
## Brief Description:
The project is a quiz game built with Python using a graphical user interface (GUI) by utilizing the Tkinter library. It fetches data such as questions, answers, and, incorrect answers from Open Trivia Database (OpenTDB) API. The questions are customized based on the preferences of the user, including the level of difficulty (easy, medium, hard), quiz type (multiple choice or true/false), and the number of questions (maximum of 50) by using HTTP get request.

### Functionalities:
The program is a GUI-based quiz game that starts by asking the user for their quiz preferences (difficulty, type, and number of questions). These preferences are collected via tkinter GUI inputs and validated—especially the number of questions, which must be numeric and no more than 50. If invalid, an error message is shown using messagebox.

The inputs are used to construct a params dictionary, which is passed to the Open Trivia DB API to fetch quiz data. Based on the selected quiz type, either the multiple_choice or true_false function is called. Both functions process the API data (converting HTML entities, organizing it into a dictionary of questions, answers, and options) and return a quiz list.

The show_question function displays the current question, options, quiz progress, and score using tkinter. When the user selects an answer, the check_answer function checks it against the correct one, updates the score, and provides immediate feedback via a messagebox.

After each answer, the next question is shown until the quiz ends. Once all questions are answered, show_result displays the final score and resets the game via setup_widgets for a new round.

The main function initializes the GUI window, launches the setup screen, and starts the main event loop with window.mainloop().

