import imageio.v2 as imageio 
filenames = ['pic_a.png', 'pic_b.png']
images= [ ]

for filename in filenames:
    images.append(imageio.imread(filename))
    
imageio.mimsave('team.gif', images, duration=0.5, loop=0)