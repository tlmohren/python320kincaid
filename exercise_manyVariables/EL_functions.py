import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
from IPython.display import HTML
from matplotlib import animation, rc
from scipy.integrate import odeint  
import configparser

def m_v(n, total_mass=1):
    '''Create masses of pendulums'''
    return total_mass*np.ones((n ,1))/n

def len_v(n, total_len=1):
    '''Create pendulums lengths'''
    return total_len*np.ones((n ,1))/n

def y0_v(n):
    '''Get initial conditions vector'''
    y0 = np.zeros(n*2) 
    y0[:n] = np.random.rand(n)*np.pi   
    return y0

def wind(l_vec):
    '''Get figure window size based on length of all pendulums'''
    return 1.1*sum(l_vec)

def solve_and_plot(function, n, tInt, len_v, y0_v, m_v, g, b, 
                   figsize, wind, n_frames, title, fps=100, dot_scale=500, *args):
    '''Solve given function and plot simulation'''
    y0 = y0_v(n)
    l_vec = len_v(n)
    m = m_v(n)
    window = wind(l_vec)
    
    y1 = odeint(function, y0, tInt, args=(n, l_vec, m, g, b))
    make_plot(l_vec, y0, y1, n, m, n_frames, fps, figsize, window, dot_scale, title)

def pendulum(y, tInt, n, l_vec, m, g, b): 
    '''Pendulum dynamics function''' 
    dydt =  np.zeros([2*n])  
    M_ij = np.zeros((n,n))
    C_ij = np.zeros((n,n))
    S_ij = np.zeros((n,n)) 
    theta = y[0:n]  
    for i in range(n ):
        for j in range(n ): 
            m_max = np.max([i,j])  
            M_ij[i,j] = np.sum(m[m_max:])
            S_ij[i,j] = np.sin(theta[ i]-theta[ j])
            C_ij[i,j] = np.cos(theta[ i]-theta[ j])
    L = np.multiply(l_vec,l_vec.transpose()) 
    M = np.multiply(M_ij, np.multiply( L,C_ij)  )  
    C = np.multiply(M_ij, np.multiply( L,S_ij)  )  
    np.fill_diagonal(C,0)
    K = np.multiply( np.diag(l_vec)*g, M_ij) 
    D = np.diag(np.ones(n))*b 
    dydt[0:n] = y[n:n*2]
    dydt[n:n*2] = -np.dot(np.linalg.inv(M), (np.dot(C,y[ n:n*2]**2) +
                  np.dot(K, np.sin( y[0:n])) +
                  np.dot(D,y[n:n*2]))) 
    return dydt

def animate(i, n, l_vec, y, line, dots): 
    '''Update animation with new frame'''
    x_pos, y_pos = position_vectors(l_vec, y[i,:n])
    line.set_data(x_pos, y_pos) 
    dots.set_offsets(np.vstack((x_pos, y_pos)).T.tolist())  
    return line, dots 

def position_vectors(l_vec, y_v):
    '''Solve for position of pendulum at any time point'''
    x_vec = np.multiply(l_vec[:,0], np.sin(y_v))
    y_vec = np.multiply(l_vec[:,0], np.cos(y_v)) 
    x_pos = np.array(np.hstack([0, np.cumsum(x_vec)]))
    y_pos = np.array(np.hstack([0, np.cumsum(y_vec)]))
    return x_pos, y_pos

def make_plot(l_vec, y0, y, n, m, n_frames, fps, figsize, window, dot_scale, title):
    '''Plot pendulum simulation'''
    fig = plt.figure(figsize=figsize)
    cmap = matplotlib.cm.get_cmap('Spectral')
    colors = [cmap(x/n) for x in range(0, n+1)]
    
    ax = fig.add_subplot(111)
    x_pos, y_pos = position_vectors(l_vec, y0[:n])
    sizes = [0]+list(m.flatten()) # add blank spot for center of pendulum
    sizes = [dot_scale*s for s in sizes]
    line = ax.plot(x_pos, y_pos, zorder=1, alpha=0.5, color='k')[0]
    dots = ax.scatter(x_pos, y_pos, zorder=2, s=sizes, 
                      c=colors[:n+1], edgecolors='k')
    
    ax.scatter([0], [0], marker='x', color='k', alpha=0.5, zorder=0, s=100)
    ax.set_title(title)
    ax.axhline(y=0, xmin=0, xmax=1, color='k', zorder=0) 
    ax.set_xlim(-window, window)
    ax.set_ylim(-window, window)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
    anim = animation.FuncAnimation(fig, animate, fargs=[n, l_vec, y, line, dots], 
           frames=n_frames, interval=int(1000/fps), blit=True)
    html = HTML(anim.to_html5_video())
    display(html)
    
    plt.clf()
    plt.close('all') # clear memory