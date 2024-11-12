---
uid: visualize-data
title: Visualize Data
---

Bonsai includes default visualizers that can be used to display data. They are displayed by double-clicking a node while the workflow is running.
Not all nodes have visualizers, since the data type output by the node has to be compatible with Bonsai's default visualizers. Data frames from OpenEphys.Onix1, for example, aren't compatible with Bonsai's default visualizers, but its members are.  

## Member selection

For nodes that require it such as ONIX [data I/O operators](xref:dataio), select the desired member: 
  1. Right-click the node that corresponds to the data I/O operator you'd like to visualize.
  1. Hover over the "Output" option that appears in the context menu after the previous step.
  1. Click the member you would like to visualize from the list of members that appears after the previous step

This populates the workflow with a <xref:Bonsai.Expressions.MemberSelectorBuilder> operator that selects the single
member from the data frame produced by the data I/O operator.

<video controls>
  <source src="../../images/select-member.mp4" type="video/mp4">
</video> 

## Visualizer selection

The second step is to select the visualizer you would like to use for the data you would like visualize. To
accomplish this:
  1. Right-click the `MemberSelector` node labelled with the member you would like to visualize.
  1. Hover over the "Select Visualizer" option in the context menu that appears after the previous step.
  1. Click the visualizer you would like to use from the list of visualizers that appears after the step.

<video controls>
  <source src="../../images/set-visualizer.mp4" type="video/mp4">
</video> 

## Visualizer configuration

The last step is to open and configure the visualizer. To accomplishe this:
  1. Start the workflow
        > [!NOTE]
        > Data will only be visualized if the operator is producing data. If this is your problem, there a couple
        > reasons this might be:
        > - Confirm the device from which you are trying to read is enabled.
        > - Some devices are stream-based and some are device-based. Event-based devices only produce data upon certain
        >   events. For example, the <xref:OpenEphys.Onix1.DigitalInput> operator only produces data when the digital
        >   port status changes state. Confirm events are occurring.
  1. If the desired visualizer is closed, double-click the `MemberSelector` node labelled with the member you would
     like to visualize 
  1. Right-click the visualizer. Some visualizers, in particular ones that involve plots, allow additional
     configuration. For example, the MatVisualizer allows changing the scale of the plot and the number of samples
     displayed in the plot. Right-clicking the visualizer window provides access to these options.

<video controls>
  <source src="../../images/visualize-data.mp4" type="video/mp4">
</video> 

> [!TIP] 
> Visualizers can be changed while the workflow is running. This facilitates comparison of different visualizers while
> data is being streamed without having to stop the workflow. In other words, the last two steps can happen
> interchangeably which is particularly helpful if you don't know which visualizer you want to use yet.

> [!NOTE]
> Some visualizers also come as Bonsai operators and can be found in the `Bonsai.Design.Visualizers` package, which
> can be installed in the Bonsai package manager. These operators must be placed in the workflow and be linked to a
> data operator to visualize the data properly. If so, this secondary operator the visualizer is toggled from this node.
