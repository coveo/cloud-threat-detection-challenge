from .sources import read_log_files
from .rules import ThreatDetector
from .sink import OutputSink


class DetectionPipeline:
    """
    Detection pipeline that processes log files line by line through candidate detection functions.

    This pipeline reads log files using the log file iterator, passes each raw log line
    to candidate-implemented detection functions, and coordinates output through a sink.
    """

    def __init__(self, input_path: str, output_path: str):
        """
        Initialize the detection pipeline.

        Args:
            input_path: Path to input file or directory containing log files
            output_path: Path to output file for writing results
        """
        self.input_path = input_path
        self.output_path = output_path

    def process_logs(self) -> None:
        """
        Process all log files through candidate detection functions.

        Reads log files line by line using the log file iterator and passes each
        raw line to the candidate detection function. The detection function
        performs side effects by writing alerts/enriched logs to the output sink.
        """
        with OutputSink(self.output_path) as output_sink:
            # Initialize detector with output sink
            detector = ThreatDetector(output_sink)

            try:
                # Use the log file iterator to read files line by line
                for raw_line in read_log_files(self.input_path):
                    # Skip empty lines
                    if not raw_line.strip():
                        continue

                    # Pass raw line to candidate detection function
                    self.process_line(detector, raw_line)

            except Exception as e:
                print(f"Error processing logs: {e}")
                # Continue processing - output sink will be properly closed

    def process_line(self, detector: ThreatDetector, raw_line: str) -> None:
        """
        Process a single raw log line through candidate detection functions.

        Args:
            detector: ThreatDetector instance with output sink
            raw_line: Raw log line string from input files
        """
        try:
            # Pass raw line to candidate-implemented detection function
            # Detection function performs side effects via output sink
            detector.process_log_line(raw_line)

        except Exception as e:
            print(f"Error processing line: {e}")
            # Continue processing other lines
