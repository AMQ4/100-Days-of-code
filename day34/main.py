from Quizzler import Quizzler
import requests

# Parameters for fetching quiz questions
params = {"amount": 10, "type": "boolean", "category": 18, "difficulty": "medium"}

# Fetch quiz data from the API
response = requests.get("https://opentdb.com/api.php", params=params)
questions = response.json()["results"]

# Create a Quizzler instance with the fetched questions
quizzler = Quizzler(questions)

# Start the main event loop to run the quiz
quizzler.main_loop()
