import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Rastgele koordinatları üretin
num_points = 1000
x_coords = np.random.randint(0, 1000, num_points)
y_coords = np.random.randint(0, 1000, num_points)

df = pd.DataFrame({'x': x_coords, 'y': y_coords})


excel_file = 'koordinatlar.xlsx'
df.to_excel(excel_file, index=False)


df = pd.read_excel(excel_file)


x_coords = df['x']
y_coords = df['y']


grid_size = 100  # 50*50, 100*100, 200*200 olarak değiştirilebilir
num_colors = (1000 // grid_size) * (1000 // grid_size)
colors = plt.cm.get_cmap('hsv', num_colors)


grid_labels = {}
color_index = 0
for x_bin in range(0, 1000, grid_size):
    for y_bin in range(0, 1000, grid_size):
        grid_labels[(x_bin, y_bin)] = colors(color_index)
        color_index += 1


colored_points = []
for x, y in zip(x_coords, y_coords):
    grid_x = (x // grid_size) * grid_size
    grid_y = (y // grid_size) * grid_size
    colored_points.append(grid_labels[(grid_x, grid_y)])


plt.figure(figsize=(10, 10))
plt.scatter(x_coords, y_coords, c=colored_points, s=10)

for x_bin in range(0, 1000, grid_size):
    plt.axvline(x_bin, color='gray', linewidth=0.5)
for y_bin in range(0, 1000, grid_size):
    plt.axhline(y_bin, color='gray', linewidth=0.5)


plt.xlabel('X Koordinatı')
plt.ylabel('Y Koordinatı')
plt.title('Rastgele Noktaların 100*100 Izgaraya Göre Renklenmesi')
plt.grid(False)


plt.savefig('verimadenciligi.jpeg')
plt.show()