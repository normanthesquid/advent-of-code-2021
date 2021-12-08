class display:
    def __init__(self, definition: str):
        signal_pattern_string, output_value_string = definition.split(" | ")

        self.signal_patterns = signal_pattern_string.rstrip().split()

        self.output_values = output_value_string.rstrip().split()
