---
uid: visualize-data
title: Visualize Data
---

Bonsai includes default visualizers that can be used to display data. Visualizers can be opened by double-clicking a node while the workflow is running.
Not all operators have visualizers, because the operator data output type has to be compatible with Bonsai's default visualizers. Data frames from OpenEphys.Onix1, for example, aren't compatible with Bonsai's default visualizers, but its members are.

Some visualizers are available as Bonsai operators and can be found in the `Bonsai.Design.Visualizers` package, which can be installed in the Bonsai package manager. These operators must be placed in the workflow and be linked to a data operator. The visualizer can be opened by double-clicking this visualizer node instead of the preceding data node.

## Selecting operator data members for visualization

For nodes that require it such as ONIX [data I/O operators](xref:dataio), select the desired member: 
  1. Right-click the node that corresponds to the data I/O operator you'd like to visualize.
  1. Hover over the "Output" option that appears in the context menu.
  1. Click the member you would like to visualize from the list of members.

This populates the workflow with a <xref:Bonsai.Expressions.MemberSelectorBuilder> operator that selects the single
member from the data frame produced by the data I/O operator.

<video controls>
  <source src="../../images/select-member.mp4" type="video/mp4">
</video> 

## Selecting visualizers

Select the visualizer you would like to use for the data you would like visualize:
  1. Right-click the `MemberSelector` node labelled with the member you would like to visualize.
  1. Hover over the "Select Visualizer" option in the context menu.
  1. Click the visualizer you would like to use from the list of visualizers.

<video controls>
  <source src="../../images/set-visualizer.mp4" type="video/mp4">
</video> 

## Opening visualizers

Open the visualizer and check:
  1. Start the workflow.
  1. If the desired visualizer is closed, double-click the `MemberSelector` node labelled with the member you would
     like to visualize.
  1. Visualize the data.     

        > [!NOTE]
        > Data will only be visualized if the operator is producing data. If you can't see any data, check that:
        > - The device from which you are trying to read is enabled.
        > - Events are occurring. Some devices are stream-based and some are device-based. Event-based devices only produce data upon certain
        >   events. For example, the <xref:OpenEphys.Onix1.DigitalInput> operator only produces data when the digital
        >   port status changes state.

> [!TIP] 
> Visualizers can be changed while the workflow is running, so Selecting and Opening visualizers steps can be done in any order. This allows you to try different visualizers (one at a time), which is particularly helpful if you don't know which visualizer you want to use.

## Configuring visualizers
Some visualizers, in particular, those that involve plots, allow additional
     configuration.

  1. Right-click the visualizer window to gain access to configuration options.
  
  For example, the MatVisualizer allows configuration of:
  - X and Y scale: click to toggle between "auto" and fixed values.
  - Channel view: click the grid square to toggle between superimposed or separate  
  - History Length: click the arrow and configure the number of samples displayed in the plot. 
  - Display Previous: click the arrow and configure the amount of buffers displayed in the plot. 
  - Channel Offset: click the arrow and configure the Y offset.
  - Channels per Page: click the arrow and configure the amount of channels displayed per visualizer page. The page number is displayed at the top of the visualizer. Move between pages by using the PageUp and PageDn keys on the keyboard. 

<video controls>
  <source src="../../images/visualize-data.mp4" type="video/mp4">
</video> 
