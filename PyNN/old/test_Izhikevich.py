

from pyNN.random import RandomDistribution, NumpyRNG
#from pyNN.neuron import *
from pyNN.nest import *
from pyNN.utility import get_script_args, Timer, ProgressBar, init_logging, normalized_filename
import matplotlib.pyplot as plt
import numpy as np


globalTimeStep = 0.01

timeStep = globalTimeStep

setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = -0.1
c = -55.0
d = 6.0

I = 0

v_init = -70
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)




neuron = create(cell_type)

neuron.initialize(**initialValues)


neuron.record('v')


totalTimes = np.zeros(0)
totalAmps = np.zeros(0)

times = np.linspace(0.0, 30.0, int(1 + (30.0 - 0.0) / timeStep))
amps = np.linspace(0.0, 0.0, int(1 + (30.0 - 0.0) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)

times = np.linspace(30 + timeStep, 300, int((300 - 30) / timeStep))
amps = np.linspace(0.075 * timeStep, 0.075 * (300 - 30), int((300 - 30) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)

injectedCurrent = StepCurrentSource(times=totalTimes, amplitudes=totalAmps)
injectedCurrent.inject_into(neuron)


#neuron.set(i_offset = 30)


run(300)






data = neuron.get_data().segments[0]




plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 7)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(G) Class 1 excitable')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 30, 300, 300],[-90, -90, -70, -90])

plt.show(block=False)
fig.canvas.draw()




############################################
##	Sub-plot H: Class 2 excitable
############################################

timeStep = globalTimeStep
setup(timestep=timeStep, min_delay=0.5)

a = 0.2
b = 0.26
c = -65.0
d = 0.0

I = -0.5

v_init = -64.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')


totalTimes = np.zeros(0)
totalAmps = np.zeros(0)

times = np.linspace(0.0, 30.0, int(1 + (30.0 - 0.0) / timeStep))
amps = np.linspace(-0.5, -0.5, int(1 + (30.0 - 0.0) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)

times = np.linspace(30 + timeStep, 300, int((300 - 30) / timeStep))
amps = np.linspace(-0.5 + 0.015 * timeStep, -0.5 + 0.015 * (300 - 30), int((300 - 30) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)

injectedCurrent = StepCurrentSource(times=totalTimes, amplitudes=totalAmps)
injectedCurrent.inject_into(neuron)


run(300)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 8)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(H) Class 1 excitable')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 30, 300, 300],[-90, -90,-70, -90]);

plt.show(block=False)
fig.canvas.draw()


#####################################################
##	Sub-plot R: Accomodation
#####################################################

timeStep = globalTimeStep
setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = 1.0
c = -55.0
d = 4.0

I = 0.0

v_init = -65.0
u_init = -16.0

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')


totalTimes = np.zeros(0)
totalAmps = np.zeros(0)

times = np.linspace(0.0, 200.0, int(1 + (200.0 - 0.0) / timeStep))
amps = np.linspace(0.0, 8.0, int(1 + (200.0 - 0.0) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)

times = np.linspace(200 + timeStep, 300, int((300 - 200) / timeStep))
amps = np.linspace(0.0, 0.0, int((300 - 200) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)

times = np.linspace(300 + timeStep, 312.5, int((312.5 - 300) / timeStep))
amps = np.linspace(0.0, 4.0, int((312.5 - 300) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)

times = np.linspace(312.5 + timeStep, 400, int((400 - 312.5) / timeStep))
amps = np.linspace(0.0, 0.0, int((400 - 312.5) / timeStep))
totalTimes = np.append(totalTimes, times)
totalAmps = np.append(totalAmps, amps)


injectedCurrent = StepCurrentSource(times=totalTimes, amplitudes=totalAmps)
injectedCurrent.inject_into(neuron)


run(400.0)



data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')

ax1 = fig.add_subplot(5, 4, 18)

#plt.xlabel("Time (ms)")
#plt.ylabel("Vm (mV)")
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(R) Accomodation')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, totalTimes,1.5 * totalAmps - 90);

plt.show(block=False)
fig.canvas.draw()



raw_input("Simulation finished... Press enter to exit...")










