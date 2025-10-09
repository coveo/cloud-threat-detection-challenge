# Cloud Threat Detection Challenge — AWS (Poetry Edition)

**Context:** As a threat detection engineer, you are tasked with investigating a security incident in your organization's AWS environment. A malicious actor has compromised the production account, and you must conduct digital forensics to understand the scope and impact of the breach.

**Objective:** Your deliverables include:

1. **Kill Chain Analysis**: A comprehensive document detailing the attack progression with supporting evidence.
2. **Detection Tool**: A Python-based filtering tool intended for a SIEM integration that identifies relevant CloudTrail events indicative of malicious activity.

## Getting started

This project uses **Poetry** for dependency management.

### Extract the Challenge Files

First, extract the provided zip file to your desired location:

```bash
# Move the file to the right folder
cd <download-folder>
mv cloud-threat-detection-challenge-events.zip <repository-folder>/events
cd <repository-folder>
```

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
poetry run python src/cli.py
```
