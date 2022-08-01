from pydantic import BaseModel
from typing import List, Optional
# x, y = ds.make_classification(n_samples=200,
#                               n_features=2,
#                               n_classes=3,
#                               n_clusters_per_class=1,
#                               #   n_informative=1,
#                               class_sep=1,
#                               n_redundant=0)


class MakeClassesRequest(BaseModel):
    samples: Optional[int] = 200
    classes: Optional[int] = 1
    separation: Optional[float] = 1.0
    noise: Optional[float] = 0.01
    seed: Optional[int] = None


class MakeClassesResponse(BaseModel):
    xs: List[float]
    ys: List[float]
    classes: List[int]
    seed: int
