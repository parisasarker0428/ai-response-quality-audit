# AI Response Quality Audit

A Python-based quality assurance project that evaluates AI-generated responses using a structured review rubric. The analysis compares model performance, identifies recurring failure patterns, and measures risks such as hallucinations and instruction-following errors.

## Project Objective

This project simulates an AI quality audit workflow similar to those used in AI evaluation, data quality, trust and safety, and model operations roles.

The audit evaluates responses across five dimensions:

- Accuracy
- Instruction following
- Completeness
- Tone
- Safety

Each response is also assigned a final rating of **Pass**, **Needs Review**, or **Fail**.

## Dataset

The dataset contains 24 synthetic AI-response evaluations across:

- Summarization
- Question answering
- Data extraction
- Classification
- Rewriting

Prompt categories include healthcare policy, insurance claims, medical billing, pharmacy, clinical notes, lab results, support tickets, and search quality.

> This project uses entirely synthetic data. It contains no real patient, customer, or proprietary information.

## Key Findings

- **24** AI responses audited
- **45.8%** overall pass rate
- **25.0%** hallucination rate
- **4.12 out of 5** average quality score
- Model A achieved the strongest performance with a **100% pass rate**
- Model C had the highest hallucination rate at **50%**
- Factual errors and instruction misses were the most frequent failure categories

## Project Structure

```text
ai-response-quality-audit/
├── data/
│   └── ai_response_audit.csv
├── src/
│   └── audit_analysis.py
├── outputs/
│   ├── cleaned_ai_response_audit.csv
│   ├── failure_type_summary.csv
│   ├── model_performance_summary.csv
│   ├── overall_quality_summary.csv
│   └── task_type_summary.csv
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

The `outputs` folder is automatically created when the analysis script runs.

## Tools and Skills Demonstrated

- Python
- pandas
- Data cleaning and validation
- Rubric-based AI evaluation
- Quality assurance metrics
- Hallucination and failure analysis
- Model performance comparison
- Reproducible reporting

## How to Run the Analysis

Clone the repository and install the required package:

```bash
git clone https://github.com/parisasarker0428/ai-response-quality-audit.git
cd ai-response-quality-audit
pip install -r requirements.txt
```

Run the analysis:

```bash
python src/audit_analysis.py
```

The script prints the audit summaries and saves the resulting CSV reports in the `outputs` folder.

## Future Improvements

- Add interactive charts and filtering
- Expand the evaluation dataset
- Introduce weighted scoring for high-risk errors
- Build a Streamlit quality-monitoring dashboard
- Add reviewer agreement and consistency metrics

## Author

**Parisa Sarker**

Background in AI response evaluation, search quality analysis, data validation, healthcare operations, and quality assurance.
