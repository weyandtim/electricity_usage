.. _api-ref:

Introduction to Electricity Maps:
=================================
Electricity Maps is a realtime Data API about electricity consumption, production and carbon intensity


How we use Electricity Maps:
----------------------------
electricity_usage utilizes the Electricity Maps API to retrieve location-specific data
on electricity production and consumption, 
based on which our scheduler determines when to execute jobs.

In order to use electricity_usage properly you are required to 
get the personal free tier subscription of Electricity Maps
which can be obtained here `<https://api-portal.electricitymaps.com/>`_

For more informaion on how to set up electricity_usage view installation.


How does Electricity Maps work:
-------------------------------

On subscribing to Electricity Maps you will be granted a authentification token 
it is used along with an area Code such as 'DE' for Germany to retriev detailed data about 
area speciffic electricity consumption and production.

For more information about Electricity Maps check out `<https://static.electricitymaps.com/api/docs/index.html#personal-and-commercial-use>`_ 
