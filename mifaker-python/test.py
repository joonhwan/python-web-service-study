from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets as ds
from sklearn.preprocessing import MinMaxScaler

color_map = plt.cm.get_cmap('viridis')
scaler = MinMaxScaler(feature_range=(0, 400))


x, y = ds.make_classification(n_samples=200,
                              n_features=2,
                              n_classes=3,
                              n_clusters_per_class=1,
                              #   n_informative=1,
                              class_sep=1,
                              n_redundant=0)
# x, y = ds.make_blobs(n_samples=200,
#                      centers=3,
#                      n_features=2)
# x, y = ds.make_moons(n_samples=200,
#                      noise=0.1)
# x, y = ds.make_s_curve(n_samples=200,
#                        noise=0.1)

x = scaler.fit_transform(x)

fig, ax = plt.subplots()
my_scatter_plot = ax.scatter(x[:, 0],
                             x[:, 1],
                             c=y,
                             vmin=min(y),
                             vmax=max(y),
                             s=5,
                             cmap=color_map,
                             alpha=1.0)
ax.set_title(None)

plt.show()
# with (
#     BytesIO() as buf,
#     open(f"output.jpg", 'wb') as ff
# ):
#     fig.savefig(buf, format="jpg")
#     ff.write(buf.getvalue())
