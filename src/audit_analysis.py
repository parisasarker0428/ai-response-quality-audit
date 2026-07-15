from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "ai_response_audit.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

SCORE_COLUMNS = [
    "accuracy_score",
    "instruction_following_score",
    "completeness_score",
    "tone_score",
    "safety_score",
]


def load_data():
    """Load the AI response audit dataset."""
    return pd.read_csv(DATA_PATH)


def add_quality_metrics(df):
    """Add calculated quality metrics to the dataset."""
    df = df.copy()

    df["average_score"] = df[SCORE_COLUMNS].mean(axis=1).round(2)

    df["quality_status"] = df["average_score"].apply(
        lambda score: "Meets Quality Bar"
        if score >= 4
        else "Needs QA Review"
    )

    return df


def summarize_overall_quality(df):
    """Create overall quality metrics."""
    total_responses = len(df)
    pass_rate = round(df["final_rating"].eq("Pass").mean() * 100, 1)
    hallucination_rate = round(
        df["hallucination_flag"].eq("Yes").mean() * 100,
        1,
    )
    average_quality_score = round(df["average_score"].mean(), 2)

    return pd.DataFrame(
        {
            "metric": [
                "Total Responses Audited",
                "Pass Rate (%)",
                "Hallucination Rate (%)",
                "Average Quality Score",
            ],
            "value": [
                total_responses,
                pass_rate,
                hallucination_rate,
                average_quality_score,
            ],
        }
    )


def summarize_by_model(df):
    """Compare model performance across quality and risk metrics."""
    return (
        df.groupby("model_name")
        .agg(
            responses_reviewed=("response_id", "count"),
            average_score=("average_score", "mean"),
            pass_rate=(
                "final_rating",
                lambda values: round(values.eq("Pass").mean() * 100, 1),
            ),
            hallucination_rate=(
                "hallucination_flag",
                lambda values: round(values.eq("Yes").mean() * 100, 1),
            ),
        )
        .round(2)
        .reset_index()
        .sort_values(by="average_score", ascending=False)
    )


def summarize_failure_types(df):
    """Identify the most common failure patterns."""
    failures = df[df["failure_type"] != "None"]

    return (
        failures.groupby("failure_type")
        .size()
        .reset_index(name="count")
        .sort_values(by="count", ascending=False)
    )


def summarize_task_types(df):
    """Compare performance across task types."""
    return (
        df.groupby("task_type")
        .agg(
            responses_reviewed=("response_id", "count"),
            average_score=("average_score", "mean"),
            pass_rate=(
                "final_rating",
                lambda values: round(values.eq("Pass").mean() * 100, 1),
            ),
        )
        .round(2)
        .reset_index()
        .sort_values(by="average_score", ascending=False)
    )


def save_outputs(df):
    """Save cleaned data and summary tables."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    df.to_csv(
        OUTPUT_DIR / "cleaned_ai_response_audit.csv",
        index=False,
    )

    summarize_overall_quality(df).to_csv(
        OUTPUT_DIR / "overall_quality_summary.csv",
        index=False,
    )

    summarize_by_model(df).to_csv(
        OUTPUT_DIR / "model_performance_summary.csv",
        index=False,
    )

    summarize_failure_types(df).to_csv(
        OUTPUT_DIR / "failure_type_summary.csv",
        index=False,
    )

    summarize_task_types(df).to_csv(
        OUTPUT_DIR / "task_type_summary.csv",
        index=False,
    )


def main():
    df = load_data()
    df = add_quality_metrics(df)
    save_outputs(df)

    print("\nAI Response Quality Audit")
    print("=" * 30)

    print("\nOverall Quality Summary:")
    print(summarize_overall_quality(df).to_string(index=False))

    print("\nModel Performance Summary:")
    print(summarize_by_model(df).to_string(index=False))

    print("\nMost Common Failure Types:")
    print(summarize_failure_types(df).to_string(index=False))

    print("\nTask Type Summary:")
    print(summarize_task_types(df).to_string(index=False))

    print("\nAnalysis complete. Files were saved to the outputs folder.")


if __name__ == "__main__":
    main()
