def calculate_score(form_data):
    score = 0
    for question in form_data:
        question_score = int (form_data[question])
        score += question_score
    return score
        
def score_category(score):
    if score <= 130:
        return "creative_design.html"

    elif score <= 260:
        return "creative_design.html"

    elif score <= 390:
        return "creative_design.html"

    elif score <= 520:
        return "cyber.html"

    elif score <= 650:
        return "outside_careers.html"
    
    