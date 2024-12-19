---
uid: ephys-socket
title: Visualizing Data in the Open Ephys GUI
---

This tutorial shows how to establish a TCP socket to visualize data acquired with ONIX hardware in the Open Ephys GUI, using the OpenEphys.Sockets.Bonsai and OpenEphys.Onix1 Bonsai packages, and the Ephys Socket Open Ephys GUI plugin.

In this example, we transmit two data streams from a NeuropixelsV1e probe: 384 channels of the LFP band and the AP band. This approach lets users take advantage of the specialized visualizers available in the Open Ephys GUI, such as the Probe Viewer which was specifically designed for very dense arrays like Neuropixels probes.

Even though the Open Ephys GUI has recording functionality, when acquiring data using the Bonsai ONIX package, data should be written to file in Bonsai, following the [Hardware Guides](xref:hardware). In particular, for the NeuropixelsV1e presented in this example, follow the [NeuropixelsV1e Headstage Hardware Guide](xref:np1e).

This tutorial guides you through building the following workflow: 

::: workflow
![/workflows/tutorials/basic-ephys-processing/spikes.bonsai workflow](../../workflows/tutorials/basic-ephys-processing/spikes.bonsai)
:::

<!-- This method is generalizable to any continuous data stream in the correct matrix format -->

> [!NOTE]
> Although this tutorial uses NeuropixelsV1e Headstage as an example, the process is similar for other ephys headstages. This
> tutorial assumes you are familiar with the [hardware guide](xref:hardware) of the ONIX headstage you intend to use.
> Use this [reference](xref:reference) for which ephys <xref:dataio> and scaling you need to use for each headstage, and links to relevant
> documentation. 

## Set up and get started in Bonsai and the Open Ephys GUI

Follow the [Getting Started](xref:getting-started) guide to set up and get familiarized with Bonsai. In particular:

- [Download the necessary Bonsai packages](xref:install-configure-bonsai#install-packages-in-bonsai) or 
[check for updates](xref:install-configure-bonsai#update-packages-in-bonsai). This tutorial assumes 
you're using the latest software.

<!-- Make sure they install OpenEphys.Sockets.Bonsai, or is this going to be included in the "necessary Bonsai packages"? -->

<!-- Open Ephys GUI instructions -->

## Configure the TCP socket in Bonsai

<!-- add txt -->
<!-- Tip about Use Alt and drag if not at the top -->

## Configure the hardware

<!-- change ref -->
::: workflow
![/workflows/tutorials/basic-ephys-processing/configuration.bonsai workflow](../../workflows/tutorials/basic-ephys-processing/configuration.bonsai)
:::

Construct a [top-level hardware configuration chain](xref:initialize-onicontext): 

<!-- change txt -->
1. Place the [configuration operators](xref:configure) that correspond to the hardware you intend to use between
<xref:OpenEphys.Onix1.CreateContext> and <xref:OpenEphys.Onix1.StartAcquisition>. In this example, these are
<xref:OpenEphys.Onix1.ConfigureHeadstage64> and <xref:OpenEphys.Onix1.ConfigureBreakoutBoard>.
1. Confirm that the device that streams electrophysiology data is enabled. The Rhd2164 device (an Intan amplifier) on
the headstage64 is the only device used in this tutorial, so you could disable other devices on the headstage and on the
breakout board to improve performance if you wanted to.

## Stream ephys data into Bonsai

<!-- change ref -->
::: workflow
![/workflows/tutorials/basic-ephys-processing/ephys-data.bonsai workflow](../../workflows/tutorials/basic-ephys-processing/ephys-data.bonsai)
:::

<!-- change txt -->
Place the relevant operators to stream electrophysiology data from your headstage:

1. Because the device on headstage64 that streams electrophysiology data is the Rhd2164 Intan amplifier, we placed the
<xref:OpenEphys.Onix1.Rhd2164Data> node onto the workflow. Use this [reference](xref:reference) to find the ephys data operator
that corresponds to each device.
1. Select the relevant members from the data frames that the data operator produces. In this example, the relevant members are "AmplifierData" and "Clock". To select those members, right-click the `Rhd2164` node, hover over the output option in the context menu, and select it from
the list.
1. Visualize the raw data to confirm that the ephys data operator is streaming data. 

## Configure data streams to transmit

<!-- change ref -->
::: workflow
![/workflows/tutorials/basic-ephys-processing/select-convert-ephys-data.bonsai workflow](../../workflows/tutorials/basic-ephys-processing/select-convert-ephys-data.bonsai)
:::

<!-- change txt -->
Connect a <xref:Bonsai.Dsp.SelectChannels> operator to the electrophysiology data stream and edit its "" property.

## Configure the TCP socket in the Open Ephys GUI

<!-- add pics -->

## Configure the visualizers in the Open Ephys GUI

<!-- add pics -->

## Stream ephys data in Bonsai and visualize in the Open Ephys GUI

<!-- add video -->
<!-- add troubleshooting -->