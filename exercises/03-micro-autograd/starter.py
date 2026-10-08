class Value:
    def __init__(self,data,_children=(),_op=''):
        self.data=float(data); self.grad=0.0; self._prev=set(_children); self._op=_op; self._backward=lambda:None
    # TODO: add, mul, pow, relu, backward
