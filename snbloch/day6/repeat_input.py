import io

f = open('input.txt', mode='r')

redistribution_cycles = 0
memory_banks = []
memory_banks_history = []
for line in f:
    for i in line.split(' '):
        memory_banks.append(int(i.strip()))

repeat_observed = False

while repeat_observed == False:

    i = 0
    maxval = 0
    maxindex = 0
    while i < len(memory_banks):
        if memory_banks[i] > maxval:
            maxindex = i
            maxval = memory_banks[i]
        i += 1

    redist_index = maxindex
    while memory_banks[maxindex] > 0:
        if redist_index == len(memory_banks) - 1:
            redist_index = 0
        else:
            redist_index += 1
        memory_banks[redist_index] += 1
        memory_banks[maxindex] -= 1

    redistribution_cycles += 1
    if memory_banks[:] in memory_banks_history:
        duplicate_index = memory_banks_history.index(memory_banks[:])
        repeat_observed = True
    else:
        memory_banks_history.append(memory_banks[:])

print 'Completed ' + str(redistribution_cycles) + ' redistribution cycles when encountering a duplicate memory bank state'
print 'The duplicated state was originally encountered on cycle number ' + str(duplicate_index + 1)
print 'It took ' + str(redistribution_cycles - (duplicate_index + 1)) + ' cycles for the duplicate to occur'
