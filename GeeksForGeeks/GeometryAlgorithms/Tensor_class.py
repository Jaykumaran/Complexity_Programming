class Tensor:
    def __init__(self, data):
        self.data = data
        self.shape = self._get_shape(data)

    def _get_shape(self, data):
        if isinstance(data, list):
            if len(data) == 0:
                return (0,)
            return (len(data),) + self._get_shape(data[0])
        else:
            return ()

    def _elementwise_add(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [self._elementwise_add(x, y) for x, y in zip(a, b)]
        else:
            return a + b

    def add(self, other):
        if self.shape != other.shape:
            raise ValueError("Shapes must be the same for addition")
        result_data = self._elementwise_add(self.data, other.data)
        return Tensor(result_data)

    def __repr__(self):
        return f"Tensor(shape={self.shape}, data={self.data})"


# Scalar
t0 = Tensor(5)
t0_added = t0.add(Tensor(10))
print(t0_added)  # Tensor(shape=(), data=15)

# 1D
t1 = Tensor([1, 2, 3])
t2 = Tensor([4, 5, 6])
print(t1.add(t2))  # Tensor(shape=(3,), data=[5, 7, 9])

# 2D
t3 = Tensor([[1, 2], [3, 4]])
t4 = Tensor([[5, 6], [7, 8]])
print(t3.add(t4))  # Tensor(shape=(2, 2), data=[[6, 8], [10, 12]])
