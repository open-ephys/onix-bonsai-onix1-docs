---
uid: rhs2116_load-data
title: Load Data
---

A script for loading data from the NeuropixelsV2e Headstage [example workflow](xref:hs64) is
available [here](https://colab.research.google.com/drive/1EJ6JQaxGRFmvjMstfisS-GyaTujPv-qg?usp=sharing) 
as a Google Colab.

> [!NOTE]
> This script will attempt to load entire files into arrays. For long recordings, data will need to
> be split into more manageable chunks by:
> - Modifying this script to partially load files
> - Modifying the workflow to cyclically create new files after a certain duration
