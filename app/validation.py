def validate_task_data(urgency: int, impact: int, complexity: int) -> None:
    values = {
        "urgency": urgency,
        "impact": impact,
        "complexity": complexity,
    }

    for field_name, value in values.items():
        if not isinstance(value, int):
            raise TypeError(f"{field_name} must be an integer")

        if value < 1 or value > 5:
            raise ValueError(f"{field_name} must be between 1 and 5")
