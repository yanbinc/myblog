.. _PSIJ_Study_Note:

Brief definition.
--------------------------


    PSIJ is dependent on three key factors, the current of aggressors / victims, PDN / regulator characteristics and jitter sensitivity to power supply noise of the victim circuits.
    Power Supply Inculde jitter is a bounded random jitter.
    
    .. image:: ../blogstatic/PSIJ/psij_analysis_flow.png
    
    Jitter Categories
    
    .. image:: ../blogstatic/PSIJ/Jitter_categories.png
    
    jitter Plot with python
    
    .. image:: ../blogstatic/PSIJ/Jitter_plot.png


Power noise impact on timing variation.
-------------------------------------------

    .. image:: ../blogstatic/PSIJ/noiseimpacttiming.png
    
    A buffer has different delay at different supply voltage.For the low supply voltage , the delay gets longer while it is another way around for the higher supply voltage. [#IDPSNIC]_
    Simply,the delay is inverse proportional to the supply voltage because transconductance,gm, is proportional to the voltage (Vgs-Vth) in Saturation mode.
    Hence,as the voltage is higher ,resistance is less so that the delay is less as illustrated in Fig.


.. [#IDPSNIC] Impact of Dynamic Power Supply Noise Induced by Clock Networks on Clock Jitter and Timing Margin. Yujeong shim and Dan oh.

