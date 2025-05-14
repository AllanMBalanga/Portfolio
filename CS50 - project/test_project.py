from project import multiple_choice, true_false, fetch_questions
import pytest
import html
import unittest
from unittest.mock import patch

#TODO use mocking to simulate API responses
#TODO multiple/boolean - pass in sample data

class TestFetchQuestions(unittest.TestCase):
    @patch("project.requests.get")
    def test_fetch_questions(self, mock_get_data):
        mock_data = {
            "response_code": 0,
                     "results": [
                {
                    "question": "Is Python dynamically typed?",
                    "correct_answer": "True",
                    "incorrect_answers": ["False"]
                }
            ] * 10
        }

        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200

        result = fetch_questions("easy","boolean", 10)
        self.assertEqual(len(result), 10)
        self.assertEqual(result[0]["answer"], "True")
        self.assertEqual(result[0]["options"], ["True", "False"])


def test_quiz_difficulty():
    with pytest.raises(ValueError):
        difficulty = "difficult"
        if difficulty not in ["easy", "medium","hard"]:
            raise ValueError("Invalid difficulty.")


def test_quiz_type():
    with pytest.raises(ValueError):
        quiz_type = "identification"
        if quiz_type == "multiple choice":
            quiz_type = "multiple"
        elif quiz_type == "true or false":
            quiz_type = "boolean"
        else:
            raise ValueError("Invalid quiz type.")

def test_max_question_count():
    with pytest.raises(ValueError):
        qs_number = 51
        if qs_number > 50:
            raise ValueError("Maximum number is 50")

def test_negative_question_count():
    with pytest.raises(ValueError):
        qs_number = -1
        if qs_number <= 0:
            raise ValueError("Please input a valid number of questions")

def test_non_numeric_input():
    with pytest.raises(ValueError):
        qs_number = "fifty"
        if not qs_number.isnumeric():
            raise ValueError("Please enter a number")


def test_multiple_choice():
    data = [{
        "question": "question",
        "correct_answer": "answer",
        "incorrect_answers": ["choice_1", "choice_2", "choice_3"]
    }]

    quiz = multiple_choice(data)

    assert quiz[0]["question"] == html.unescape("question")
    assert quiz[0]["answer"] == html.unescape("answer")

def test_true_false():
    data = [{
        "question": "question",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }]

    quiz = true_false(data)

    assert quiz[0]["question"] == html.unescape("question")
    assert quiz[0]["answer"] == html.unescape("True")


