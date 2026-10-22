# 1. We define a structured dictionary for health categories and custom coach tips
# step 1: Define a structured dictionary for health categories and custom coach tips
BMI_KNOWLEDGE_BASE = {
    "underweight": {
        "label": "Underweight",
        "tip": "Consider eating more nutritious food and consulting a healthcare professional.",
        "coach_diet": "Focus on nutrient-dense meals, healthy fats (avocados, nuts), and lean proteins to gain weight safely.",
        "coach_exercise": "Try resistance training or light weightlifting to build healthy muscle mass rather than burning too many calories."
    },
    "normal": {
        "label": "Normal weight",
        "tip": "Maintain a balanced diet and regular exercise to keep your weight in check.",
        "coach_diet": "Keep up the great work! Focus on eating a colorful variety of whole foods, fiber, and staying hydrated.",
        "coach_exercise": "Aim for 150 minutes of moderate cardiovascular activity per week combined with strength training."
    },
    "overweight": {
        "label": "Overweight",
        "tip": "Consider creating a calorie deficit through diet and exercise and consulting a healthcare professional.",
        "coach_diet": "Focus on high-fiber foods and lean proteins to stay full while maintaining a gentle calorie deficit.",
        "coach_exercise": "Incorporate a mix of brisk walking, swimming, or cycling along with consistent strength training."
    }
}
# 2. We define a function to map BMI scores to our dictionary keys

def get_bmi_category(bmi):
    """Maps a numerical BMI score to our dictionary keys."""
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal"
    else:
        return "overweight"
# 3. We define a function to fetch custom answers based on user input and category

def get_coach_response(user_message, category):
    """Fetches custom answers instantly out of the dictionary."""
    msg = user_message.lower()
    data = BMI_KNOWLEDGE_BASE[category]
    
    if "diet" in msg or "eat" in msg or "food" in msg:
        return data["coach_diet"]
    elif "exercise" in msg or "workout" in msg or "train" in msg:
        return data["coach_exercise"]
    elif "bye" in msg or "exit" in msg:
        return "Goodbye! Keep tracking your health progress safely."
    else:
        return f"I see your status is {data['label']}. Ask me specific questions about your 'diet' or 'exercise' for tailored tips!"
# 4. We define a synchronous chat interface for user interaction

def chat_interface(category):
    """A standard synchronous loop for chatting with the user."""
    print("\n--- 💬 AI Health Coach Chat Started ---")
    print("Type your questions below (e.g., 'What should I eat?', 'Workout ideas?'). Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        
        # Check if user wants to exit
        if user_input.strip().lower() in ['exit', 'bye']:
            print("Coach: Goodbye! Stay healthy.")
            break
            
        # Get response instantly without async delays
        response = get_coach_response(user_input, category)
        print(f"Coach: {response}")
# 5. We define the main function to run the BMI calculator and launch the chat interface
def main():
    print("# My BMI Calculator & Knowledge Base Chatbot")
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: ")) 
    except ValueError:
        print("Please enter valid numerical numbers.")
        return

    if height <= 0:
        print("Height must be greater than zero.")
        return

    # Calculate BMI and pull the category name
    bmi = weight / (height ** 2)
    category = get_bmi_category(bmi)
    
    # Grab data from the dictionary using the category key
    current_health_data = BMI_KNOWLEDGE_BASE[category]
    
    print(f"\nYour calculated BMI is: {bmi:.1f}")
    print(f"Status: {current_health_data['label']}")
    print(f"Recommendation: {current_health_data['tip']}")

    # Launch the chat interface
    chat_interface(category)

if __name__ == "__main__":
    main()
