.. _usage-ref:

Usage
============================

How to use electricity_usage
----------------------------

electricity_usage ist used via an commandline Interface made with click,
it provides the following commands:

* ``electricity_usage start --area 'DE'``
    - The "start" command is used to create a new instance of a scheduler called daemon
    - The command utilizes an Area Key to retrieve details regarding both electricity generation and usage.

* ``electricity_usage run --estimate 1000 --deadline 2024-12-12 10:10:10  --commandline "echo Hello World"``
    - The "run" command adds a new job to the schedule
    - Every job needs the following parameter:
        - estimate <int> is an intiture value reflecting the aproximate runtime of the job
        - deadline <YYYY-MM-DD HH:MM:SS> is the time the job needs to be done the deadline needs to be in the future
        - commandline "echo Hello World" the commandline is executed when a run condition is met

* ``electricity_usage stop``
    - The "stop" command is used to stop the scheduler
    - By execution the command all existing jobs get remooved

* ``electricity_usage areas``
    - The "areas" command retrieves a list of available area keys.

* ``electricity_usage queue``
   - The "queue" command retrieves a list of jobs in queue
