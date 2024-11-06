---
uid: configure
title: Configuration Operators
---

Aggregate configuration operators belong in a top-level chain of operators between
[`CreateContext`](xref:OpenEphys.Onix1.CreateContext) and [`StartAcquisition`](xref:OpenEphys.Onix1.StartAcquisition) to
configure ONIX hardware hubs. These are known as aggregate configuration operators because they configure an aggregation
of devices (also referred to as a hub) on a given headstage, miniscope, breakout board, etc..