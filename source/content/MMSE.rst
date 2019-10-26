.. _MMSE:

Minimum Mean Square Error 
==============================
    
    
Introduction
------------------
    An estimation method which minimizes the mean square error (MSE),
    which is a common measure of estimator quality, of the fitted values of a dependent variable.
    
Question
-------------
    Assume we have a lot of data. we make an equation of matrix Y,X
    
    .. math::
        y_1=\beta _0+\beta _1 X_{11}+\beta _2 X_{12}+\text{...}+\beta _k X_{1 k}+\epsilon _1
    .. math::
        y_2=\beta _0+\beta _1 X_{21}+\beta _2 X_{22}+\text{...}+\beta _k X_{2 k}+\epsilon _2
    .. math::
        \text{...}
    .. math::
        y_n=\beta _0+\beta _1 X_{\text{n1}}+\beta _2 X_{\text{n2}}+\text{...}+\beta _k X_{\text{nk}}+\epsilon _n
    
    What we want is get B matrix to estimate Y
    
    .. math::
        \hat{y}=\beta _0+\beta _1 X_1+\beta _2 X_2+\text{...}+\beta _k X_k
    
    How????
            
Math Algorithm
----------------------
    
    
    A popular algorithm is MMSE.
    MMSE  definition is to minimize the error of y and y-estimate 
    
    .. math::
        &\text{Err=}\sum _n\left(y_n-\hat{y}_n\right){}^2\\
        &\text{Err=}\sum _n\left(y_n-\beta _0-\beta _1 X_{\text{n1}}-\beta _2 X_{\text{n2}}-\text{...}-\beta _k X_{\text{nk}}\right){}^2
    
    With given data, Err is β's non-negative 2nd order function. It's minimum value is exist.
    The partial derivative should be zero for error minimization.
    
    .. math::
        &\partial \text{Err}\left/\partial \beta _0\right.=-2 \sum _n \left(y_n-\hat{y}_n\right)=0\\
        &\partial \text{Err}\left/\partial \beta _j\right.=-2 \sum _n \left(y_n-\hat{y}_n\right) X_{\text{nj}}=0 \       j=1,2,\text{...},k
    
    Normal Equations
    
    .. math::
        &\sum _n\left(y_n-\beta _0-\beta _1 X_{\text{n1}}-\beta _2 X_{\text{n2}}-\text{...}-\beta _k X_{\text{nk}}\right)=0\\
        &\sum _n\left(y_n-\beta _0-\beta _1 X_{\text{n1}}-\beta _2 X_{\text{n2}}-\text{...}-\beta _k X_{\text{nk}}\right)X_{\text{nj}}=0 j=1,2,\text{...},k
        
        
        
    .. math::
        &\text{N$\beta $}_0+\beta _1 \left(\sum _n X_{\text{n1}}\right)+\beta _2 \left(\sum _n X_{\text{n2}}\right)+\text{...}+
        \beta _k \left(\sum _n X_{\text{nk}}\right)=\sum _n y_n\\
        &\beta _0 \left(\sum _n X_{\text{n1}}\right)+\beta _1 \left(\sum _n X^2{}_{\text{n1}}\right)+\beta _2 \left(\sum _n X_{
        \text{n1}} X_{\text{n2}}\right)+\text{...}+\beta _k \left(\sum _n X_{\text{n1}} X_{\text{nk}}\right)=\sum _n y_n X_{\text{n1}}\\
        &\text{...}\\
        &\beta _0 \left(\sum _n X_{\text{nk}}\right)+\beta _1 \left(\sum _n X_{\text{n1}} X_{\text{nk}}\right)+
        \beta _2 \left(\sum _n X_{\text{n2}} X_{\text{nk}}\right)+\text{...}+\beta _k \left(\sum _n X^2{}_{\text{nk}}\right)=
        \sum _n y_n X_{\text{nk}}
    
    Left side coefficient Matrix is symmetric matrices
    
    .. math::
        A=X'X
    
    .. math::
        A&=\begin{vmatrix}
        &N&\sum _n X_{\text{n1}} &\sum _n X_{\text{n2}}&\text{...}&\sum _n X_{\text{nk}} \\ 
        &\sum _n X_{\text{n1}}&\sum _n X^2{}_{\text{n1}}&\sum _n X_{\text{n1}} X_{\text{n2}}&\text{...}&\sum _n X_{\text{n1}} X_{\text{nk}}\\
        &\text{...}&\text{...}&\text{...}&\text{...}&\text{...}\\
        &\sum _n X_{\text{nk}}&\sum _n X_{\text{n1}} X_{\text{nk}}&\sum _n X_{\text{n2}} X_{\text{nk}}&\text{...}&\sum _n X^2{}_{\text{nk}}
        \end{vmatrix}\\
        &=\begin{vmatrix}
        &1&1&1&\text{...}&1 \\ 
        &X_{11}&X_{21} &X_{31}&\text{...}&X_{n1} \\ 
        &\text{...}&\text{...}&\text{...}&\text{...}&\text{...}\\
        &X_{1k}&X_{2k} &X_{3k}&\text{...}&X_{nk} \\ 
        \end{vmatrix}
        \begin{vmatrix}
        &1&X_{11} &X_{12} &\text{...}&X_{1k}  \\ 
        &1&X_{21} &X_{22}&\text{...}&X_{2k} \\ 
        &\text{...}&\text{...}&\text{...}&\text{...}&\text{...}\\
        &1&X_{n1} &X_{n2}&\text{...}&X_{nk} \\ 
        \end{vmatrix}
    
    Right side constant item Z can be expressed in
    
    .. math::
        Z=X'Y
    .. math::
        Z=\begin{vmatrix}
        \sum _n Y_{\text{n}}\\
        \sum _n X_{\text{n1}} Y_{\text{n}}\\
        \text{...}\\
        \sum _n X_{\text{nk}} Y_{\text{n}}
        \end{vmatrix}=
        \begin{vmatrix}
        &1&1&1&\text{...}&1 \\ 
        &X_{11}&X_{21} &X_{31}&\text{...}&X_{n1} \\ 
        &\text{...}&\text{...}&\text{...}&\text{...}&\text{...}\\
        &X_{1k}&X_{2k} &X_{3k}&\text{...}&X_{nk} \\ 
        \end{vmatrix}
        \begin{vmatrix}
        Y_{\text{1}}\\
        Y_{\text{2}}\\
        \text{...}\\
        Y_{\text{n}}
        \end{vmatrix}
        
    Finally
    
    .. math::
        \left(X'X\right)B=X'Y
    .. math::
        B=\left(X'X\right)^{-1}X'Y
                
MMSE Example
----------------------
    
    .. csv-table:: Data for Analysis
        :widths: 20 10 10 10 10 10 10 10 10 10
        :stub-columns: 1
        :file: solubility.csv
    
    Using 1st-order function to calculate B
    
            
            .. image:: ../blogstatic/MMSE/plot.png
            
            .. literalinclude:: mmse_example.py
        
        