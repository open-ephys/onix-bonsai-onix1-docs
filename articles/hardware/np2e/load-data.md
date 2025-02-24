---
uid: np2e_load-data
title: Load Data
---

A script for loading data from the NeuropixelsV2e Headstage [example workflow](xref:np2e) is
available [here](https://colab.research.google.com/drive/1me3HUaqB7IulBrWIYgq8-9hYu-nDFkLc?usp=sharing) 
as a Google Colab.

> [!NOTE]
> This script will attempt to load entire files into arrays. For long recordings, data will need to
> be split into more manageable chunks by:
> - Modifying this script to partially load files
> - Modifying the workflow to cyclically create new files after a certain duration
