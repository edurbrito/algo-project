import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv("src/speedup.csv")

palette = sb.color_palette("bright", n_colors=5)

sb.lineplot(data=dt, x="points", y="speedup", hue="axes", palette=palette)
plt.title("Linear Search / (Build Tree + Range Search) | 20 Queries")
plt.show()