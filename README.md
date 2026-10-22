# BMI Calculator & AI Health Coach Chatbot

A beginner-friendly Python console application that calculates a user's Body Mass Index (BMI) and launches a context-aware AI Health Coach Chatbot based on your specific results. 

This project demonstrates the power of clean code layout using Python dictionaries  as structured knowledge bases instead of relying on heavily nested `if-elif-else` loops.

---

# Key Features

* Precise BMI Calculation: Takes real-time user inputs for height (meters) and weight (kg) to compute your exact body metrics.
* Dictionary-Driven Knowledge Base:Uses structured Python dictionaries to cleanly manage categories, summaries, and personalized training tips.
* Context-Aware Chatbot:An interactive, conversational terminal companion that alters its health, diet, and exercise advice dynamically depending on whether your calculated baseline score is underweight, normal weight, or overweight.
* Zero External Dependencies:Built entirely with standard vanilla Python, requiring absolutely no third-party package setups or advanced async loops.

---

## How It Works 

Instead of cluttering the chatbot interface with complex conditional loops, the script matches your calculated BMI score to specific internal dictionary maps:

1. Underweight (< 18.5):Focuses on nutrient-dense calorie surpluses and muscle-building resistance exercises.
2. Normal Weight (18.5 – 24.9):Focuses on weight maintenance, balanced health routines, and stamina.
3. Overweight (≥ 24.9): Focuses on safe caloric deficits, dietary substitutions, and cardio variations.

---

##  Requirements

*Python 3.51 installed on your operating system.

---

# How to Run the Project

1. Clone or download this project file onto your local computer.
2. Open your system Terminal (Mac/Linux) or Command Prompt (Windows).
3. Navigate into the specific directory where your script is saved:
   ```bash
   cd path/to/your/folder
   ```
4. Run the script file:
   ```bash
   python bmi_calculator.py
   ```

---

##  Sample Execution Flow

```text
# My BMI Calculator & Knowledge Base Chatbot
Enter your weight in kg: 72
Enter your height in meters: 1.75

Your calculated BMI is: 23.5
Status: Normal weight
Recommendation: Maintain a balanced diet and regular exercise to keep your weight in check.

--- 💬 AI Health Coach Chat Started ---
Type your questions below (e.g., 'What should I eat?', 'Workout ideas?'). Type 'exit' to quit.

You: What should I eat?
Coach: Keep up the great work! Focus on eating a colorful variety of whole foods, fiber, and staying hydrated.

You: exit
Coach: Goodbye! Stay healthy.
```

---
