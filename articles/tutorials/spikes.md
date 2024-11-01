---
uid: spikes
title: Spike Detection
---

<!-- I think this tutorial should use a file to show the actual spike data and then show how to modify it for online data -->

This tutorial is dedicated to teaching how to use ONIX hardware and the OpenEphys.Onix1 Bonsai package to detect spikes
with a simple fixed threshold as well as visualize and save raw/spike data. The following workflow is an example of
what you can expect after finishing this tutorial by the end of the tutorial. 

::: workflow
![/workflows/tutorials/spikes.bonsai workflow](../../workflows/tutorials/spikes/spikes.bonsai)
:::

> [!NOTE]
> Although this tutorial uses the headstage64 to exemplify the spike detection process, it's pretty similar for
> other hardware. This tutorial in addition to the [hardware guide](xref:hardware) for your particular
> ONIX headstage should be sufficient for you to be able to detect spikes with whatever you have your hands on.

1. [Get started](xref:getting-started) in Bonsai. In particular, 
   [download the necessary Bonsai packages](xref:install-configure-bonsai#install-packages-in-bonsai). 
   If you've already downloaded them, 
   [check for updates](xref:install-configure-bonsai#update-packages-in-bonsai). This tutorial assumes you're using the
   latest software.

1. Create the top-level configuration graph

    ::: workflow
    ![/workflows/tutorials/spikes/configuration.bonsai workflow](../../workflows/tutorials/spikes/configuration.bonsai)
    :::

    In this workflow, all devices on the breakout board and all devices on the headstage64 except the Rhd2164 are
    configured to be disabled at run-time. For the sole purpose of teaching how to detect spikes, I only need the data
    from Rhd2164 Intan amplifier and don't have to bother with all that other stuff. 
    
    If you are collecting electrophysiology data from hardware that is not the headstage64, replace the
    <xref:OpenEphys.Onix1.ConfigureHeadstage64> node with a [configuration operator](xref:configure) that corresponds to
    your hardware, and confirm the device that streams electrophysiology data on that headstage is enabled. 

1. Place the relevant operator to stream electrophysiology data from your hardware and select the
   relevant output members

    ::: workflow
    ![/workflows/tutorials/spikes/ephys-data.bonsai workflow](../../workflows/tutorials/spikes/ephys-data.bonsai)
    :::
  
    Because I am using headstage64 in this example and the headstage64 streams electrophysiology through Rhd2164 Intan
    amplifier, I place the <xref:OpenEphys.Onix1.Rhd2164Data> node onto the workflow. If you are using different
    hardware, the table at the bottom of this tutorial[^1] provides a reference for which ephys <xref:dataio> you need
    to place onto your workflow for your particular hardware and links to relevant documentation. Select the relevant
    members from the frames that are produced by the chosen ephys data operators. In this case, those members are
    "AmplifierData" and "Clock". This is most easily performed by clicking one of the members that appears after
    hovering over the output option in the context menu that appears after right-clicking the `Rhd2164` node. 

    <!-- placeholder for visual demonstrating the output member selection -->

    Let's visualize the raw data. Start the workflow by pressing <kbd>F5</kbd> or clicking the green triangle play
    button at the top of the workflow editor. Double click the selected member that is streaming ephys data. In my case,
    that's the `MemberSelector` selecting "AmplifierData".

    <!-- placeholder for visual demonstrating the output member selection -->

    <!-- Now stop the workflow -->

1. Create the data processing graph for spike detection

    ::: workflow
    ![/workflows/tutorials/spikes/spike-detection.bonsai workflow](../../workflows/tutorials/spikes/spike-detection.bonsai)
    :::

    First, select from which channels you want to detect spikes by connecting a `SelectChannels` node to your
    electrophysiology data stream and editing its "Channels" property. 
    
    Center the dynamic range of the signal around zero and scale the ADC signal to μV. Although the following
    calculation can be done in one `ConvertScale` operator, the calculations are more straightforward using two of them
    connected in series because the `ConvertScale` operator applies the "Shift" offset after applying the "Scale" scalar
    instead of the reverse order of operation. Connect the first `ConvertScale` operator to the `SelectChannels` operator. 
      - Center the dynamic range of the signal around zero by subtracting 2^bit depth - 1^ from the signal. This is done
        in your Bonsai workflow by editing the "Shift" property of the first `ConvertScale` operator. If you are unsure
        about the bit depth of the electrophysiology data from your particular hardware, refer to the table at the
        bottom of this tutorial.[^1] The headstage64's Rhd2164 device has a bit depth of 16, so I set "Shift" to 32768 to
        subtract 32768 from our data. I also set the "Depth" property to S16 so that the negative data is properly
        represented. S16 refers to a signed 16-bit data type  
      - Scale the ADC signal to μV by multiplying all values in the ADC signal by a scalar that is determined by the
        gain of the amplifier and resolution the ADC contained in the amplifier device This is done in your Bonsai
        workflow by editing the "Scale" property of the second `ConvertScale` operator. If you are unsure about the step
        size of the electrophysiology data from your particular hardware, refer to the table at the bottom of this
        tutorial.[^1] The Rhd2164 amplifier device has a step size of 0.195 μV, so I set "Scale" to 0.195 to multiply our
        data by 0.195. I also set the "Depth" property to F32 because a larger bit depth is required to correctly
        represent the scaled values. 

    Following a similar process as before for visualizing data, we can visualize the scaled data.
    <!-- placeholder for visual demonstrating the scaled data -->

    <br>
    Apply a filter to the signal. For the purpose of detecting spikes, I set a high-pass filter at 300 Hz. This is done
    in your Bonsai workflow by connecting a `FrequencyFilter` operator to the second `ConvertScale` operator and setting
    its "Cutoff1" property to 300. 

    Following a similar process as before for visualizing data, we can visualize the scaled, filtered data.
    <!-- placeholder for visual demonstrating the scaled, filtered data -->

    Last, set a simple fixed threshold for detecting spikes. <!-- discuss these details -->

    Following a similar process as before for visualizing data, we can visualize the spike data.
    <!-- placeholder for visual demonstrating the spike data -->

    > [!TIP] 
    > You can test this spike detection workflow using a pre-recorded data known to have spikes. Simply recreate the
    > data processing graph in a new workflow but replace the ephys data node (in the case of the headstage64, replace
    > the `Rhd2164` node) with a `MatrixReader` that reads from the file containing spiky ephys data.
    
<!-- > [!TIP] 
> If you choose to save data, make sure you place the `MatrixWriter` operator before filtering and scaling to save raw
> data instead of scaled or scaled, filtered data. The `FrequencyFilter` operator could remove signals from a bandwidth
> of interest and the second `ConvertScale` value increase the size of your data without increasing meaningful
> information.  -->

[^1]:

| Hardware                     | Configuration Operator                                  | Amplifier Device                                                                                            | Ephys Data Operator                       | Data Frame                                     | Shift  | Scale  |
|------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------|------------------------------------------------|--------|--------|
| Headstage64                  | <xref:OpenEphys.Onix1.ConfigureHeadstage64>             | [Intan Rhd2164](https://intantech.com/files/Intan_RHD2164_datasheet.pdf)                                    | <xref:OpenEphys.Onix1.Rhd2164Data>        | <xref:OpenEphys.Onix1.Rhd2164DataFrame>        | -32768 | 0.195  |
| HeadstageRhs2116             | <xref:OpenEphys.Onix1.ConfigureHeadstageRhs2116>        | [Intan Rhs2116](https://intantech.com/files/Intan_RHS2116_datasheet.pdf)                                    | <xref:OpenEphys.Onix1.Rhs2116Data>        | <xref:OpenEphys.Onix1.Rhs2116DataFrame>        | -32768 | 0.195  |
| NeuropixelsV1e<wbr>Headstage | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV1eHeadstage> | [Neuropixels 1.0 probe](https://www.neuropixels.org/_files/ugd/328966_c5e4d31e8a974962b5eb8ec975408c9f.pdf) | <xref:OpenEphys.Onix1.NeuropixelsV1eData> | <xref:OpenEphys.Onix1.NeuropixelsV1DataFrame>  | -512   | *      |
| NeuropixelsV2e<wbr>Headstage | <xref:OpenEphys.Onix1.ConfigureNeuropixelsV2eHeadstage> | [Neuropixels 2.0 probe](https://www.neuropixels.org/_files/ugd/328966_2b39661f072d405b8d284c3c73588bc6.pdf) | <xref:OpenEphys.Onix1.NeuropixelsV2eData> | <xref:OpenEphys.Onix1.NeuropixelsV2eDataFrame> | -2048  | 2.4414 |


\* The Neuropixels 1.0 probes have selectable gain which has an effect on the multiplier for scaling the signal to μV.
Use the following formula to calculate the correct "Scale" value: $1.2e6/1024/gain$