---
uid: property-categories
title: Property Categories
---

Operators can be configured through editable properties. These properties fall
into the following categories:

<span class="badge oe-badge-border oe-badge-orange"
id="configuration">Configuration</span> properties have an effect on hardware
when a workflow is started and are used to initialize the hardware state. If
they are changed while a workflow is running, they will not have an effect until
the workflow is restarted. For example, the `Driver` and `Index` properties of
<xref:OpenEphys.Onix1.CreateContext#properties> are used to specify the hardware
prior to starting a recording.

<span class="badge oe-badge-border oe-badge-blue"
id="acquisition">Acquisition</span> properties have an immediate effect on
hardware when the workflow is running. For example, the stimulus properties of
<xref:OpenEphys.Onix1.Headstage64ElectricalStimulatorTrigger#properties> can be 
dynamically configured while a workflow is running to shape stimulus patterns in 
real-time.

<span class="badge oe-badge-border oe-badge-green" id="multi-device">Multi-device</span> properties
are only available through [multi-device configuration operators](xref:configure). They are used to
configure a collection of devices contained by a single piece of hardware such as a headstage,
miniscope, or breakout board. For example, the 
[BreakoutBoard](xref:OpenEphys.Onix1.ConfigureBreakoutBoard#breakoutboard) property can be used to
provide unique names to different Breakout boards and their devices if multiple are used on a single
host computer.

<span class="badge oe-badge-border oe-badge-purple" id="single-device">Single-device</span>
properties are available through [single-device configuration
operators](xref:device-configure) and multi-device configuration operators which
combine multiple individual devices. They are used to configure a single device. 
For example, the <xref:OpenEphys.Onix1.ConfigureBreakoutBoard.AnalogIO#analogio> 
property can be used to configure the Analog IO device on a breakout board.

<!-- TODO: Move this to the user guide -->
<!-- Writing <span class="badge oe-badge-border oe-badge-blue" id="acquisition">Acquisition</span> <span
class="badge oe-badge-border oe-badge-purple" id="device">Device</span> properties to hardware
dynamically (e.g. while the the workflow is running) requires using single-device configuration operators
because externalizing device properties from a multi-device configuration operator in Bonsai is
currently not possible. -->

