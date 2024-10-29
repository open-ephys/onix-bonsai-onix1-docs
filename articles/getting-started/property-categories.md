---
uid: property-categories
title: Property Categories
---

There are specific categories of properties that define when an operator's properties can be modified. 

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