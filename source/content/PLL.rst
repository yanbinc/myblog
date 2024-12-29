.. _Note_PLL_Study:




phasenoise to jitter














1. 导入scope量测的时钟信息bin文件。- 怀疑是phase noise（period jitter）
2. 导入scope量测的底噪 - phasenoise

3. 分析
    - 导入信息中需要有时钟的基础信息，比如频率，幅度
    - 查看是否有完整的过零点
    - 增加了额外的LPF
    -




VCO
******************

VCO 振荡器就是LC Loop

它的谐振频率

    .. math::
     f = \frac{1}{2\pi\sqrt{LC}}

L中有寄生电阻，会衰减震荡。L的储能就显得很重要，定了了品质因素Q

    .. math::
     Q_{L}(f) = \frac{X_{L}}{R} = \frac{2\pi fL}{R}$

在LC loop中添加激励，则完成了整个VCO的搭建。

可变电容器 一般是switched capacitor bank。


除法器
******************

整型
-----------

单模预分频
^^^^^^^^^^^^^^^^

Single Modulus Prescaler

B counter & 1/P P是2的幂

    .. math::
     N = 2^{P}

    .. math::
     N = \frac{f_{VCO}}{f_{N}} = \frac{f_{VCO}}{f_{PD}}

缺点，频率分辨率差了P倍。

双模预分频
-------------

Dual modulus presaler

A counter & 1/P
B counter & 1/(P+1) B>=A

最终为（B-A）



Loop Filter
*********************


    .. math::
    F(s) =\frac{1+s\tau _{2}}{1+s( \tau _{1} +\tau _{2})}\
    \tau _{1} =R_{1} C\
    \tau _{2} =R_{2} C\







