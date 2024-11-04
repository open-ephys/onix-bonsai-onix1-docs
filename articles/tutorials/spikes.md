---
uid: spikes
title: Working with ephys data in Bonsai

---

<!-- I think this tutorial should use a file to show the actual spike data and then show how to modify it for online data -->

This tutorial shows  how to use ONIX hardware and the OpenEphys.Onix1 Bonsai package to perform basic online signal processing
functions such as channel selection, filtering, visualization and a simple spike detection with using a fixed threshold.
It will guide you through building the following workflow. 

::: workflow
![/workflows/tutorials/spikes.bonsai workflow](../../workflows/tutorials/spikes/spikes.bonsai)
:::

> [!NOTE]
> Although this tutorial uses headstage64, the process is similar for
> other ephys headstages. This tutorial assumes you are familiar with the [hardware guide](xref:hardware) of the 
> ONIX headstage you intend to use. Use the table at the bottom of this tutorial[^1] as a reference for which ephys <xref:dataio> you need
> and scaling corresponds to each headstage and links to relevant documentation. 

1. [Get started](xref:getting-started) in Bonsai. In particular, 
   [download the necessary Bonsai packages](xref:install-configure-bonsai#install-packages-in-bonsai) or 
   [check for updates](xref:install-configure-bonsai#update-packages-in-bonsai) to make sure you have the latest version. This tutorial assumes you're using the
   latest software.

1. Create the top-level configuration graph
    
    ::: workflow
    ![/workflows/tutorials/spikes/configuration.bonsai workflow](../../workflows/tutorials/spikes/configuration.bonsai)
    :::

    11. Place the [configuration operator](xref:configure) that corresponds to
    the headstage you intend to use. In our example, this is <xref:OpenEphys.Onix1.ConfigureHeadstage64>.

    11. Make sure the device that streams electrophysiology data is enabled. We will only be using the Rhd2164 device on headstage64 (the Intan amplifier), so you could disable other devices on the headstage or on the breakout board.
    
1. Place the relevant operator to stream electrophysiology data from your headstage and select the relevant output members.

    ::: workflow
    ![/workflows/tutorials/spikes/ephys-data.bonsai workflow](../../workflows/tutorials/spikes/ephys-data.bonsai)
    :::
  
    11. The device on headstage64 that streams electrophysiology data is the Rhd2164 Intan
    amplifier, so we need to place the <xref:OpenEphys.Onix1.Rhd2164Data> node onto the workflow.
    
    11. Select the relevant members from the data frames that the data operator produces. In this example, the relevant members are
    "AmplifierData" and "Clock". To do this, right-click the `Rhd2164` node, hover over the output option in the context menu and select one of the members from the list.

    <!-- placeholder for visual demonstrating the output member selection -->

1. Check that you can stream data by visualizing it. 

    11. Start the workflow by clicking the green triangle play
    button at the top of the workflow editor or pressing <kbd>F5</kbd>.
    
    11. Double click the selected member that is streaming ephys data. In this example,
    that's the `MemberSelector` that selects "AmplifierData".

    For ease of visualization, click on the visualizer and configure it:
    - Increase the History length to 100
    - 

    <!-- placeholder for visual demonstrating the output member selection -->

    <!-- Now stop the workflow -->

1. Create the data processing graph for processing the ephys data.

    ::: workflow
    ![/workflows/tutorials/spikes/spike-detection.bonsai workflow](../../workflows/tutorials/spikes/spike-detection.bonsai)
    :::

    11. Select and reorder channels of interest.
    
    Connect a `SelectChannels` node to the electrophysiology data stream and edit its "Channels" property.
    Remember indexing starts at 0. Use commas to separate multiple channels and brackets for ranges.
    Reorder channels by writing the channel numbers in the order in which you want to visualize the channels.
    
    11. Center the dynamic range of the signal around zero
    
    Connect a `ConvertScale` operator to the `SelectChannels` operator.
    - Edit its "Shift" property to subtract 2^bit depth - 1^ from the signal. Refer to the table at the bottom of this tutorial to find the Shift necessary for each device.[^1]
    In this example, the Rhd2164 device on headstage64 has a bit depth of 16, so "Shift" has to be set to 32768 to subtract 32768 from the raw data.
    - Set the "Depth" property to F32 because this bit depth is required to correctly represent scaled data from all devices.

    11. Scale the ADC signal to microvolts.
    
    Connect a second `ConvertScale` operator to the `ConvertScale` operator that is already on the workflow.
    - Edit its "Scale" property to multiply the signal by a scalar in order to get microvolt values. This scalar is determined by the gain of the amplifier and resolution the ADC contained in the amplifier device. Refer to the table at the bottom of this tutorial to find the Scale necessary for each device.[^1]
    In this example, the Rhd2164 device on headstage64 has a step size of 0.195 μV, so "Scale" has to be set to 0.195 to multiply the centered data by 0.195.
    - Keep the "Depth" property at F32.

    > [!NOTE]
    > Although both the Shift and Scale calculation can be done in one `ConvertScale` operator, the calculations are more straightforward using two operators
    > connected in series because the `ConvertScale` operator applies the "Shift" offset after applying the "Scale" scalar so if we used a single operator,
    > we would have to scale the Shift parameter.
    
1. Visualize the centered and scaled data.

    <!-- placeholder for visual demonstrating the scaled data -->

1. Apply a frequency filter to the signal.

    Connect a `FrequencyFilter` operator to the second `ConvertScale` operator and set its properties.
    The sample rate for ephys data in all devices is 30kHz.
    For looking at spikes, set the "Cutoff1" property to 300 to apply a high-pass filter at 300 Hz. 

1. Visualize the scaled, filtered data.

    <!-- placeholder for visual demonstrating the scaled, filtered data -->

1. Detect spikes

    Based on the amplitude of the signal, set a fixed threshold for detecting spikes. <!-- discuss these details -->

1. Visualize the spike data.

    <!-- placeholder for visual demonstrating the spike data -->

    > [!TIP] 
    > You can test this spike detection workflow using a pre-recorded data known to have spikes. Simply recreate the
    > data processing graph in a new workflow and replace the ephys data node (in the case of the headstage64, replace
    > the `Rhd2164` node) with a `MatrixReader` that reads from the file containing spiking ephys data.
    
<!-- > [!TIP] 
> If you choose to save data, make sure you place the `MatrixWriter` operator before filtering and scaling to save raw
> data instead of scaled or scaled, filtered data. The `FrequencyFilter` operator could remove signals from a bandwidth
> of interest and the second `ConvertScale` value increase the size of your data without increasing meaningful
> information.  -->

[^1]:

| Hardware                     | Configuration Operator                                  | Amplifier Device (ephys amplifier/spike channels)                                                                       | Ephys Data Operator                       | Data Frame                                     | Shift  | Scale                  |
|------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|------------------------------------------------|--------|------------------------|
| Headstage64                  | <xref:OpenEphys.Onix1.ConfigureHeadstage64>             | [Intan Rhd2164 (amplifier channels)](https://intantech.com/files/Intan_RHD2164_datasheet.pdf)                           | <xref:OpenEphys.Onix1.Rhd2164Data>        | <xref:OpenEphys.Onix1.Rhd2164DataFrame>        | -32768 | 0.195                  |
| HeadstageRhs2116             | <xref:OpenEphys.Onix1.ConfigureHeadstageRhs2116>        | [Intan Rhs2116](https://intantech.com/files/Intan_RHS2116_datasheet.pdf)                                                | <xref:OpenEphys.Onix1.Rhs2116Data>        | <xref:OpenEphys.Onix1.Rhs2116DataFrame>        | -32768 | 0.195                  |
| NeuropixelsV1e<wbr>Headstage | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV1eHeadstage> | [Neuropixels 1.0 probe (AP band)](https://www.neuropixels.org/_files/ugd/328966_c5e4d31e8a974962b5eb8ec975408c9f.pdf)   | <xref:OpenEphys.Onix1.NeuropixelsV1eData> | <xref:OpenEphys.Onix1.NeuropixelsV1DataFrame>  | -512   | $1.2e6/1024/gain$*     |
| NeuropixelsV2e<wbr>Headstage | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV2eHeadstage> | [Neuropixels 2.0 probe](https://www.neuropixels.org/_files/ugd/328966_2b39661f072d405b8d284c3c73588bc6.pdf)             | <xref:OpenEphys.Onix1.NeuropixelsV2eData> | <xref:OpenEphys.Onix1.NeuropixelsV2eDataFrame> | -2048  | 2.4414                 |


\* The Neuropixels 1.0 probes have selectable gain which has an effect on the multiplier for scaling the signal to μV, so the $1.2e6/1024/gain$ formula must be used to calculate the correct "Scale" value. The Gain is set by the user in the [Configuration GUI](xref:np1e_gui) of that headstage.