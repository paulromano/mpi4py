from ..MPI import Datatype
from numpy import DTypeLike, dtype

def from_numpy_dtype(dtype: DTypeLike) -> Datatype: ...
def to_numpy_dtype(datatype: Datatype) -> dtype: ...
