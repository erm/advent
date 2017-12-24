import io
from collections import Counter

file = open('input.txt', 'r')

components = []

for line in file:
    line = line.strip().split('/')
    components.append([int(line[0]), int(line[1])])

bridge_lengths = []
bridge_strengths = []
longest_bridge = []
longest_bridge_strength = 0
current_bridge = []

def choose_next_path(previous, last):
    if last[0] == previous[0] or last[0] == previous[1]:
        #print 'Choosing ',last[1]
        return last[1]
    else:
        #print 'Choosing ',last[0]
        return last[0]

def build_bridge(current_bridge, components):
    #print 'Building bridge out of current bridge: ',current_bridge
    found_next = False
    global longest_bridge, longest_bridge_strength
    global bridge_lengths, bridge_strengths
    if len(current_bridge) == 0:
        #print 'New bridge detected, starting at port 0'
        current_port = 0
    elif len(current_bridge) == 1:
        #print '1 component in existing bridge.  Choosing a path from ',current_bridge[-1]
        current_port = choose_next_path([0,0], current_bridge[-1])
    else:
        #print 'Multiple components in existing bridge.  Choosing a path from ',current_bridge[-1]
        current_port = choose_next_path(current_bridge[-2], current_bridge[-1])
    for component in components:
        if current_port in component:
            #print 'Found next component to use: ',component
            found_next = True
            new_bridge = current_bridge[:]
            new_bridge.append(component)
            #print 'New bridge assembled with next component: ',new_bridge
            new_components = components[:]
            #print 'Removing component: ',component
            new_components.remove(component)
            #print 'New components list: ',new_components
            build_bridge(new_bridge, new_components)
    if found_next == False:
        current_bridge_strength = 0
        #print 'Did not find another component to add to the bridge!'
        #print current_bridge
        for component in current_bridge:
            current_bridge_strength += component[0] + component[1]
        current_bridge_length = len(current_bridge)
        print 'Length of current bridge: ',current_bridge_length
        bridge_lengths.append(current_bridge_length)
        bridge_strengths.append(current_bridge_strength)

build_bridge(current_bridge, components)
max_bridge_length = max(Counter(bridge_lengths))
longest_bridges = [i for i,val in enumerate(bridge_lengths) if val==max_bridge_length]
longest_strongest_bridge = 0
for i in longest_bridges:
    if bridge_strengths[i] > longest_strongest_bridge:
        longest_strongest_bridge = bridge_strengths[i]
print longest_strongest_bridge
