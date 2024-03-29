.. _usage-ref:

How to use electricity_usage
=====================================================================

``electricity_usage`` is used via commandline interface made with `click <https://pypi.org/project/click/>`_. The command documentation can be found in :ref:`click-ref`

Functional subcommands
-------------------------------------
The intended use of ``electricity_usage`` is as follows:

1. Start the tool using the subcommand ``electricity_usage start [OPTION]``
    - Use the ``&`` operator to start the tool as a background process. You will not be able to queue jobs otherwise.
    - The "start" command is used to create a new instance of a scheduler called daemon
    - The command has an optional argument ``area``, which defaults to Germany. If you wish to compare data from a different region, you can specify it here.

2. To add jobs to the queue, use ``electricity_usage run [OPTION]``. All jobs must be given the required parameters, which are:
    - ``--estimate`` <int>
    - ``--deadline`` <datetime>
    - ``--commandline`` <string>

   For a more detailed description, see :ref:`click-ref`

3. **To stop the tool and abandon all queued jobs, use** ``electricity_usage stop``.

Optional Subcommands
-----------------------------------

* With the ``electricity_usage areas`` command you can see a list of all provided area codes. 
* With the ``electricity_usage queue`` command you can see a list of all jobs currently in the queue.

