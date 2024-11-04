---
uid: ucla-miniscope-v4_memory-monitor
title: UCLA Miniscope v4 Memory Monitor
---

The following excerpt from the UCLA Miniscope v4 [example workflow](xref:ucla-miniscope-v4) demonstrates memory monitor functionality and saves memory monitor data.

::: workflow
![/workflows/hardware/ucla-miniscope-v4/memory-monitor.bonsai workflow](../../../workflows/hardware/ucla-miniscope-v4/memory-monitor.bonsai)
:::

The <xref:OpenEphys.Onix1.MemoryMonitorData> operator generates a sequence of
<xref:OpenEphys.Onix1.MemoryMonitorDataFrame>s. `MemoryMonitorData` emits `MemoryMonitorDataFrame`s at a regular
interval defined during <xref:ucla-miniscope-v4_configuration> using the
<xref:OpenEphys.Onix1.ConfigureUclaMiniscopeV4>'s `MemoryMonitor SamplesPerSecond` property (in our case 10 Hz). In the
UCLA Miniscope v4 example workflow, the `MemoryMonitorData`'s `DeviceName` property is set to
"BreakoutBoard/MemoryMonitor". This links the `MemoryMonitorData` operator to the corresponding configuration operator.
The [CsvWriter](https://bonsai-rx.org/docs/api/Bonsai.IO.CsvWriter.html) operator saves the `Clock`, `BytesUsed`, and
`PercentUsed` members to a file with the following format: `memory-use_<timestamp>.csv`. Because `CsvWriter` is a _sink_
operator, its output sequence is equivalent to its input sequence. In other words, its output is equivalent to
`MemoryMonitorData`'s output. Therefore, it's possible to use a
[MemberSelector](https://bonsai-rx.org/docs/api/Bonsai.Expressions.MemberSelectorBuilder.html) operator on the
`CsvWriter` to select members from the `MemoryMonitorDataFrame`. The `MemberSelector` operator selects the `PercentUsed`
member from the `MemoryMonitorDataFrame` so the user can visualize `PercentUsed` data from the `MemoryMonitorDataFrame`.

> [!NOTE]
> The `MemoryMonitorDataFrame` operator generates a
> data stream that is most useful in the context of closed-loop performance. It tells the user if data
> is being consumed rapidly enough by the host PC to keep up with data production by the hardware. The
> hardware FIFO is a buffer that is required to deal with the fact that computers with normal
> operating systems cannot perform operations with strict regularity. When there are hiccups in
> acquisition, the hardware FIFO picks up the slack, but should then be cleared immediately. To get
> the lowest latencies, the `BlockReadSize` should be as small as possible *while the memory use
> percentage remains around 0%*.

> [!WARNING]
> If the hardware FIFO's `PercentUsed` is non-zero for long time periods, or is increasing, the
> `StartAcquisition`'s `BlockReadSize` setting is too small (see the [UCLA Miniscope v4 configuration](xref:ucla-miniscope-v4_configuration)). A small
> `BlockReadSize` will mean that the host computer does not have to wait long for enough data to
> become available to propagate it forward, but will reduce overall bandwidth by increasing the
> frequency at which the host computer checks if data is available and performs hardware reads.