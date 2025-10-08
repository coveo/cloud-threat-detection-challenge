# Cloud Threat Detection Challenge — AWS (Poetry Edition)

**Objective:** Build a detection engine that ingests AWS telemetry and surfaces credible threats.

This edition includes:
- CloudTrail events
- VPC Flow Logs
- GuardDuty-like findings

## Getting Started

This project uses **Poetry** for dependency management.

### Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Install Dependencies
```bash
poetry install
```

### Run the Challenge
```bash
poetry run python src/cli.py --in data/logs --out alerts.json
```

### Grade Your Results
```bash
poetry run python grade.py --alerts alerts.json --truth data/truth.json
```

### Run Tests
```bash
poetry run pytest -q
```

---

Everything else (data, source code, grader) is identical to the venv version, 
but dependency management is handled via Poetry for cleaner reproducibility.
