Click CLI
=============

The :program:`electricity_usage` command accepts the following subcommands: ``start``, ``stop``, ``run``, ``areas``, ``queue``. If none of these are used, the command does nothing.
<!--
   .. click:: electricity_usage.__main__:cli
    :prog: electricity_usage
-->
The subcommands ``start`` and ``run`` take additional options, as listed below. 

   .. click:: electricity_usage.commands.start:start
   :prog: start


