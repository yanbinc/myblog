.. _Note_SMV_Study:

Note : SMV Study
=====================

SMV Overview
------------------
    
    System Margin Validation(SMV) is a methodology for verifying the signal integrity
    of a circuit board and assessing how much margin is in the design relative to
    silicon characteristic and processes that vary over time,including voltage,
    frequency,humidity and component aging,among other factors. [#HMME]_

    Because of cost constraints, the amount of testing before mass production generally
    does not exceed dozens to hundreds of system plus environment combinations.
    UPM need to be extrapolated from small batch test results.

    Unit Per Million(UPM) is the number of fail unit per million systems.
    General standard of SI IO is 50upm.

    **TakeAway Points**

    One key question that needs to be answered before mass production of different
    chips/IPs is **how to infer mass production risks from laboratory small batch testing?**


SMV Measurement Requirement
----------------------------------

.. csv-table:: SMV Measurement Items
   :header: "Type", "Item", "Description"
   :widths: 10, 10, 30

   "Monte-Carlo", PVT+Reboot,"DOE"
   "Guard-Band", "LTME", "Long-Term Margin Extrapolation"
   "Guard-Band", "Aging", ""
   "Guard-Band", "Impedance", "Impedance variation impact"
   "Guard-Band", "LBHR", "Low Temp boot High Temp Run"
   "Guard-Band", "Padanoia", ""

SMV Detail and Coding
------------------------------

Pending...(Secret)


SMV Result Demo
--------------------------

**The content of this table is fictitious and is for display only.**

Based on this brief UPM table we can get that
the DDR can reach 1dpc 4800 and 2dpc 4000 with mass production low risk.

    .. image:: ../blogstatic/SMV/upm_result_demo.png





Reference Book:
-----------------------
    
.. [#HMME] Determining How Much Electrical Margin is Enough to Ship a Product. Stephen Peters,David Shykind,et al,. DTTC 2005(Intel Internal Conference)

    
    