class Job:
    def __init__(self, job_id, estimate, deadline, area, commandline):
        self.job_id = job_id
        self.estimate = estimate
        self.deadline = deadline
        self.area = area
        self.commandline = commandline