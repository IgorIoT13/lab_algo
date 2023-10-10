class ErrorWithInfo (Exception):
    def __init__(self):
        self.meseg = "Error with into valuer"
        super().__init__(self.meseg)