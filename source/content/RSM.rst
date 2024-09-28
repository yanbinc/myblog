.. _RSM:

RSM Coding
==============================
    
    
Introduction
------------------
    The response surface modeling (RSM) technique provides a tool that gives us the ability to model 
    the behavior of our signaling system as the circuit and interconnect characteristics vary. 
    RSM works by fitting a statistical model of the output response as a function of changes in the input variables. [#ASIHSDD]_
    
    The general form of the response surface model is 
    y is the system response. β is the model fit coefficients. x is the system input.
    
    .. math::
        y=\beta _0+\beta _1 X_1+\beta _2 X_2+\text{...}+\beta _k X_k+\epsilon
    
    It is highly flexible, allowing to fit curved response surface by using higher-order combinations of input variables.
    In general ,second-order models are sufficient for high-speed signaling links.
    
    .. math::
        y=\sum _{i=1}^{n_{\text{var}}} X_i^2 \beta _{\text{ii}}+\sum _{i=1}^{n_{\text{var}}} \sum _{j\neq i}^
        {n_{\text{var}}} X_i \beta _{\text{ij}} X_j+\sum _{i=1}^{n_{\text{var}}} \beta _i X_i+\beta _0
    
RSM  Procedure
---------------------
    Let's understand this by using step by step coding.
    
After finish a Doe simulation . we will get an input and output table.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    .. image:: ../blogstatic/RSM/doe_1.png
    
Generate a second-order table.(focus on eye-height this time)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Input variable number is 12.[corner,cpu_pkg_z,cpu_pkg_len,brd_z,brd_ofld_len,dimm_z,dimm_len,
    dram_pkg_td,dram_pkg_z,dram_cdie,dram_tol0,dram_tol1]
    
    .. math::
        k=\frac{1}{2} \left(n_{\text{var}}-1\right) n_{\text{var}}+2 n_{\text{var}}+1
    
    Then the amount of terms in 2nd-ord RSM model , k , is  91 (1+2*12+12*(12-1)/2=91)
    
    see the number and list 
    
    .. image:: ../blogstatic/RSM/doe_var.png
    
    check the corresponding value with input matrix.
    
    .. image:: ../blogstatic/RSM/X_matrix.png
            
Normalize the martix.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Rather than use the raw data, regression tool usually fit the model to a transformed version of data.
    The purpose is to minimize the infulence of different term's coefficient.
    Refernce Book [#ASIHSDD]_ proposal an round normalization while I suggest to use legacy normalization.
    See following comparison.
    
    .. image:: ../blogstatic/RSM/norm.png
    
    Which method is better? Let's see the result in MMSE part.
            
Regression Analysis.
^^^^^^^^^^^^^^^^^^^^^^^
    MMSE result 
    
    .. image:: ../blogstatic/RSM/mmse_result.png
    
    Conclusion: The result shows normalized X is better than Round Normalized X in regression analysis.
    
    Why?
    
    Sometimes DOE table is not **orthogonal array**. Round Normalization introduce extra error.
            
Regression Result Criteria.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Residuals vector / standard residual/R-square/R-square_adj/RMSE 
    
    .. math::
        \text{e=}\hat{y}-y
    .. math::
        \text{d=e/}\hat{\sigma }
    .. math::
        R^2=1-\text{SS}_{\text{error}}/\text{SS}_{\text{total}}
    .. math::
        R^2{}_{\text{adj}}=\left(\text{SS}_{\text{error}}\right./\text{dF}_{\text{error}}\text{)/}\left(\text{SS}_{\text{total}}\right./\text{dF}_{\text{total}})
    .. math::
        \text{RMSE=}\sqrt{\frac{\text{SS}_{\text{error}}}{\text{dF}_{\text{error}}}}
    .. math::        
        \text{SS}_{\text{error}}=\sum _{i=0}^n \left(\hat{y}_i-\bar{y}\right){}^2=y^{\mathsf{T}} y-b^{\mathsf{T}} x^{\mathsf{T}}y
    
    .. image:: ../blogstatic/RSM/criteria_2.png
    
    .. image:: ../blogstatic/RSM/criteria_3.png
            
Significant Test.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Model significance : the F-Test
    
    .. math::
        F_0=\left(\text{SS}_{\text{model}}\right./\text{dF}_{\text{model}}\text{)/}\left(\text{SS}_{\text{error}}\right./\text{dF}_{\text{error}})
    
    Parameter significance : Individual t-Tests
    
    .. math::
        t_{0 i}=b_i/\text{SE}_i
    
    .. literalinclude:: t_test.py
    
    .. image:: ../blogstatic/RSM/t_test2.png
    
    Accoring to Refernce Book [#ASIHSDD]_ , 'At a 95% confidence level, the critical value for the t-statistic is
    2.365 obtrained from Appendix D. Result of the hypothesis tests are listed in the rightmost column of the 
    table ,which show that 11 of the 20 model terms are significant for eye width model.All other terms can be
    removed from the model without significant degradation in the model fit'
    
    .. image:: ../blogstatic/RSM/summary_tf_test.png
    
    My option is not good . Refernce Book [#MAO]_ propose to use stepwise for further optimization.
    
    **Stepwise is not considered in this document**.
            
Result comparison with commerical tool [#JMP]_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    JMP's MMSE result .(RSM backward sim stepwise 1st time result with full parameter) 
    
    .. image:: ../blogstatic/RSM/jmp_1.png
    
    .. image:: ../blogstatic/RSM/jmp_2.png
    
    Coefficients Comparison.
    
    .. image:: ../blogstatic/RSM/jmp_3.png
    
    Conclusion:
    
    Constant and 1st order item coefficient value show **big difference**.
    
    2nd order item coefficient value show **good correlation**.
    
    The output estimate by coefficient shows **good correlation**. 
    
    It's weird.   **Why?**
    
    After review the output , i find the root cause is **different expression**.
    
    Orginal JMP Equation 
    
    .. image:: ../blogstatic/RSM/jmp_math_1.png
    
    Expand polynomial expressions in Mathematica
    
    .. image:: ../blogstatic/RSM/jmp_math_2.png
    
    After expand the equation,Correlate well.
    
    .. image:: ../blogstatic/RSM/jmp_math_3.png
    
    .. image:: ../blogstatic/RSM/jmp_comparison_1.png
            
Conclusion.
^^^^^^^^^^^^^^^^^^^^
            Current code can correlate JMP stepwise 1st step well.
    
UPM Analysis.
^^^^^^^^^^^^^^^^^^^^^^^^^
            Generate 1Million row variable table and get the output according to equation after stepwise. 
            
            Sort the result to see the system's performance. Eg.0.01% value.
            
            
    .. [#ASIHSDD] Advanced Signal integrity for high speed digital design.  Stephen H.HALL & Howard L.Heck
    .. [#JMP] JMP help.
    .. [#MAO] Regression analysis and experiment design. Shisong Mao.
    
