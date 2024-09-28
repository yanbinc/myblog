.. _Note_SMV_Study:

Note : SMV Study
=====================

SMV Overview
------------------
    
    System Margin Validation(SMV) is a methodology for verifying the signal integrity
    of a circuit board and assessing how much margin is in the design relative to
    silicon characteristic and processes that vary over time,including voltage,
    frequency,humidity and component aging,among other factors. [#HMME]_

    由于成本限制，量产前的实验室单个接口shmoo测试的芯片/单板往往不超过25pcs（5pcs/corner），

    基于测试需要判断量产的风险

    Unit Per Million(UPM) 指百万个系统里面的故障数。(一般intel的标准是UPM50)

    **核心要点**

    回答了如何基于实验室小批量测试来**数值化**外推量产风险，而不是单薄的低/中低/中/高风险。


SMV 测试分类
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


SMV Result Demo
--------------------------

**The content of this table is fictitious and is for display only.**

Based on this brief UPM table we can get that
the DDR can reach 1dpc 4800 and 2dpc 4400 with mass production low risk.

    .. image:: ../blogstatic/SMV/upm_result_demo.png


SMV's Advantage
--------------------------------

#) 传统测试方法

    #) 长期稳定压力测试

    #) 加压测试(降低电压，或者提升频率档位)

#) 传统测试方法的不足

    #) 只有pass/fail，没有数值，所以无法数学分析

    #) 加压测试的signoff太依赖于经验，随着速率越来越高，判决准确率越来越低

    - eg：上一代产品，电压min=0.9v，而一直降低到0.8v，实验室系统都能稳定运转。基于此给出了pass结论。而新的产品，电压只能到0.82V.问，现在是否仍能满足量产要求？如果电压是0.85v又如何？

#) SMV的优势

    #) SMV可以给出数值解析解。

    #) SMV的UPM结果和仿真UPM的拟合。可以修正仿真spec，可以预测改版/设计变动的量产风险。甚至如果下一代模拟设计架构不变，可以用来修正下一代的timing table


Reference Book:
-----------------------
    
.. [#HMME] Determining How Much Electrical Margin is Enough to Ship a Product. Stephen Peters,David Shykind,et al,. DTTC 2005(Intel Internal Conference)

    
    