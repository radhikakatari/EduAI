def assist_student(question):
    if 'difficult' in question:
        return "It seems you're finding this topic challenging. Would you like some additional resources or a different explanation?"
    elif 'exam' in question:
        return "Don't worry! Make sure to review the key concepts and practice previous questions."
    else:
        return "Let me help you with that. Please provide more details."

# Example usage
student_question = "I'm finding this topic difficult."
response = assist_student(student_question)
print("AI Assistant Response:", response)