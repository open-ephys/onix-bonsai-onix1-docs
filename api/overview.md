---
uid: OpenEphys.Onix1
title: OpenEphys.Onix1
---

> [!TIP]
> Quickly access these pages in Bonsai by pressing <kbd>F1</kbd> while an OpenEphys.Onix1 operator
> is selected in the workflow or Toolbox. 

OpenEphys.Onix1 is a Bonsai package for control of and data acquisition from ONIX hardware. This
section of the docs is dedicated to facilitate construction of workflows using OpenEphys.Onix1. It
contains helpful information about OpenEphys.Onix1 operators and the data elements they produce.
such as in-depth descriptions of their properties and their data types. The data elements produced
by OpenEphys.Onix1 operators where you can find information such as equations for converting
electrophysiology signals from the DAC step-size to volts. Take the
<xref:OpenEphys.Onix1.Rhs2116DataFrame> for example.

## Property Categories

In the OpenEphys.Onix1 package, properties belong to specific categories that define when the
property effects the hardware. 

<span class="badge bg-warning-subtle border border-warning-subtle text-warning-emphasis rounded-pill"
id="configuration">configuration</span> properties have an effect on hardware when a workflow is started and are used to
initialize the hardware state. Even if they are changed while a workflow is running, they will not have an effect until
the workflow is restarted.

<span class="badge bg-primary-subtle border border-primary-subtle text-primary-emphasis rounded-pill"
id="acquisition">acquisition</span> properties have an immediate effect on hardware when the workflow is running. For
instance, stimulus waveform properties can be dynamically modified according to parameters in your workflow.

`Devices` properties refer to the individual devices available within a particular aggregate operator. Aggregate
operators include <xref:OpenEphys.Onix1.ConfigureHeadstage64>, <xref:OpenEphys.Onix1.ConfigureBreakoutBoard>, and more.
Explore other available options under the [aggregate configuration operators](xref:configure) page.