System Architecture and Backend Functionality
==============================================

Arkitecture
------------

Electricity Usage consists of:

Frontend:  
    - Command-line interface (CLI) built with Click. For more information, see :ref:`click-ref`.

Backend:  
    - Daemon (daemon.py): A scheduler responsible for initiating processes by executing command-line instructions and processing data.  
    - data_dirs.py: used to define a directory for communication between the daemon and the CLI.  
    - em_data.py: utilized to retrieve data from Electricity Maps.  

Backend Operation
------------------

Creating a Daemon Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A daemon instance is created using the start command of our CLI.

.. code-block:: python

    data_dir = data_dirs.create_input_dir_path()
    # create daemon instance
    daemon_instance = daemon.Daemon(em_auth_token, area, data_dir)

    # start daemon.run in separate thread
    daemon_thread = threading.Thread(target=daemon_instance.run) 

    daemon_thread.start()

By creating a daemon instance, a watchdog observer is created to monitor the specified `data_dir`, 
which serves as a communication pathway between the CLI and daemon. 
Watchdog is a Python package used to monitor changes to a directory, 
functioning cross-platform. 
Learn more about watchdog at `<https://python-watchdog.readthedocs.io/en/stable/>`_.

Daemon Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **run(self):**

    Executes the command-line of a job if one of the following conditions is met:
    
    - When electricity production exceeds consumption.
        .. code-block:: python
    
            if power_consumption < power_production:
                # execute command
    
    - When the job's latest starting point (latest_starting_point = deadline - estimate) is less than or equal to the current time.
        .. code-block:: python
    
            if job_instance.latest_starting_point <= datetime.datetime.now():
                # execute command
    
    The conditions are checked periodically (every 20 minutes due to updates in electricity production and consumption values).


- **process_json_file(self, file_path):**

    This method reads information about new jobs from a JSON file in the `data_dir` directory and uses it to create a new job,
    which is then stored in the list jobs. 
    The method is automatically executed when a new JSON file is detected in the daemon's `data_dir` directory.


- **stop(self):**

    This method stops the execution of the `run` method by setting a stop event.
    It also cleans up the `data_dir` directory created in `data_dirs.py` and deletes the `daemon_instance`, 
    effectively deleting all current jobs. 
    The method is executed using the stop command of our CLI.

Communication (Daemon <-> CLI)
-------------------------------

Communication between the CLI and daemon occurs via the file system. 
We utilize `platformdirs` to access an independent folder. 
The structure of our communication folder is created in `data_dirs.py`. 
For more information about `platformdirs`, 
refer to the `<https://platformdirs.readthedocs.io/en/latest/>`_.

The CLI commands `run` and `stop` add files to the `input_dir` directory, 
which are then registered by the daemon using the Watchdog Observer. 
Watchdog is a Python package used to monitor changes to a directory, 
functioning cross-platform. 
Learn more about watchdog at `<https://python-watchdog.readthedocs.io/en/stable/>`_.
After a file is registered, corresponding daemon methods are invoked.