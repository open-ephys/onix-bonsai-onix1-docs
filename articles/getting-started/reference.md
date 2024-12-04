---
uid: reference
title: Software Reference
---

The following table provides information about which operators correspond to which hardware and the "Shift" and "Scale"
values to convert the ADC value to μV. "Shift" refers to the value required to subtract from unsigned data to center its
dynamic range around zero. The "Shift" value is typically $2^{(bit depth - 1)}$. "Scale" refers to the scalar required to
multiply to your data to convert it from units of DAC step size to μV.

| Hardware                         | Configuration Operator                                      | Analog Input Device                                                                                                    | Ephys Data Operator                           | Data Frame                                         | Shift  | Scale              |
|----------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------|--------|--------------------|
| Headstage64                      | <xref:OpenEphys.Onix1.ConfigureHeadstage64>                 | [Intan Rhd2164 (amplifier & auxiliary)](https://intantech.com/files/Intan_RHD2164_datasheet.pdf)                       | <xref:OpenEphys.Onix1.Rhd2164Data>            | <xref:OpenEphys.Onix1.Rhd2164DataFrame>            | -32768 | 0.195              |
| HeadstageRhs2116                 | <xref:OpenEphys.Onix1.ConfigureHeadstageRhs2116>            | [Intan Rhs2116](https://intantech.com/files/Intan_RHS2116_datasheet.pdf)                                               | <xref:OpenEphys.Onix1.Rhs2116Data>            | <xref:OpenEphys.Onix1.Rhs2116DataFrame>            | -32768 | 0.195              |
| NeuropixelsV1e<wbr>Headstage     | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV1eHeadstage>     | [Neuropixels 1.0 probe (AP & LFP)](https://www.neuropixels.org/_files/ugd/328966_c5e4d31e8a974962b5eb8ec975408c9f.pdf) | <xref:OpenEphys.Onix1.NeuropixelsV1eData>     | <xref:OpenEphys.Onix1.NeuropixelsV1DataFrame>      | -512   | $1.2e6/1024/gain$* |
| NeuropixelsV2e<wbr>Headstage     | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV2eHeadstage>     | [Neuropixels 2.0 probe](https://www.neuropixels.org/_files/ugd/328966_2b39661f072d405b8d284c3c73588bc6.pdf)            | <xref:OpenEphys.Onix1.NeuropixelsV2eData>     | <xref:OpenEphys.Onix1.NeuropixelsV2eDataFrame>     | -2048  | 3.05176            |
<!-- | NeuropixelsV2eBeta<wbr>Headstage | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV2eBetaHeadstage> | Neuropixels 2.0 Beta probe                                                                                             | <xref:OpenEphys.Onix1.NeuropixelsV2eBetaData> | <xref:OpenEphys.Onix1.NeuropixelsV2eBetaDataFrame> | -8192  | 0.7629             |
| BreakoutBoard                    | <xref:OpenEphys.Onix1.ConfigureBreakoutBoard>               | [Breakout Board Analog Input]() in                                                                                       | <xref:OpenEphys.Onix1.AnalogInput>            | <xref:OpenEphys.Onix1.AnalogInputDataFrame>        | -8192  | 0.7629             | -->

\* The Neuropixels 1.0 probes have selectable gain which has an effect on the multiplier for scaling the signal to μV,
so the $1.2e6/1024/gain$ formula must be used to calculate the correct "Scale" value. The Gain is set by the user in the
[Configuration GUI](xref:np1e_gui) of that headstage.

