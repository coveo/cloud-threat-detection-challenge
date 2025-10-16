# Implementation Plan

- [x] 1. Update project configuration and dependencies

  - Update pyproject.toml to require Python 3.12 and include necessary dependencies
  - Ensure Poetry configuration is properly set up for the challenge environment
  - _Requirements: 3.1, 3.2, 3.3, 3.4_

- [x] 2. Implement simple log file reader

  - Create iterator-based function in src/detector/sources.py that reads log files line by line
  - Handle both single file and directory input paths
  - Yield raw log lines as strings without any parsing or processing
  - _Requirements: 1.1, 1.2, 1.3, 2.1_

- [x] 3. Create placeholder detection function structure

  - Implement minimal placeholder class in src/detector/rules.py with process_log_line method
  - Function should accept raw log line string and return list of alert dictionaries
  - Include clear comments indicating this is for candidate implementation
  - _Requirements: 2.2, 2.3, 2.4, 2.5_

- [x] 4. Update detection pipeline for raw line processing

  - Modify src/detector/pipeline.py to use the log file iterator
  - Pass each raw log line to candidate detection function
  - Collect and aggregate results from candidate functions
  - _Requirements: 1.5, 2.6, 6.4_

- [x] 5. Update CLI interface for challenge requirements

  - Modify src/cli.py to handle input/output parameters as specified
  - Ensure proper integration with updated pipeline
  - Add basic error handling and user feedback
  - _Requirements: 1.6, 6.1, 6.2, 6.6_

- [x] 6. Create comprehensive README documentation

  - Write complete setup instructions including Poetry and Python 3.12 requirements
  - Document command-line usage with examples
  - Explain challenge objectives and expected deliverables
  - Include troubleshooting section for common issues
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.6_

- [x] 7. Add kill chain analysis section to README

  - Document the forensic investigation portion of the challenge
  - Recommend OpenSearch for log analysis with Docker installation link
  - Explain kill chain reconstruction as first deliverable
  - Provide guidance on analysis approach and expected output format
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [x] 8. Document detection implementation requirements

  - Add section explaining placeholder functions and candidate responsibilities
  - Specify expected alert output format and structure
  - Include examples of how to test implementations locally
  - Document submission requirements and evaluation criteria
  - _Requirements: 4.5, 6.3, 6.5_

- [ ] 9. Clean up existing code and remove unnecessary complexity

  - Remove existing detection rules that provide too much guidance
  - Simplify pipeline to focus on raw line processing
  - Remove any parsing logic that candidates should implement themselves
  - Ensure codebase provides minimal framework without revealing detection approaches
  - _Requirements: 2.4, 2.5_

- [x] 10. Add comprehensive type hints to all existing code

- [x] 10.1 Add type hints to CLI module (src/cli.py)

  - Add type annotations for all function parameters and return values
  - Import necessary typing modules (Optional, Dict, Any, etc.)
  - Ensure main() function and argument parsing have proper type hints
  - _Requirements: 7.1, 7.2, 7.3, 7.5_

- [x] 10.2 Add type hints to log sources module (src/detector/sources.py)

  - Add type annotations for file reading functions and iterators
  - Use Path type for file path parameters
  - Ensure Iterator type hints for log line generators
  - _Requirements: 7.1, 7.2, 7.3, 7.5_

- [x] 10.3 Add type hints to detection pipeline (src/detector/pipeline.py)

  - Add type annotations for DetectionPipeline class and all methods
  - Include type hints for class attributes and instance variables
  - Ensure proper typing for pipeline orchestration methods
  - _Requirements: 7.1, 7.2, 7.3, 7.5_

- [x] 10.4 Add type hints to output sink module (src/detector/sink.py)

  - Add type annotations for OutputSink class and all methods
  - Use Dict[str, Any] for alert data structures
  - Include proper typing for file operations and JSON handling
  - _Requirements: 7.1, 7.2, 7.3, 7.5_

- [x] 10.5 Add type hints to detection rules module (src/detector/rules.py)

  - Add comprehensive type annotations to ThreatDetector class
  - Include type hints for placeholder methods that candidates will implement
  - Define type aliases for common data structures (AlertDict, LogEntry, etc.)
  - Ensure candidate-facing functions serve as typing examples
  - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.7_

- [ ]\* 10.6 Add mypy configuration and type checking validation

  - Create mypy.ini configuration file with appropriate settings
  - Add type checking to development workflow
  - Ensure all modules pass mypy validation without errors
  - Document type checking process in README
  - _Requirements: 7.6, 7.8_

- [ ] 11. Update documentation to include type hints guidance

- [ ] 11.1 Add type hints section to README

  - Document type annotation requirements for candidates
  - Provide examples of proper typing patterns
  - Explain typing imports and common patterns used in the codebase
  - Include guidance on type checking tools and validation
  - _Requirements: 7.4, 7.7_

- [ ] 11.2 Update code examples in README with type hints
  - Ensure all code snippets in documentation include proper type annotations
  - Update function signatures and class examples
  - Demonstrate typing best practices in all examples
  - _Requirements: 7.4, 7.5, 7.7_
