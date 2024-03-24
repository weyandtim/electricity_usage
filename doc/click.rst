.. _click-ref:

Click CLI
=============

The :program:`electricity_usage` command accepts the following subcommands: ``start``, ``stop``, ``run``, ``areas``, ``queue``. If none of these are used, the command does nothing.

   .. click:: electricity_usage.__main__:cli
    :prog: electricity_usage
    :nested: full

The options for :option:`area` correspond to the area codes used by the Eleectricity Maps API. For a full list of codes and corresponding areas, see :ref:`api-ref`

