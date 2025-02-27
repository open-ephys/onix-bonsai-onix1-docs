---
uid: device-configure
title: Device Configuration Operators
---

> [!TIP]
>  Device configuration operators are not recommended for using off-the-shelf Open Ephys hardware.
>  Use [Device Group configuration operators](xref:configure) instead. They confer the following
>  benefits:
> - The `address` and `name` properties of Device Group configuration operators undergo automatic
>   configuration which reduces the risk of erroneous configuration.
> - The workflow is less cluttered with configuration operators as one Device Group configuration
>   operator corresponds to multiple device operators. This improves workflow legibility and
>   expedites the workflow scripting process.

Device configuration operators belong in a top-level configuration chain between
[CreateContext](xref:OpenEphys.Onix1.CreateContext) and
[StartAcquisition](xref:OpenEphys.Onix1.StartAcquisition) to configure devices that can be found on
ONIX hardware. [!INCLUDE [device description](<./../includes/device-description.md>)]