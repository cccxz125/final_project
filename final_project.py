import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']  
matplotlib.rcParams['axes.unicode_minus'] = False


number = 50

steps = 1000

box_size = 50

step_size = 1.5

temperature = 1.0

x = np.zeros((number, steps))
y = np.zeros((number, steps))

x[:, 0] = np.random.uniform(-50, 50, number)
y[:, 0] = np.random.uniform(-50, 50, number)


for t in range(1, steps):
    angle = np.random.uniform(0, 2*np.pi, number)
    dx = step_size * np.cos(angle)
    dy = step_size * np.sin(angle)

    x[:, t] = x[:, t-1] + dx
    y[:, t] = y[:, t-1] + dy

msd = np.mean((x - x[:, 0:1])**2 + (y - y[:, 0:1])**2, axis=0)


plt.figure(figsize=(6, 6))
for i in range(number):
    plt.plot(x[i], y[i], linewidth=0.8)

plt.title("布朗運動粒子軌跡")
plt.xlabel("X 位置")
plt.ylabel("Y 位置")
plt.grid(True)
plt.show()


plt.figure(figsize=(6, 4))
plt.plot(msd)
plt.title("均方位移 (MSD) 與時間關係")
plt.xlabel("時間（步數）")
plt.ylabel("MSD")
plt.grid(True)
plt.show()




x = np.zeros((number, steps))
y = np.zeros((number, steps))

x[:, 0] = np.random.uniform(-box_size/2, box_size/2, number)
y[:, 0] = np.random.uniform(-box_size/2, box_size/2, number)


for t in range(1, steps):
    angle = np.random.uniform(0, 2*np.pi, number)
    dx = step_size * np.cos(angle)
    dy = step_size * np.sin(angle)

    x[:, t] = x[:, t-1] + dx
    y[:, t] = y[:, t-1] + dy


    out_left   = x[:, t] < -box_size/2
    out_right  = x[:, t] >  box_size/2
    x[out_left, t]  = -box_size/2 + (-box_size/2 - x[out_left, t])
    x[out_right, t] =  box_size/2 - (x[out_right, t] - box_size/2)

    out_bottom = y[:, t] < -box_size/2
    out_top    = y[:, t] >  box_size/2
    y[out_bottom, t] = -box_size/2 + (-box_size/2 - y[out_bottom, t])
    y[out_top, t]    =  box_size/2 - (y[out_top, t] - box_size/2)


msd = np.mean((x - x[:, 0:1])**2 + (y - y[:, 0:1])**2, axis=0)


plt.figure(figsize=(6, 6))
for i in range(number):
    plt.plot(x[i], y[i], linewidth=0.7)

plt.title("布朗運動粒子軌跡（含邊界反射）")
plt.xlabel("X 位置")
plt.ylabel("Y 位置")
plt.xlim(-box_size/2, box_size/2)
plt.ylim(-box_size/2, box_size/2)
plt.grid(True)
plt.show()


plt.figure(figsize=(6, 4))
plt.plot(msd)
plt.title("均方位移（MSD）與時間關係")
plt.xlabel("時間（步數）")
plt.ylabel("MSD")
plt.grid(True)
plt.show()




fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-box_size/2, box_size/2)
ax.set_ylim(-box_size/2, box_size/2)
ax.set_title("布朗運動動畫（邊界反射 / 溫度調整）")
ax.set_xlabel("X 位置")
ax.set_ylabel("Y 位置")
sc = ax.scatter(x[:, 0], y[:, 0], s=10)


def update(frame):
    angle = np.random.uniform(0, 2*np.pi, number)
    dx = step_size * np.cos(angle)
    dy = step_size * np.sin(angle)

    x[:, frame] = x[:, frame-1] + dx
    y[:, frame] = y[:, frame-1] + dy


    out_left   = x[:, frame] < -box_size/2
    out_right  = x[:, frame] >  box_size/2
    x[out_left, frame]  = -box_size/2 + (-box_size/2 - x[out_left, frame])
    x[out_right, frame] =  box_size/2 - (x[out_right, frame] - box_size/2)

    out_bottom = y[:, frame] < -box_size/2
    out_top    = y[:, frame] >  box_size/2
    y[out_bottom, frame] = -box_size/2 + (-box_size/2 - y[out_bottom, frame])
    y[out_top, frame]    =  box_size/2 - (y[out_top, frame] - box_size/2)

 
    sc.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return sc,

ani = animation.FuncAnimation(fig, update, frames=steps, interval=30)
plt.show()
