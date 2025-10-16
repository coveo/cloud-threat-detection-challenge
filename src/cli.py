import argparse
import sys
from pathlib import Path
from src.detector.pipeline import DetectionPipeline


def main():
    """
    Main entry point for the threat detection challenge CLI.

    Processes security logs through candidate-implemented detection functions
    and outputs results to specified file.
    """
    parser = argparse.ArgumentParser(
        description="Threat Detection Challenge - Process security logs through detection functions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  poetry run python -m src.cli --in /path/to/logs --out alerts.json
  poetry run python -m src.cli --in single_log.txt --out results.json
  poetry run python -m src.cli --in /path/to/directory
        """,
    )

    parser.add_argument(
        "--in",
        dest="input_path",
        required=True,
        help="Input file or directory containing log files to process",
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        default="alerts.json",
        help="Output file path for detection results (default: alerts.json)",
    )

    args = parser.parse_args()

    # Validate input path exists
    input_path = Path(args.input_path)
    if not input_path.exists():
        print(f"Error: Input path '{args.input_path}' does not exist", file=sys.stderr)
        return 1

    # Validate input is file or directory
    if not (input_path.is_file() or input_path.is_dir()):
        print(
            f"Error: Input path '{args.input_path}' must be a file or directory",
            file=sys.stderr,
        )
        return 1

    # Create output directory if it doesn't exist
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Provide user feedback
    if input_path.is_file():
        print(f"Processing log file: {args.input_path}")
    else:
        print(f"Processing log files in directory: {args.input_path}")
    print(f"Output will be written to: {args.output_path}")

    try:
        # Initialize and run detection pipeline
        pipeline = DetectionPipeline(
            input_path=str(input_path), output_path=str(output_path)
        )

        print("Starting log processing...")
        pipeline.process_logs()

        # Check if output file was created and provide feedback
        if output_path.exists():
            file_size = output_path.stat().st_size
            print(f"Processing complete! Results written to {args.output_path}")
            print(f"Output file size: {file_size} bytes")
        else:
            print("Processing complete, but no output file was generated.")
            print(
                "This may indicate no alerts were detected or an issue with detection functions."
            )

    except KeyboardInterrupt:
        print("\nProcessing interrupted by user", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error during processing: {e}", file=sys.stderr)
        print(
            "Please check your input files and detection function implementation.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
