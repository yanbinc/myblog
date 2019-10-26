.. _PSIJ_Application:


    - A very simple and highly accurate expression for the power supply-induced jitter sensitivity transfer function for CMOS buffer chains.The key element for total system performance definition.
    - Improve the trade off between the power supply induced jitter (PSIJ) performance and the cost for the circuit (ODC,clk tree path).
    - Jitter tracking/anti-tracking (Memory and parallel bus interface).

    
Improve silicon design. [#RPSIJDDR]_
--------------------------------------------------------
    
    This thesis proposes the following techniques to achieve the goal:
    The static phase offset (SPO) is the dominant mechanism causing reference spurs in the
    spectrum of the multiplying delay-locked loop (MDLL) output. With a high-gain stage
    inserted between the phase detector/phase frequency detector and the charge pump, the
    equivalent SPO has been decreased by a factor equal to the gain of the gain stage. The
    effectiveness of the proposed technique has been verified at both behavioral level with a
    Simulink model and the transistor level with circuit simulation results.
    This thesis also presents a very simple and highly accurate expression for the power
    supply-induced jitter sensitivity transfer function for CMOS buffer chains. The transfer
    function is mainly a function of the maximum and minimum propagation delay of the buffer
    chain.
    Lastly in this thesis, a concise method is proposed for converting the frequency domain
    equivalent serial resistance (ESR) and equivalent serial capacitance (ESC) to an approximate
    broadband equivalent circuit which can be readily used in time domain jitter analysis.
    Finally a case study demonstrates that, with the proposed techniques in this dissertation,
    the MDLL based clock distribution circuit for a DDR controller improves the tradeoffii
    between performance and cost compared to the traditional phase locked loop (PLL) based
    clock distribution circuit.
    
    With technology scaling and increasing data rates, in modern integrated circuits, the average
    current density and power noise amplitude have increased due to decreasing power supply
    voltage and increasing switching speed. Reduced supply voltage causes reduced noise
    margins, large voltage variations and other signal integrity issues which could lead to design
    failures .
    Power supply noise is one of the major sources of timing jitter . It directly
    contributes to the jitter of the internal timing sources of the system, e.g., PLL (phase locked
    loop), DLL (delay locked loop) and clock distribution buffers. Jitter is a non-linear
    function of the magnitude and frequency of power supply noise. There is a band of power
    supply noise frequency that can create the worst type of jitter, the center frequency of which
    varies with its amplitude.
    
    This research focuses on the methods for estimating and improving PSIJ performance
    within the application of a double data rate (DDR) controller. **Jitter for the DDR controller is
    mainly caused by the clock multiplier, the clock tree, and the IO buffer. On-die
    measurement shows that 33% of the total jitter is contributed by the clock multiplier and the
    IO buffer; while 67% of the total jitter comes from the clock tree . The clock tree jitter is 5
    largely related to power supply noise.**
    Methods for improving system jitter performance and estimation have been deeply
    studied in the past decade. For example, to achieve low jitter clock multiplication,
    multiplying delay locked loop (MDLL) have been explored. ** 
    Compared to a PLL, an MDLL will be a better candidate for DDR controller applications because its
    superior phase noise outperforms the conventional PLL . Most importantly, any
    jitter created by the on-chip noise is completely corrected when a clean reference clock edge
    arrives at the input of the DLL. An MDLL achieves both low jitter and ease of design,
    however, its high reference spur limits its application. ** In this dissertation, an MDLL with
    static phase offset (SPO) reduction technique is proposed to overcome the limitations.
    Because the physical sizes of block PHYDATx8 and PHYAC shown in Figure 1.2 are
    large and the capacitive load of the output of clock multipliers is typically large, long clock
    buffer chains have been used. As a result, the PSIJ of a buffer chain becomes significant.
    The PSIJ must be well controlled and accurately estimated in jitter budget calculation.
    Conventionally a metric know as the alpha factor is used to estimate the PSIJ of a buffer
    chain; however, as data rate approaches multi-gigabits per second, this method becomes too
    pessimistic.
    To properly characterize the PSIJ, PSIJ analysis methodology has been
    proposed and applied to multi-gigabit I/O interface design. The key concept of power supply
    induced jitter sensitivity (PSIJS) has been proposed and applied to PSIJ analysis. PSIJS of
    single buffer  and PSIJ of two- stage and multi-stage buffers have been
    studied. In this dissertation a simple and concise PSIJS expression of multi-stage buffer
    chain is derived, which can be used to calculate PSIJ of buffer chains quickly and
    accurately.
    To decrease PSIJ, an on-die decoupling capacitor (ODC) is often the most effective
    method, but over-design can increase the cost and sometimes make the method unfeasible.
    An ODC can be modeled as a resistor in series with a capacitor. The series resistor and the
    series capacitor are respectively called Rdie and Cdie.
    From the die perspective, in the frequency range between 50MHz and 500MHz, the
    parallel Cdie and the package inductance form a resonant impedance peak on the power
    distribution network (PDN), which may cause a large IR (where R is the supply rail
    resistance and I is the current flowing through the resistance) drop so that the resonant
    frequency should be accurately calculated to evaluate the effect of the IR drop. A method of
    accurately obtaining the frequency domain (narrowband) ODC is reported in . However,
    the frequency domain ODC cannot be directly used for the time domain transient simulation
    applications, which include plotting time domain waveforms for jitter estimation, and sizing
    how much extra on-die decoupling capacitance is needed to satisfy the supply noise design
    specification which typically is less than 5% nominal supply voltage. In order to overcome
    the above difficulties, in this dissertation, an accurate conversion method is proposed for
    frequency domain narrowband to time domain wideband Rdie/Cdie and the effectiveness is
    verified with a test chip measurement.

Jitter Tracking [#SNIJMO]_
------------------------------------------------

    .. image:: ../blogstatic/PSIJ/jitter_tracking_0.png

    .. image:: ../blogstatic/PSIJ/jitter_tracking_1.png

    .. image:: ../blogstatic/PSIJ/jitter_tracking_2.png
    
System optimization specification [#TDJSA]_
------------------------------------------------------------------------
    - Advanced Computing Requirement on Memory Bandwidth fuels the requirement of High Bandwidth Memory.
    - Development of HBM may involve multiple different IP functional blocks to be integrated.
    - Top Down definition of jitter specification for each blocks is needed in order to define the total system performance.
    - A top down definition proposal was presented which captures the key element for specification definition.
    - Example of building a system level behavioral model was presented which help to evaluate system performance and trade offs.
    - The proposed method allows system designers to evaluate and more accurately predict the trade offs before the system is manufactured.





    .. [#RPSIJDDR] Reduction of Power Supply Induced Jitter with Applications to DDR Controllers. Xinjie Wang
    .. [#SNIJMO] Supply noise induced jitter modeling and optimization for high-speed interfaces
    .. [#PMSNIJ] Prediction and Measurement of Supply Noise Induced Jitter in High-Speed I/O Interfaces 
    .. [#TDJSA] Top Down Jitter Specification Approach for HBM System Optimization
