import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## Q1. 
# 2nd order Runge-Kutta method
dt, tmin, tmax = 0.1, 0.0, 10.0 # set \Delta t, t0, tmax
step=int((tmax-tmin)/dt) # create array t from tmin to tmax with equal interval dt
t = np.linspace(tmin,tmax,step)
y = np.zeros(step) # initialize array y as all 0
ya = np.exp(-t) # analytical solution y=exp(-t)
plt.plot(t,ya,label='Exact',lw=5) # plot y vs. t (analytical)
y[0]=1.0 # initial condition
y1 = np.zeros(step)
for i in range(step-1):
    y1[i] = y[i]-0.5 * dt * y[i]
    y[i+1] = y[i]- dt * y1[i] # 2nd order Runge-Kutta method
dt, tmin, tmax = 0.1, 0.0, 10.0 # set
plt.plot(t, y, ls='--', lw=3, label='Numerical') # plot y vs t (numerical)
plt.plot(t, y/ya, lw=3, label='Ratio') # plot y/ya vs. t
plt.legend() #display legends
plt.show() #display plots


## Q3.
# Define variables
dim = 2 # system dimension (x,y)
nums = 1000 # number of steps
R = np.zeros(dim) # particle position
V = np.zeros(dim) # particle velocity
Rs = np.zeros([dim,nums]) # particle position (at all steps)
Vs = np.zeros([dim,nums]) # particle velocity (at all steps)
Et = np.zeros(nums) # total enegy of the system (at all steps)
time = np.zeros(nums) # time (at all steps)

# Define functions
def init(): # initialize animation
  particles.set_data([], [])
  line.set_data([], [])
  title.set_text(r'')
  return particles,line,title

# Animate simulation with 4th order Runge-Kutta method
R1 = np.zeros(dim)
V1 = np.zeros(dim)
R2 = np.zeros(dim)
V2 = np.zeros(dim)
R3 = np.zeros(dim)
V3 = np.zeros(dim)
R4 = np.zeros(dim)
V4 = np.zeros(dim)
def animate(i):
    global R,V,F,Rs,Vs,time,Et
    V1 = V - zeta/m*0.5*dt*V - k/m*0.5*dt*R
    R1 = R + V*0.5*dt
    V2 = V - zeta/m*0.5*dt*V1 - k/m*0.5*dt*R1
    R2 = R + V1*0.5*dt
    V3 = V - zeta/m*dt*V2 - k/m*dt*R2
    R3 = R + V2*dt
    V4 = V - (V+V1*2+V2*2+V3)/6.*zeta/m*dt - k/m*dt*(R+R1*2+R2*2+R3)/6.
    R4 = R + (V+V1*2+V2*2+V3)/6.*dt 
    R  = R4
    V  = V4
    Rs[0:dim,i]=R
    Vs[0:dim,i]=V
    time[i]=i*dt
    Et[i]=0.5*m*np.linalg.norm(V)**2+0.5*k*np.linalg.norm(R)**2
    particles.set_data(R[0], R[1])
    line.set_data(Rs[0,0:i], Rs[1,0:i])
    title.set_text(r"$t = {0:.2f},E_T = {1:.3f}$".format(i*dt,Et[i]))
    return particles,line,title

# System parameters
# particle mass, spring & friction constants
m, k, zeta = 1.0, 1.0, 0.
# Initial condition
R[0], R[1] = 1., 1. # Rx(0), Ry(0)
V[0], V[1] = 1., 0. # Vx(0), Vy(0)
dt = 0.1*np.sqrt(k/m) # set \Delta t
box = 5 # set size of draw area
# set up the figure, axis, and plot element for animatation
fig, ax = plt.subplots(figsize=(7.5,7.5)) # setup plot
ax = plt.axes(xlim=(-box/2,box/2),ylim=(-box/2,box/2)) # draw range
particles, = ax.plot([],[],'ko', ms=10) # setup plot for particle
line, = ax.plot([],[],lw=1) # setup plot for trajectry
title = ax.text(0.5,1.05,r'',transform=ax.transAxes,va='center') # title
anim = animation.FuncAnimation(fig,animate,init_func=init,
         frames=nums,interval=5,blit=True,repeat=False) # draw animation
# anim.save('movie.mp4',fps=20,dpi=400)

# Q4.
fig, ax = plt.subplots(figsize=(7.5,7.5))
ax.set_xlabel(r"$t$", fontsize=20)
ax.plot(time,Rs[0]) # plot R_x(t)
ax.plot(time,Rs[1]) # plot R_y(t)
ax.plot(time,Et) # plot E(t) (ideally constant if \deta=0)
ax.legend([r'$R_x(t)$',r'$R_y(t)$',r'$E_T(t)$'], fontsize=14)
plt.show()