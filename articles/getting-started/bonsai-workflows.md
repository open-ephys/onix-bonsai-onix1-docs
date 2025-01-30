---
uid: bonsai-workflows
title: Bonsai Workflows
---

Scripts in Bonsai are known as **workflows**. A workflow comprises of "operators" that are represented
by nodes which connect to form a data processing graph. Each connection indicates that the
downstream operator on the right takes the sequence of data from the upstream operator on the left
as input. The behavior of an operator depends on its type. For example:

- A `source` operator produces its own sequence of data.
- A `transform` operator transforms data in its input sequence.
- A `sink` operator produces a side effect (such as writing data or outputting an external signal
like a noise through your computer's speaker or a digital output toggle through your ONIX breakout
board).
- A `combinator` operator controls the flow of downstream sequences.

The workflow editor represents these operators using different colors and a grey arc. The [official
Bonsai docs](https://bonsai-rx.org/docs/articles/operators.html) provides a nice description of operators
and the various types with pictures.

Below is an example workflow which configures ONIX hardware.

::: workflow
![/workflows/getting-started/start-acquisition.bonsai workflow](../../workflows/getting-started/start-acquisition.bonsai)
:::

> [!TIP]
> This workflow, and others like it in these docs, can be copied and pasted into
> the Bonsai editor using the clipboard icon that appears when you hover your
> mouse over the image.

We'll take a closer look at how this workflow is created and what it's used for
in the following pages.