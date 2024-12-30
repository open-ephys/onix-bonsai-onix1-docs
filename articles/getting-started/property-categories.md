---
uid: property-categories
title: Property Categories
---

There are specific categories of properties that define when and how an operator's properties can be modified. 

## Configuration & Acquisition Properties

<span class="badge bg-warning-subtle border border-warning-subtle text-warning-emphasis rounded-pill"
id="configuration">configuration</span> properties have an effect on hardware when a workflow is started and are used to
initialize the hardware state. Even if they are changed while a workflow is running, they will not have an effect until
the workflow is restarted.

<span class="badge bg-primary-subtle border border-primary-subtle text-primary-emphasis rounded-pill"
id="acquisition">acquisition</span> properties have an immediate effect on hardware when the workflow is running. For
instance, stimulus waveform properties can be dynamically modified according to parameters in your workflow.

## Aggregate & Device Properties

<span class="badge bg-success-subtle border border-success-subtle text-success-emphasis rounded-pill"
id="aggregate">aggregate</span> properties belong to [aggregate configuration operators](xref:configure). They are
simply referred to as "Configuration Operators" in the [Reference](xref:OpenEphys.Onix1) TOC for concision and
simplicity as they are recommended default operators for configuring Open Ephys ONIX hardware.

<span class="badge bg-danger-subtle border border-danger-subtle text-danger-emphasis rounded-pill"
id="device">device</span> properties belong to [device configuration operators](xref:device-configure) though aggregate
operators can derive these properties from device operators. All properties in device configuration operators are device
properties. Aggregate operators often derive device properties from device configuration operators. For example, the
<xref:OpenEphys.Onix1.ConfigureHeadstage64> operator derives properties from the <xref:OpenEphys.Onix1.ConfigureBno055>
operator. 

## Writing Acquisition Properties to Hardware Dynamically

Writing acquisition properties to hardware dynamically (e.g. while the the workflow is running) requires using
device operators because externalizing device properties from an aggregate operator in Bonsai is currently not possible. 