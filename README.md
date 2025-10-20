# Threat Detection Challenge

## Overview

Welcome to the Threat Detection Challenge! As a threat detection engineer, you are tasked with investigating a security incident and implementing detection logic to identify malicious activity in security logs.

**Your deliverables include:**

1. **Kill Chain Analysis**: A comprehensive forensic investigation document detailing the attack progression with supporting evidence
2. **Detection Implementation**: Python-based detection functions that process security logs and identify threats

This challenge tests your ability to:
- Conduct digital forensics and incident response
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

### Part 1: Kill Chain Analysis (Forensic Investigation)

**This is your first deliverable and should be completed before implementing detection rules.**

Analyze the provided security logs to understand what happened during the incident. You are expected to write a document detailing the security event with a timeline of the attack and important log entries as supporting evidence.

> 💡 **Recommended Analysis Tool**: Consider using a hosted OpenSearch, or locally deployed with Docker, for log analysis - [OpenSearch Docker installation guide](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/)

**Deliverable**: A kill chain analysis document that reconstructs the security event timeline with supporting evidence from the logs.

### Part 2: Detection Implementation

After understanding the kill chain, consider what needs to be implemented to catch similar events in action. Implement threat detection logic in the provided Python framework:

1. **Parse Log Data**: Handle various log formats (JSON, structured text, etc.)
2. **Extract Relevant Fields**: Identify key data points for threat detection
3. **Implement Detection Rules**: Create logic to identify malicious activity
4. **Generate Alerts**: Output structured alerts for detected threats
5. **Handle Edge Cases**: Manage malformed logs and parsing errors


## Implementation Guide

### Detection Function Structure

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

### Alert Output Format

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

### Testing Your Implementation

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

## Deliverables and Submission

Submit the following components to complete the challenge:

### 1. Kill Chain Analysis Document
- **Format**: PDF or Markdown document (3-5 pages with visualizations)
- **Content**: Comprehensive forensic investigation including:
  - Executive summary of the incident
  - Timeline of attack progression with supporting evidence
  - Technical details of each attack phase
  - Recommendations for prevention and detection

### 2. Detection Implementation
- **Primary File**: `src/detector/rules.py` with your complete detection logic
- **Documentation**: Code comments explaining your detection approach
- **Sample Output**: `sample_alerts.json` with example alerts from your implementation

### 3. Implementation Evidence
- **Testing Results**: Evidence that your implementation handles various log formats
- **Performance Notes**: Any optimizations or considerations for large datasets

**Required File Structure:**
```
threat-detection-challenge/
├── src/detector/rules.py          # Your detection implementation
├── kill_chain_analysis.pdf        # Your forensic analysis
├── sample_alerts.json            # Example output from your detector
└── README_IMPLEMENTATION.md      # Your implementation notes
```

Good luck with the challenge! Focus on demonstrating your analytical skills in the forensic investigation and your technical abilities in the detection implementation.
