class SerialGenerator:
    """
    Generates a random serial number. Increases by 1 each time.

    Attributes:
        start : automatically starts at 0 unless defined
    """
    def __init__(self,start=0):
        self.start = self.new = start

    def __repr__(self):
        return f"Generates serial number starting at {self.start}."

    def generate(self):
        """Generates a new serial number, increases by one each time"""
        self.new += 1
        return (self.new - 1)

    def reset(self):
        """Resets the serial number back to inital starting amount"""
        self.new = self.start
