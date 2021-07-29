def calculate_score(form_data):
    career_scores = {
        "creative_design": 0,
        "fintech_business": 0,
        "advanced_technology": 0,
        "cybersecurity_it": 0,
        "tech_related": 0,
    }
   


    for question in form_data:
        career = form_data[question]
        career_scores[career] += 1

    return career_scores

def score_category(scores):
    max_score = 0
    max_career = ''
    
    for score in scores:
        if scores[score] > max_score:
            max_score = scores[score]
            max_career = score

    return max_career + ".html" 
