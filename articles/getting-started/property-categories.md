---
uid: property-categories
title: Property Categories
---

There are specific categories of properties that define when and how an operator's properties can be modified. 

## Configuration & Acquisition Properties

<span class="badge oe-badge-border oe-badge-yellow" id="configuration">configuration</span> properties have an effect on
hardware when a workflow is started and are used to initialize the hardware state. Even if they are changed while a
workflow is running, they will not have an effect until the workflow is restarted.

<span class="badge oe-badge-border oe-badge-blue" id="acquisition">acquisition</span> properties have an immediate
effect on hardware when the workflow is running. For instance, stimulus waveform properties can be dynamically modified
according to parameters in your workflow.

## Aggregate & Device Properties

<span class="badge oe-badge-border oe-badge-green" id="aggregate">aggregate</span> properties are only available through
[aggregate configuration operators](xref:configure). 

<span class="badge oe-badge-border oe-badge-red" id="device">device</span> properties are available through 
[device configuration operators](xref:device-configure) and aggregate configuration operators that derive them from
device configuration operators. For example, <xref:OpenEphys.Onix1.ConfigureHeadstage64> derives properties from
<xref:OpenEphys.Onix1.ConfigureBno055>. 

Writing acquisition device properties to hardware dynamically (e.g. while the the workflow is running) requires using
device configuration operators because externalizing device properties from an aggregate operator in Bonsai is currently not possible. 