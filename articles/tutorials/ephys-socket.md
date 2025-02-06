---
uid: ephys-socket
title: Visualizing Data in the Open Ephys GUI
---

This tutorial shows how to establish a TCP connection to visualize data acquired with ONIX hardware in the Open Ephys GUI, using the OpenEphys.Sockets.Bonsai and OpenEphys.Onix1 Bonsai packages, and the Ephys Socket Open Ephys GUI plugin.

In this example, we transmit two data streams from a NeuropixelsV1e probe: the LFP band and the AP band data (384 channels). This approach lets users take advantage of the specialized visualizers available in the Open Ephys GUI, such as the Probe Viewer which was specifically designed for very dense arrays like Neuropixels probes.

Even though the Open Ephys GUI has recording functionality, when acquiring data using the Bonsai ONIX package, data should be written to file in Bonsai following the [Hardware Guides](xref:hardware). In particular, for the NeuropixelsV1e data presented in this example, follow the [NeuropixelsV1e Headstage Hardware Guide](xref:np1e).

This tutorial guides you through building the following workflow in Bonsai: 

::: workflow
![/workflows/tutorials/ephys-socket/ephys-socket.bonsai workflow](../../workflows/tutorials/ephys-socket/ephys-socket.bonsai)
:::

And the corresponding Signal Chains for visualization of the SpikeData and LFPData in the Open Ephys GUI.

![TCP Socket Probe Open Ephys GUI configuration](../../images/ephys-socket-tut/ephys_socket_gui_signalchain_working_probe_viewer.png){width=650px}

![TCP Socket LFP Open Ephys GUI configuration](../../images/ephys-socket-tut/ephys_socket_gui_signalchain_working_lfp_viewer.png){width=650px}

<!-- This method is generalizable to any continuous data stream in the correct matrix format -->

> [!NOTE]
> This tutorial uses NeuropixelsV1e Headstage as an example, but the process is similar for other ephys headstages. This
> tutorial assumes you are familiar with the [hardware guide](xref:hardware) of the ONIX headstage you intend to use.
> Use the information on the <xref:dataio> reference page to know which shift and scaling you need to use for each device on other headstages.

## Get Started in Bonsai and the Open Ephys GUI

1. Follow the [Getting Started](xref:getting-started) guide to set up and get familiarized with Bonsai. In particular:

- [Download the necessary Bonsai packages](xref:install-configure-bonsai#install-packages-in-bonsai) or 
[check for updates](xref:install-configure-bonsai#update-packages-in-bonsai) if they're already installed. This tutorial assumes you're using the latest packages.
- Read about [visualizing data](xref:visualize-data). We recommend verifying each step of the tutorial by visualizing the data produced.

<!-- Do we list OpenEphys.Sockets.Bonsai or assume they'll download what is included in the "necessary Bonsai packages"? -->

2. Follow the [Open Ephys GUI documentation](xref:https://open-ephys.github.io/gui-docs/) to set up and get familiarized with the Open Ephys GUI. In particular:

- Download and install the application by following the [Open Ephys GUI installation instructions](xref:https://open-ephys.github.io/gui-docs/User-Manual/Installing-the-GUI.html)
- Install the Ephys Socket plugin and the Probe Viewer plugin by using the [Plugin Installer](xref:https://open-ephys.github.io/gui-docs/User-Manual/Plugins/index.html#plugin-installer).
- Read about [Exploring the user interface](https://open-ephys.github.io/gui-docs/User-Manual/Exploring-the-user-interface.html), [Building a signal chain](https://open-ephys.github.io/gui-docs/User-Manual/Building-a-signal-chain.html) and [General plugin features](https://open-ephys.github.io/gui-docs/User-Manual/Plugins/index.html#general-plugin-features), as well as specific plugin pages such as the [Ephys Socket plugin](https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Ephys-Socket.html), [Probe Viewer plugin](https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Probe-Viewer.html) and the [LFP Viewer plugin](https://open-ephys.github.io/gui-docs/User-Manual/Plugins/LFP-Viewer.html).


## Configure the TCP Connection in Bonsai

Place one TcpServer node per datastream at the top of the workflow and set their properties:

::: workflow
![/workflows/tutorials/ephys-socket/configure-socket.bonsai workflow](../../workflows/tutorials/ephys-socket/configure-socket.bonsai)
:::

- Adress: Use "localhost" if using the Open Ephys GUI on the same PC or local network as Bonsai.
- Name: give the communication channel a unique name. We will use this name to provide the datastream to the socket within Bonsai. In this example, we have named them "socket1" and "socket2".
- Port: choose a unique port number. We will use this port number to establish the connection with the Open Ephys GUI.

> [!TIP]
> The TcpServer nodes need to be at the top of the workflow. If they end up somewhere else and you need to move them, do the following: click and hold on the node, hold down the Alt key on the keyboard, hover over a node in the workflow row over which you want to place it until an arrow appears, and let go.  


## Configure the Hardware

Construct an ONIX [top-level hardware configuration chain](xref:initialize-onicontext): 

::: workflow
![/workflows/tutorials/ephys-socket/configuration.bonsai workflow](../../workflows/tutorials/ephys-socket/configuration.bonsai)
:::

1. Place the [configuration operators](xref:configure) that correspond to the hardware you intend to use between
<xref:OpenEphys.Onix1.CreateContext> and <xref:OpenEphys.Onix1.StartAcquisition>. In this example, these are <xref:OpenEphys.Onix1.ConfigureNeuropixelsV1eHeadstage> and <xref:OpenEphys.Onix1.ConfigureBreakoutBoard>.
1. Confirm that the device that streams electrophysiology data is enabled. In this example, we will be using the device NeuropixelsV1eData.
1. Configure the hardware as necessary. In the case of NeuropixelsV1e Headstage, you must provide gain and calibration files and can perform other configurations as explained in the [NeuropixelsV1e Headstage Configuration](xref:np1e_configuration). In this example, we used an AP Gain value of 1000 and LFP Gain value of 50.

## Stream Ephys Data into Bonsai

Place the relevant operators to stream electrophysiology data from your headstage:

::: workflow
![/workflows/tutorials/ephys-socket/ephys-data.bonsai workflow](../../workflows/tutorials/ephys-socket/ephys-data.bonsai)
:::

1. Place the <xref:OpenEphys.Onix1.NeuropixelsV1eData> node into the workflow, since the device on NeuropixelsV1e Headstage that streams electrophysiology data is the Neuropixels 1.0 probe.
1. Select the relevant members from the data frames that `NeuropixelsV1eData` produces. In this example, the relevant members are "SpikeData" and "LfpData". To do this, right-click `NeuropixelsV1eData`, hover over the output option in the context menu, and select "SpikeData" from the list. Repeat for "LfpData".

Visualize the raw data to confirm that the ephys data operator is streaming data. 

## Configure the Data Streams to Transmit

Connect a `SendMatOverSocket` operator to each of the electrophysiology data streams. This operator comes from the OpenEphys.Sockets Bonsai package. Make sure it's [installed and updated](xref:install-configure-bonsai).

<!-- I'm not sure how to link to the reference as was done with other nodes <xref:Bonsai.Dsp.SelectChannels> -->

::: workflow
![/workflows/tutorials/ephys-socket/ephys-socket.bonsai workflow](../../workflows/tutorials/ephys-socket/ephys-socket.bonsai)
:::

Configure the "Connection" property of each `SendMatOverSocket` node to each of the TCP Socket names configured earlier. In this example, we used "socket1" for "SpikeData" and "socket2" for "LfPData".


## Configure the TCP Socket in the Open Ephys GUI to Stream and View Data
### Using the Ephys Socket and Probe Viewer processors for SpikeData

Drag the source processor `Ephys Socket` from the Processor list and drop it onto the Signal Chain area, followed by the sink processor `Probe Viewer`.

Configure the Scale and Offset properties of the `Ephys Socket` processor:

- Edit its "Scale" property to multiply the signal by a scalar in order to get microvolt values. This scalar is
determined by the gain of the amplifier and resolution the ADC contained in the amplifier device. In this example, we "Scale" by 1.171875 because the NeuropixelsV1e device on NeuropixelsV1e headstage has a step size of 1.2e6/1024/_gain_&nbsp;μV/bit and the AP Gain was configured at 1000.

- Edit its "Offset" property to subtract 2^bit depth - 1^ from the signal. In this example, we "Offset" 512 because the NeuropixelsV1e device outputs unsigned 10-bit data.

![TCP Socket Probe Open Ephys GUI configuration](../../images/ephys-socket-tut/ephys_socket_gui_signalchain_connect_probe_viewer.png){width=650px}

Press the "Connect" button on the `Ephys Socket` and open the visualizer by clicking the “tab” button in the upper right of the `Probe Viewer`.

![TCP Socket Probe Open Ephys GUI configuration](../../images/ephys-socket-tut/ephys_socket_gui_signalchain_working_probe_viewer.png){width=650px}

Click the play button in the Control Panel at the top of the GUI to begin data acquisition.

![TCP Socket Probe Open Ephys GUI visualizer](../../images/ephys-socket-tut/ephys_socket_probe_viewer_gui_window.png){width=650px}

### Using the Ephys Socket and LFP Viewer processors for LfpData

Drag the source processor `Ephys Socket` from the Processor list and drop it onto the Signal Chain area, followed by the sink processor `Probe Viewer`.

Configure the Scale and Offset properties of the `Ephys Socket` processor:

- Edit its "Scale" property to multiply the signal by a scalar in order to get microvolt values. This scalar is
determined by the gain of the amplifier and resolution the ADC contained in the amplifier device. In this example, we "Scale" by 23.4375 because the NeuropixelsV1e device on NeuropixelsV1e headstage has a step size of 1.2e6/1024/_gain_&nbsp;μV/bit and the LFP Gain was configured at 50.

- Edit its "Offset" property to subtract 2^bit depth - 1^ from the signal. In this example, we "Offset" 512 because the NeuropixelsV1e device outputs unsigned 10-bit data.

![TCP Socket LFP Open Ephys GUI configuration](../../images/ephys-socket-tut/ephys_socket_gui_signalchain_connect_lfp_viewer.png){width=650px}

Press the "Connect" button on the `Ephys Socket` and open the visualizer by clicking the “tab” button in the upper right of the `LFP Viewer`.

![TCP Socket LFP Open Ephys GUI configuration](../../images/ephys-socket-tut/ephys_socket_gui_signalchain_working_lfp_viewer.png){width=650px}

Click the play button in the Control Panel at the top of the GUI to begin data acquisition.

![TCP Socket LFP Open Ephys GUI visualizer](../../images/ephys-socket-tut/ephys_socket_lfp_viewer_gui_window.png){width=650px}

> [!TIP]
> You can read more about using each specific plugin in the [Plugins section of the Open Ephys GUI documentation](xref:https://open-ephys.github.io/gui-docs/User-Manual/Plugins/index.html) 

## Stream Ephys Data in Bonsai and Visualize it in the Open Ephys GUI

Here is a video showing how this works:

<video controls>
  <source src="../../images/ephys-socket.mp4" type="video/mp4">
</video> 


<!-- add troubleshooting -->