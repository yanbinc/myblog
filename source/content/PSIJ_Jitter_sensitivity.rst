.. _PSIJ_Jitter_sensitivity:

JTF(jitter transfer tunction)
----------------------------------------
    .. math::
        J(f)=H(f)V(f)
    .. math::
        H(f)=\frac{j}{2 \text{$\pi $f$\tau $}_d}H_0\text{[1-}e^{-\text{j2$\pi $f$\tau $}_d}]
    .. math::
        \left| H(f)\right|=H_0\left| sinc(f\tau _d)\right|
    .. math::
        H_0\text{= }\frac{T_d^{V_{\min }}-T_d^{V_{\max }}}{V_{\max }-V_{\min }}
    
    .. image:: ../blogstatic/PSIJ/psij_h0.png
    
    Refernce Paper: [#ATFRPGV]_  [#SNIJMO]_ 
    
    .. image:: ../blogstatic/PSIJ/jtf_1.png
    
    .. literalinclude:: ../blogstatic/PSIJ/plot_JS.py
    
    .. image:: ../blogstatic/PSIJ/jtf_2.png 
    
    .. image:: ../blogstatic/PSIJ/jtf_3.png 
    
    [#ATFRPGV]_
    
    
    .. [#ATFRPGV] Analytical Transfer Functions Relating Power and Ground Voltage Fluctuations to Jitter at a Single-ended Full-swing Buffer. Chulsoon Hwang
    .. [#SNIJMO] Supply Noise Induced Jitter Modeling and Optimization for High-Speed Interface. Yujeong shim and Guang Chen.
