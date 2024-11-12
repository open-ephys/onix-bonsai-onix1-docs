---
uid: spikes
title: Processing ephys data in Bonsai

---

<!-- I think this tutorial should use a file to show the actual spike data and then show how to modify it for online data -->

This tutorial shows how to use ONIX hardware and the OpenEphys.Onix1 Bonsai package to perform basic online signal
processing functions in Bonsai such as channel selection and reordering, filtering and event detection such as a fixed
threshold crossing.

This type of processing is important for real-time feedback while monitoring data being acquired. However, Bonsai's integrated visualizers and event detectors are limited, so we recommend using the tools available in the Open Ephys GUI for specialized ephys visualizations. The Open Ephys GUI is particularly suited for visualizing data from very dense arrays such as Neuropixels probes.
<!-- You can follow the Visualizing data in the Open Ephys GUI tutorial to set up your system to acquire in Bonsai and visualize in the Open Ephys GUI.  -->

More advanced event detection algorithms such as spike sorting, ripple detection, etc. need specific implementations in Bonsai. Event detection in Bonsai will be faster and it allows actuation using ONIX or other hardware for closed-loop applications. 

This tutorial will guide you through building the following workflow: 

::: workflow
![/workflows/tutorials/spikes.bonsai workflow](../../workflows/tutorials/spikes/spikes.bonsai)
:::

> [!NOTE]
> Although this tutorial uses headstage64 as an example, the process is similar for other ephys headstages. This
> tutorial assumes you are familiar with the [hardware guide](xref:hardware) of the ONIX headstage you intend to use.
> Use the table at the bottom of this tutorial[^1] as a reference for which ephys <xref:dataio> you need and scaling
> corresponds to each headstage and links to relevant documentation. 

## Set up and get to know Bonsai

Follow the [Getting Started](xref:getting-started) guide to set up and get familiarized with Bonsai. In particular:

- [Download the necessary Bonsai packages](xref:install-configure-bonsai#install-packages-in-bonsai) or 
[check for updates](xref:install-configure-bonsai#update-packages-in-bonsai). This tutorial assumes 
you're using the latest software.

- Read about [visualizing data](xref:visualize-data) since we recommend checking each step of the tutorial by visualizing the data produced but we don't cover it here.

## Configure the hardware

::: workflow
![/workflows/tutorials/spikes/configuration.bonsai workflow](../../workflows/tutorials/spikes/configuration.bonsai)
:::

This is accomplished by constructing a [top-level configuration chain](xref:initialize-onicontext): place the
[configuration operator](xref:configure) that corresponds to the hardware you intend to use between
<xref:OpenEphys.Onix1.CreateContext> and <xref:OpenEphys.Onix1.StartAcquisition>. In our example, this is
<xref:OpenEphys.Onix1.ConfigureHeadstage64> and <xref:OpenEphys.Onix1.ConfigureBreakoutBoard>. Confirm the device
that streams electrophysiology data is enabled. The Rhd2164 device (an Intan amplifier) on the headstage64 is the
only device used in this tutorial, so you could disable other devices on the headstage and on the breakout board.

## Stream ephys data into Bonsai

::: workflow
![/workflows/tutorials/spikes/ephys-data.bonsai workflow](../../workflows/tutorials/spikes/ephys-data.bonsai)
:::

Place the relevant operator to stream electrophysiology data from your headstage and select the relevant output
members. Because the device on headstage64 that streams electrophysiology data is the Rhd2164 Intan amplifier, we
placed the <xref:OpenEphys.Onix1.Rhd2164Data> node onto the workflow. Select the relevant members from the data
frames that the data operator produces. In this example, the relevant members are "AmplifierData" and "Clock". To select those members, right-click the `Rhd2164` node, hover over the output option in the context menu, and select it from
the list.

<!-- placeholder for visual demonstrating the output member selection -->

Visualize the raw data to confirm the ephys data operator is streaming data. 

<!-- placeholder for visual demonstrating streaming data -->

<!-- Now stop the workflow -->

## Select and reorder channels

::: workflow
![/workflows/tutorials/spikes/select-convert-ephys-data.bonsai workflow](../../workflows/tutorials/spikes/select-convert-ephys-data.bonsai)
:::

Connect a <xref:Bonsai.Dsp.SelectChannels> operator to the electrophysiology data stream and edit its "Channels" property.
Remember indexing starts at 0. Use commas to separate multiple channels and brackets for ranges.
Reorder channels by writing the channel numbers in the order in which you want to visualize the channels.

## Convert data to physical units

::: workflow
![/workflows/tutorials/spikes/select-convert-ephys-data.bonsai workflow](../../workflows/tutorials/spikes/select-convert-ephys-data.bonsai)
:::

1. Center the dynamic range of the ADC signal around zero

    Connect a <xref:Bonsai.Dsp.ConvertScale> operator to the `SelectChannels` operator and set its properties:
    - Edit its "Shift" property to subtract 2^bit depth - 1^ from the signal. Refer to the table at the bottom of
    this tutorial to find the Shift necessary for each device.[^1] In this example, we "Shift" -32768 because the 
    Rhd2164 device outputs 16-bit data.
    - Set the "Depth" property to F32 because this bit depth is required to correctly represent scaled data from all
    devices.

1. Scale the ADC signal to microvolts.

    Connect a second `ConvertScale` operator to the first `ConvertScale` operator and set its properties:
    - Edit its "Scale" property to multiply the signal by a scalar in order to get microvolt values. This scalar is
    determined by the gain of the amplifier and resolution the ADC contained in the amplifier device. Refer to the
    table at the bottom of this tutorial to find the "Scale" necessary for each device.[^1] In this example, we
    "Scale" by 0.195 because the Rhd2164 device on headstage64 has a step size of 0.195 μV/bit
    - Keep the "Depth" property at F32.

Visualize the transformed data to confirm the output of the shifting and scaling operations
comport with expectations.

> [!NOTE]
> Although both the Shift and Scale calculation can be done in one `ConvertScale` operator, the calculations are
> more straightforward using two operators connected in series because the `ConvertScale` operator applies the
> "Shift" offset after applying the "Scale" scalar so if we used a single operator, we would have to scale the Shift
> parameter.

<!-- placeholder for visual demonstrating the scaled data -->

## Apply a frequency filter

::: workflow
![/workflows/tutorials/spikes/filter-ephys-data.bonsai workflow](../../workflows/tutorials/spikes/filter-ephys-data.bonsai)
:::

Connect a `FrequencyFilter` operator to the second `ConvertScale` operator and set its properties.
- Set its "SampleRate" property to 30000. Ephys data in all devices is 30 kHz.
- Set the "FilterType" property to an adequate type. In this example, we use a high pass filter to look at spikes.
- Set the "Cutoff1" and "Cutoff2" properties to an adequate value. In this examples, we use 300 Hz as the
    lower cutoff frequency. 

<!-- placeholder for visual demonstrating the scaled, filtered data -->

> [!TIP] 
> If you choose to save data, make sure you place the `MatrixWriter` operator before filtering and scaling to save raw
> data instead of scaled or scaled, filtered data. The `FrequencyFilter` operator could remove signals from a bandwidth
> of interest and the second `ConvertScale` value increase the size of your data without increasing meaningful
> information.

## Detect events

::: workflow
![/workflows/tutorials/spikes/spikes.bonsai workflow](../../workflows/tutorials/spikes/spikes.bonsai)
:::

Based on the amplitude of the signal on the selected channel, set a fixed threshold for detecting spikes. <!-- discuss these details -->

Visualize the spike data.

<!-- placeholder for visual demonstrating the spike data -->

> [!TIP] 
> You can test this spike detection workflow using a pre-recorded data known to have spikes. Simply recreate the
> data processing graph in a new workflow and replace the ephys data node (in the case of the headstage64, replace
> the `Rhd2164` node) with a `MatrixReader` that reads from the file containing spiking ephys data.


[^1]:

| Hardware                     | Configuration Operator                                  | Ephys Device                                                                                                            | Ephys Data Operator                       | Data Frame                                     | Shift  | Scale                  |
|------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|------------------------------------------------|--------|------------------------|
| Headstage64                  | <xref:OpenEphys.Onix1.ConfigureHeadstage64>             | [Intan Rhd2164 (amplifier channels)](https://intantech.com/files/Intan_RHD2164_datasheet.pdf)                           | <xref:OpenEphys.Onix1.Rhd2164Data>        | <xref:OpenEphys.Onix1.Rhd2164DataFrame>        | -32768 | 0.195                  |
| HeadstageRhs2116             | <xref:OpenEphys.Onix1.ConfigureHeadstageRhs2116>        | [Intan Rhs2116](https://intantech.com/files/Intan_RHS2116_datasheet.pdf)                                                | <xref:OpenEphys.Onix1.Rhs2116Data>        | <xref:OpenEphys.Onix1.Rhs2116DataFrame>        | -32768 | 0.195                  |
| NeuropixelsV1e<wbr>Headstage | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV1eHeadstage> | [Neuropixels 1.0 probe (AP)](https://www.neuropixels.org/_files/ugd/328966_c5e4d31e8a974962b5eb8ec975408c9f.pdf)        | <xref:OpenEphys.Onix1.NeuropixelsV1eData> | <xref:OpenEphys.Onix1.NeuropixelsV1DataFrame>  | -512   | $1.2e6/1024/gain$*     |
| NeuropixelsV2e<wbr>Headstage | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV2eHeadstage> | [Neuropixels 2.0 probe](https://www.neuropixels.org/_files/ugd/328966_2b39661f072d405b8d284c3c73588bc6.pdf)             | <xref:OpenEphys.Onix1.NeuropixelsV2eData> | <xref:OpenEphys.Onix1.NeuropixelsV2eDataFrame> | -2048  | 2.4414                 |


\* The Neuropixels 1.0 probes have selectable gain which has an effect on the multiplier for scaling the signal to μV, so the $1.2e6/1024/gain$ formula must be used to calculate the correct "Scale" value. The Gain is set by the user in the [Configuration GUI](xref:np1e_gui) of that headstage.