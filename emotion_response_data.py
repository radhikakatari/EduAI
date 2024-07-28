def recommend_learning_materials(emotion, performance_data):
    if emotion in ['Sad', 'Angry', 'Fear']:
        # Suggest easy or engaging materials to boost morale
        materials = ['Introduction to Topic X', 'Fun Quiz on Topic Y']
    elif emotion == 'Happy':
        # Suggest challenging materials
        materials = ['Advanced Topic Z', 'In-depth Analysis on Topic Y']
    else:
        # Neutral or other emotions
        materials = ['Review materials', 'Practice problems']
    
    # Consider performance data to refine suggestions
    # e.g., if struggling with Topic X, suggest more resources on Topic X
    return materials

# Example usage
performance_data = {...}  # Student performance data
emotion = 'Happy'
recommended_materials = recommend_learning_materials(emotion, performance_data)
print("Recommended Materials:", recommended_materials)