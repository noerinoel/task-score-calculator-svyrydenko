from app.validation import validate_task_data


def calculate_priority_score(urgency: int, impact: int, complexity: int) -> int:
    validate_task_data(urgency, impact, complexity)
    return urgency * 3 + impact * 2 - complexity



def classify_priority(score: int) -> str:
    if score >= 16:
        return "high"
    if score >= 10:
        return "medium"
    return "low"



def analyze_task(urgency: int, impact: int, complexity: int) -> dict:
    score = calculate_priority_score(urgency, impact, complexity)
    priority = classify_priority(score)

    return {
        "score": score,
        "priority": priority,
    }
