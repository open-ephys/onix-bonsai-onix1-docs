---
uid: np1e_load-data
title: Load NeuropixelsV1e Headstage Data
---

The following python script can be used to load and plot the data produced by the NeuropixelsV1e Headstage [example workflow](xref:breakout_workflow).

[!code-python[](../../../workflows/hardware/np1e/load-np1e.py)]

> [!NOTE]
> This script will attempt to load entire files into arrays. For long recordings, data will need to
> be split into more manageable chunks by:
> - Modifying this script to partially load files
> - Modifying the workflow to cyclically create new files after a certain duration
