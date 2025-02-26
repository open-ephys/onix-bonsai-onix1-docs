---
uid: configure
title: Device Group Configuration Operators
---

Device Group configuration operators belong in a top-level configuration chain between
[CreateContext](xref:OpenEphys.Onix1.CreateContext) and
[StartAcquisition](xref:OpenEphys.Onix1.StartAcquisition) to configure ONIX hardware. These are
known as Device Group configuration operators because they configure a group of devices on a given
headstage, miniscope, breakout board, etc. [!INCLUDE [device description](<./../includes/device-description.md>)]

Device Group configuration operators are simply referred to as "Configuration Operators" in the
[Reference](xref:OpenEphys.Onix1) table of contents for concision and simplicity as they are
the recommended starting-point operators for configuring Open Ephys ONIX hardware. There are also
<xref:device-configure>. 