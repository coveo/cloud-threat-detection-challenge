from typing import Dict, Any, Optional
from .sink import OutputSink

# Type aliases for common data structures
AlertDict = Dict[str, Any]
LogEntry = Dict[str, Any]


class ThreatDetector:
    """
    PLACEHOLDER CLASS FOR CANDIDATE IMPLEMENTATION

    This class contains placeholder methods that candidates must implement
    to complete the threat detection challenge.

    DO NOT modify the method signatures - the pipeline expects these exact interfaces.
    """
    
    output_sink: OutputSink
    
    def __init__(self, output_sink: OutputSink) -> None:
        """
        Initialize threat detector with output sink for writing results.
        
        Args:
            output_sink: OutputSink instance for writing enriched logs and alerts
        """
        self.output_sink = output_sink

    def process_log_line(self, raw_line: str) -> None:
        """
        PLACEHOLDER METHOD - IMPLEMENT YOUR DETECTION LOGIC HERE

        This method receives a raw log line as a string and processes it for threats.
        When threats are detected, write enriched logs/alerts to the output sink.

        Args:
            raw_line (str): Raw log line from input files

        Side Effects:
            Writes alerts/enriched logs to self.output_sink when threats detected.
            Use self.output_sink.write_alert(alert_dict) to write results.
        """
        # TODO: IMPLEMENT YOUR DETECTION LOGIC HERE
        pass  # Replace this with your implementation
