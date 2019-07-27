# -*- coding: utf-8 -*-
"""

@author: siksdad
Yoon Kim
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation


class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)

        self.t = np.linspace(0, 4, 400)
        self.x = np.cos(np.pi*self.t)
        self.y = np.sin(np.pi*self.t)
        self.z = self.t

        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        self.line1 = Line2D([], [], color='black')
        self.line1z = Line2D([], [], color='blue')
        self.line1a = Line2D([], [], color='red', linewidth=2)
        self.line1e = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        ax1.add_line(self.line1)
        ax1.add_line(self.line1z)
        ax1.add_line(self.line1a)
        ax1.add_line(self.line1e)
        ax1.set_xlim(-1.5, 1.5)
        ax1.set_ylim(-1.5, 1.5)
        ax1.set_aspect('equal', 'datalim')
        ax1.grid(linestyle='-')
        ax1.set_title('Angle at Circle')
        ax1.xaxis.set_ticks(np.arange(-1.5, 2.0, 0.5))
        ax1.yaxis.set_ticks(np.arange(-1.5, 2.0, 0.5))


        ax2.set_xlabel('A')
        ax2.set_ylabel('y')
        self.line2 = Line2D([], [], color='black')
        self.line2a = Line2D([], [], color='red', linewidth=2)
        self.line2e = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        ax2.add_line(self.line2)
        ax2.add_line(self.line2a)
        ax2.add_line(self.line2e)
        ax2.set_xlim(0, 4)
        ax2.set_ylim(-1.5, 1.5)
        ax2.grid(linestyle='-')
        ax2.set_title('y=sin(A*pi)')
        ax2.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
        ax2.yaxis.set_ticks(np.arange(-1.5, 2.0, 0.5))

        ax3.set_xlabel('x')
        ax3.set_ylabel('A')
        self.line3 = Line2D([], [], color='black')
        self.line3a = Line2D([], [], color='red', linewidth=2)
        self.line3e = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        ax3.add_line(self.line3)
        ax3.add_line(self.line3a)
        ax3.add_line(self.line3e)
        ax3.set_xlim(-1.5, 1.5)
        ax3.set_ylim(0, 4)
        ax3.grid(linestyle='-')
        ax3.set_title('x=cos(A*pi)')
        ax3.xaxis.set_ticks(np.arange(-1.5, 2.0, 0.5))
        ax3.yaxis.set_ticks(np.arange(0, 4.5, 0.5))

        animation.TimedAnimation.__init__(self, fig, interval=50, blit=True)

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
        head_slice = (self.t > self.t[i] - 0.2) & (self.t < self.t[i])

        self.line1.set_data(self.x[:i], self.y[:i])
        self.line1z.set_data([0.0,self.x[i]], [0.0,self.y[i]])
        self.line1a.set_data(self.x[head_slice], self.y[head_slice])
        self.line1e.set_data(self.x[head], self.y[head])

        self.line2.set_data(self.z[:i], self.y[:i])
        self.line2a.set_data(self.z[head_slice], self.y[head_slice])
        self.line2e.set_data(self.z[head], self.y[head])

        self.line3.set_data(self.x[:i], self.z[:i])
        self.line3a.set_data(self.x[head_slice], self.z[head_slice])
        self.line3e.set_data(self.x[head], self.z[head])

        self._drawn_artists = [self.line1, self.line1z, self.line1a, self.line1e,
                               self.line2, self.line2a, self.line2e,
                               self.line3, self.line3a, self.line3e]



    def new_frame_seq(self):
        return iter(range(self.t.size))

    def _init_draw(self):
        lines = [self.line1, self.line1z,self.line1a, self.line1e,
                 self.line2, self.line2a, self.line2e,
                 self.line3, self.line3a, self.line3e]
        for l in lines:
            l.set_data([], [])

ani = SubplotAnimation()
#ani.save('test_sub.mp4')
plt.show()
