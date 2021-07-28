def calculate_score(form_data):
    score = 0
    for question in form_data:
        question_score = int (form_data[question])
        score += question_score
    return score
        
def score_category(score):
    if score <= 200:
        return "creative_design.html"

    elif score <= 300:
        return "business_technology.html"

    elif score <= 400:
        return "advanced_technology.html"

    elif score <= 500:
        return "cybersecurity_it.html"

    elif score <= 600:
        return "tech_related.html"
    
    