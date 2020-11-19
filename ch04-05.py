from device import Router, Switch

rtr1 = Router('iosV', '15.6', '10.10.10.1')
rtr2 = Router('isr', '16.9', '10.11.11.1')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.8')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), sep='')
print('Sw1\n', sw1.getdesc(), '\n', sep='')
