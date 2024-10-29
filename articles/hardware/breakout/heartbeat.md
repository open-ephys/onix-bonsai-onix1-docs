---
uid: breakout_heartbeat
title: Breakout Board Heartbeat
hardware: true
device: heartbeat
---

The breakout board provides a heartbeat function that prevents the breakout board from blocking. It must be enabled so
that the software doesn't wait forever to receive data if the hardware isn't transmitting data (i.e. if no data sources
are enabled). In practice, you can ignore the Heartbeat functionality after confirming it's enabled. The following excerpt 
from the Breakout Board [example workflow](xref:breakout_workflow) demonstrates how to observe the heartbeat functionality.

::: workflow
![/workflows/hardware/breakout/heartbeat.bonsai workflow](../../../workflows/hardware/breakout/heartbeat.bonsai)
:::

The <xref:OpenEphys.Onix1.HeartbeatData> operator generates a sequence of
[HeartbeatDataFrames](xref:OpenEphys.Onix1.HeartbeatDataFrame). `HeartbeatData` emits `HeartbeatDataFrames` at a regular
interval defined during <xref:breakout_configuration> using the <xref:OpenEphys.Onix1.ConfigureBreakoutBoard>'s
`Heartbeat BeatsPerSecond` property (in our case 10 Hz). The `HeartbeatData`'s `DeviceName` property is set to
"BreakoutBoard/Heartbeat". This links the `HeartbeatData` operator to the corresponding configuration operator. The
[MemberSelector](https://bonsai-rx.org/docs/api/Bonsai.Expressions.MemberSelectorBuilder.html) operator selects the
`Clock` member from the `HeartbeatDataFrame` so the user can visualize the number of clock cycles that have passed for
a given heartbeat pulse if they double-click the `Clock` node. 