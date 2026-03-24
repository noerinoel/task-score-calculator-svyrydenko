from app.core import analyze_task


def parse_int(value: str) -> int:
    return int(value.strip())


def run_cli() -> None:
    urgency = parse_int(input("Enter urgency (1-5): "))
    impact = parse_int(input("Enter impact (1-5): "))
    complexity = parse_int(input("Enter complexity (1-5): "))

    result = analyze_task(urgency, impact, complexity)

    print(f"Score: {result['score']}")
    print(f"Priority: {result['priority']}")


if __name__ == "__main__":
    run_cli()
