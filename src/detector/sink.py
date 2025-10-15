import json
from typing import Dict, Any


class OutputSink:
    """
    Output sink for writing enriched logs and alerts to output file.
    
    Provides interface for candidates to write detection results and enriched
    log entries to the specified output file in JSON format.
    """
    
    def __init__(self, output_path: str):
        """
        Initialize output sink with target file path.
        
        Args:
            output_path: Path to output file for writing results
        """
        self.output_path = output_path
        self.output_file = None
        self._initialize_output_file()
    
    def _initialize_output_file(self):
        """Initialize the output file for writing."""
        try:
            self.output_file = open(self.output_path, 'w', encoding='utf-8')
            # Start JSON array
            self.output_file.write('[\n')
            self._first_entry = True
        except (IOError, OSError) as e:
            print(f"Error initializing output file {self.output_path}: {e}")
            raise
    
    def write_alert(self, alert: Dict[str, Any]) -> None:
        """
        Write alert or enriched log entry to output file.
        
        Args:
            alert: Dictionary containing alert/enriched log data
        """
        if not self.output_file:
            print("Warning: Output file not initialized, cannot write alert")
            return
        
        try:
            # Add comma separator for subsequent entries
            if not self._first_entry:
                self.output_file.write(',\n')
            else:
                self._first_entry = False
            
            # Write JSON entry with proper indentation
            json_str = json.dumps(alert, indent=2, ensure_ascii=False)
            # Indent the entire JSON object
            indented_json = '\n'.join('  ' + line for line in json_str.split('\n'))
            self.output_file.write(indented_json)
            self.output_file.flush()  # Ensure data is written immediately
            
        except Exception as e:
            print(f"Error writing alert to output file: {e}")
    
    def close(self) -> None:
        """Finalize output file and cleanup resources."""
        if self.output_file:
            try:
                # Close JSON array
                self.output_file.write('\n]\n')
                self.output_file.close()
                self.output_file = None
            except Exception as e:
                print(f"Error closing output file: {e}")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()