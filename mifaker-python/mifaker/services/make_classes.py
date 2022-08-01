from io import BytesIO
from random import seed
from re import A
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG

from sklearn import datasets as ds
from sklearn.preprocessing import MinMaxScaler
from fastapi.responses import StreamingResponse
from mifaker.models.generate import MakeClassesRequest, MakeClassesResponse

import matplotlib
# matplotlib.use('Agg')

# color_map = plt.cm.get_cmap('viridis')
color_map = plt.cm.get_cmap('RdYlBu')
# color_map_discrete = plt.colors.LinearSegmentedColormap.from_list(
#     "", ["red", "cyan", "magenta", "blue"])
np.random.seed(0)


def _make_classes(request: MakeClassesRequest):
    seed = request.seed or np.random.randint(1, 100000000)
    features, classes = ds.make_classification(n_samples=request.samples,
                                               n_features=2,
                                               n_classes=request.classes,
                                               n_clusters_per_class=1,
                                               class_sep=request.separation,
                                               flip_y=request.noise,  # TODO CHECKME
                                               n_redundant=0,
                                               random_state=seed)
    scaler = MinMaxScaler(feature_range=(0, 400))
    print(features.shape)
    features = scaler.fit_transform(features)
    # classes = scaler.fit_transform(classes)
    return features, classes, seed


def make_classes(request: MakeClassesRequest) -> MakeClassesResponse:
    features, classes, seed = _make_classes(request)

    xs = features[:, 0].tolist()
    ys = features[:, 1].tolist()
    classes = classes.tolist()
    print(classes)
    return MakeClassesResponse(xs=xs, ys=ys, classes=classes, seed=seed)


def _make_classes_figure(request: MakeClassesRequest) -> Figure:
    features, classes, _ = _make_classes(request)
    x, y = features[:, 0], features[:, 1]

    fig = Figure(figsize=(6, 6))
    fig.set_dpi(300)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("")
    ax.scatter(x, y,
               c=classes,
               vmin=min(classes),
               vmax=max(classes),
               s=10,
               cmap=plt.cm.rainbow,
               alpha=1.0)

    return fig


def make_classes_svg(request: MakeClassesRequest) -> StreamingResponse:
    fig = _make_classes_figure(request)
    buf = BytesIO()
    # FigureCanvasAgg(fig).print_jpg(buf)
    # FigureCanvasSVG(fig).print_svg(buf, dpi=300)
    svg = FigureCanvasSVG(fig)
    svg.print_svgz(buf)
    buf.seek(0)
    return StreamingResponse(content=buf, media_type="image/svg+xml", headers={"Content-Encoding": "gzip"})


def make_classes_jpg(request: MakeClassesRequest) -> StreamingResponse:
    fig = _make_classes_figure(request)
    buf = BytesIO()
    # FigureCanvasAgg(fig).print_jpg(buf, dpi=600, quality=100)
    fig.savefig(buf, format="jpg")
    buf.seek(0)
    return StreamingResponse(content=buf, media_type="image/jpeg")
