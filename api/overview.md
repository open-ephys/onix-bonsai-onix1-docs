---
uid: OpenEphys.Onix1
title: OpenEphys.Onix1
---

> [!TIP]
> Quickly access these pages in Bonsai by pressing <kbd>F1</kbd> while an OpenEphys.Onix1 operator
> is selected in the workflow or Toolbox. 

OpenEphys.Onix1 is a Bonsai package for control of and data acquisition from 
ONIX hardware. This section of the docs is dedicated to facilitate construction 
of workflows using OpenEphys.Onix1. It contains helpful information about 
OpenEphys.Onix1 operators and the data elements they produce. The 
<xref:OpenEphys.Onix1.Rhs2116DataFrame> page exemplifies this. It contains 
information to interpret data such as equations for converting electrophysiology 
signals from the raw ADC values to volts. 

## Property Categories

### Configuration properties vs Acquisition properties

In the OpenEphys.Onix1 package, properties belong to specific categories that
define when the property effects the hardware. 

<span class="badge oe-badge-border oe-badge-yellow"
id="configuration">Configuration</span> properties have an effect on hardware
when a workflow is started and are used to initialize the hardware state. If
they are changed while a workflow is running, they will not have an effect until
the workflow is restarted. For example, CreateContext's
<xref:OpenEphys.Onix1.CreateContext.Index> Configuration property is used to 
specify the hardware prior to starting a recording, and editing this property 
has no effect until the workflow is started or restarted.

<span class="badge oe-badge-border oe-badge-blue"
id="acquisition">Acquisition</span> properties have an immediate effect on
hardware when the workflow is running. For example, 
Headstage64ElectricalStimulatorTrigger's 
<xref:OpenEphys.Onix1.Headstage64ElectricalStimulatorTrigger.InterPulseInterval>
property allows dynamically configuring the duration between electrical 
stimulation pulses. Along with its other Acquisition properties, the entire
electrical stimulation pattern can be modulated in real-time while the workflow
is running.

### Device Group properties vs Device properties

Properties are additionally categorized by whether they effect a group of devices
or a single device.

<span class="badge oe-badge-border oe-badge-green" id="device-group">Device
Group</span> properties are only available through [Device Group configuration
operators](xref:configure). These properties are used to configure a group of
devices. For example, ConfigureNeuropixelsV2eHeadstage's 
<xref:OpenEphys.Onix1.ConfigureNeuropixelsV2eHeadstage.Port> property 
configures the port name for all devices on the NeuropixelsV2e Headstage (which
in turn automatically configures each device's address). 

<span class="badge oe-badge-border oe-badge-purple" id="device">Device</span>
properties are available through [Device configuration
operators](xref:device-configure) and Device Group configuration operators which
typically combine multiple individual devices. These properties are used to 
configure a single device. For example, ConfigureBreakoutBoard's 
<xref:OpenEphys.Onix1.ConfigureBreakoutBoard.AnalogIO> properties configure the
Breakout Board's Analog I/O device.
