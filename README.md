# Threat Detection Challenge

## Overview

Welcome to the Threat Detection Challenge! As a threat detection engineer, you are tasked with investigating a security incident and implementing detection logic to identify malicious activity in security logs.

**Your deliverable**: Detection Implementation, a Python-based detection function that processes security logs and identifies threats

This challenge tests your ability to:
- Parse and analyze security log data
- Implement threat detection rules and logic
- Handle various log formats and edge cases

## Prerequisites

- **Python 3.12** or higher
- **Poetry** for dependency management
- Basic understanding of security logs and threat detection concepts

## Setup Instructions

### 1. Install Python 3.12

Ensure you have Python 3.12 or higher installed on your system:

```bash
python --version
# Should show Python 3.12.x or higher
```

If you need to install Python 3.12:
- **macOS**: `brew install python@3.12`
- **Ubuntu/Debian**: `sudo apt update && sudo apt install python3.12`
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

### 2. Install Poetry

Poetry is used for dependency management and virtual environment handling:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

After installation, add Poetry to your PATH (follow the instructions shown after installation).

Verify Poetry installation:
```bash
poetry --version
```

### 3. Clone and Setup Project

```bash
# Navigate to the project directory
cd threat-detection-challenge

# Install dependencies using Poetry
poetry install

# Verify installation
poetry run python -m src.cli --help
```

### 4. Prepare Log Files

Place your log files in the `events/` directory or prepare the path to your log files for processing.

## Command-Line Usage

The threat detection tool processes security logs through your implemented detection functions.

### Basic Usage

```bash
# Process a single log file
poetry run python -m src.cli --in /path/to/logfile.txt --out alerts.json

# Process all files in a directory
poetry run python -m src.cli --in /path/to/logs/ --out results.json

# Use default output file (alerts.json)
poetry run python -m src.cli --in events/
```

### Command-Line Arguments

- `--in` (required): Input file or directory containing log files to process
- `--out` (optional): Output file path for detection results (default: `alerts.json`)

### Examples

```bash
# Process logs from events directory
poetry run python -m src.cli --in events/ --out threat_alerts.json

# Process a specific log file
poetry run python -m src.cli --in events/cloudtrail.log --out cloudtrail_alerts.json

# Process directory with default output
poetry run python -m src.cli --in /var/log/security/
```

## Challenge Objectives

### Detection Implementation

From the kill chain, consider what needs to be implemented to catch similar events in action. Implement threat detection logic in the provided Python framework:

1. **Parse Log Data**: Handle various log formats (JSON, structured text, etc.)
2. **Extract Relevant Fields**: Identify key data points for threat detection
3. **Implement Detection Rules**: Create logic to identify malicious activity
4. **Generate Alerts**: Output structured alerts for detected threats
5. **Handle Edge Cases**: Manage malformed logs and parsing errors


### Implementation Guide

#### Detection Function Structure

Your main implementation goes in `src/detector/rules.py` in the `ThreatDetector` class:

```python
class ThreatDetector:
    def __init__(self, output_sink):
        self.output_sink = output_sink
    
    def process_log_line(self, raw_line: str) -> None:
        # TODO: Implement your detection logic here
        
        # 1. Parse the raw log line
        # 2. Extract relevant fields
        # 3. Apply detection rules
        # 4. Generate alerts for threats
        
        # Example alert structure:
        alert = {
            "timestamp": "2024-01-01T12:00:00Z",
            "severity": "high",
            "threat_type": "suspicious_login",
            "evidence": "Multiple failed login attempts",
            "confidence": 0.85,
            "original_log": raw_line
        }
        
        # Write alert to output
        self.output_sink.write_alert(alert)
```

#### Alert Output Format

Your detection functions should generate alerts in this standardized format:

```json
{
  "timestamp": "2024-01-01T12:00:00Z",
  "severity": "high|medium|low|critical",
  "threat_type": "descriptive_threat_name",
  "source_log": "reference_to_original_log",
  "evidence": "description_of_suspicious_activity",
  "confidence": 0.85,
  "metadata": {},
  "enriched_fields": {},
  "original_log": "raw_log_line_for_reference"
}
```

#### Testing Your Implementation

1. **Run with Sample Data**: Test your detection functions with known log samples
2. **Validate Output Format**: Ensure alerts follow the expected JSON structure
3. **Check Edge Cases**: Test with malformed or incomplete log entries
4. **Performance Testing**: Verify your implementation handles large log files efficiently

```bash
# Test with sample logs
poetry run python -m src.cli --in test_logs/ --out test_results.json

# Validate output format
cat test_results.json | python -m json.tool
```

### Optional: Kill Chain Analysis (Forensic Investigation)

**This deliverable is not mandatory, but completing it will distinguish you as a top candidate.**

While the detection implementation is required, candidates who deliver a comprehensive kill chain analysis will demonstrate advanced threat hunting and analytical capabilities that set them apart. This is your opportunity to showcase expertise that goes beyond the baseline requirements.

Your task is to analyze the events and provide deeper insight into the attack by mapping observed activities to the MITRE ATT&CK framework. Identify the specific tactics and techniques employed by the attacker at each stage, extract key Indicators of Compromise (IOCs) such as IP addresses, user agents, API calls, resource identifiers, and timestamps, and explain how these events correlate to demonstrate the progression of the attack. This analysis should help security teams understand the attacker's objectives, methods, and the critical detection points within the kill chain.

## Deliverables and Submission

We will review the details during the interview.

### 1. Detection Implementation
- **Primary File**: `src/detector/rules.py` with your complete detection logic
- **Documentation**: Code comments explaining your detection approach
- **Sample Output**: `sample_alerts.json` with example alerts from your implementation

### 2. Kill chain analysis
If you go above and beyond, provide a document with the analysis in the format of your choice.

**Suggested File Structure:**
```
threat-detection-challenge/
├── src/detector/rules.py          # Your detection implementation
├── kill_chain_analysis.<whatever>        # Your forensic analysis
├── sample_alerts.json            # Example output from your detector
```

Good luck with the challenge! Focus on demonstrating your analytical skills in the forensic investigation and your technical abilities in the detection implementation.
