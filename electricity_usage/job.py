import datetime

# This class serves as a data structure for storing job parameters.
class Job:
    def __init__(self, job_id, estimate, deadline, commandline):
        self.job_id = job_id
        self.estimate = estimate
        self.deadline = deadline
        self.commandline = commandline

