- tensor: n-dim array.

- 3 Arguments: 

- Shape
- Precision level
- Compute type (GPU/CPU)
- from python data: use .tensor(data)

- Always copies the data --&gt; to use zero-copy, use .from_numpy(arr) function for numpy
- Diff  .Tensor() vs .tensor()

- .Tensor creates the data with default precision etc while .tensor allows u to define the parameters of the data.
- tensor different methods to use:

1. method zero can use .zeros() to create matrix with zeros
2. if one with want, use .ones() to create matrix with ones
3. if u wanna to fill the matrix with a value, u need to specify it as a argument and every element in matrix will be filled by that value.