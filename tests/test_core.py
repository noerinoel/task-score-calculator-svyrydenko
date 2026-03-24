import pytest

from app.core import analyze_task, calculate_priority_score, classify_priority


def test_calculate_priority_score_returns_expected_value():
    score = calculate_priority_score(urgency=5, impact=4, complexity=2)
    assert score == 21


def test_classify_priority_returns_high():
    assert classify_priority(16) == "high"


def test_analyze_task_returns_full_result():
    result = analyze_task(urgency=3, impact=3, complexity=2)

    assert result["score"] == 13
    assert result["priority"] == "medium"


def test_calculate_priority_score_raises_for_invalid_range():
    with pytest.raises(ValueError):
        calculate_priority_score(urgency=0, impact=3, complexity=2)