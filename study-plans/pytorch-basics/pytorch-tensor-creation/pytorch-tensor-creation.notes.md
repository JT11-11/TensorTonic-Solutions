- tensor: n-dim array.

- 3 Arguments: 

- Shape
- Precision level
- Compute type (GPU/CPU)
- from python data: use .tensor(data)

- Always copies the data --&gt; to use zero-copy, use .from_numpy(arr) function for numpy
- Diff  .Tensor() vs .tensor()

- .Tensor creates the data with default precision etc while .tensor allows u to define the parameters of the data.