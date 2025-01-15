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
<xref:OpenEphys.Onix1.Headstage64ElectricalStimulatorTrigger#properties> can be dynamically
configured while a workflow is running to shape stimulus patterns in real-time.

<span class="badge oe-badge-border oe-badge-green" id="device-group">Device
Group</span> properties are only available through [Device Group configuration
operators](xref:configure) that are used for globally configuring groups of
devices. For example,
<xref:OpenEphys.Onix1.ConfigureBreakoutBoard.BreakoutBoard#breakoutboard> property can be used
to provide a unique name to different Breakout boards if multiple are used on a
single host computer.

<span class="badge oe-badge-border oe-badge-red" id="device">Device</span>
properties are available through [Device configuration
operators](xref:device-configure) and device group configuration operators that
combine multiple individual devices. For example, the
<xref:OpenEphys.Onix1.ConfigureBreakoutBoard.AnalogIO#analogio> property can be used to
configure the Analog IO device on a breakout board.

<!-- TODO: Move this to the user guide -->
<!-- Writing <span class="badge oe-badge-border oe-badge-blue" id="acquisition">Acquisition</span> <span
class="badge oe-badge-border oe-badge-red" id="device">Device</span> properties to hardware
dynamically (e.g. while the the workflow is running) requires using device configuration operators
because externalizing device properties from a device group configuration operator in Bonsai is
currently not possible. -->

