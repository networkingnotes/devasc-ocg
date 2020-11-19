class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router Model              :{self.model}\n'\
            f'Software Version          :{self.swversion}\n'\
            f'Router Management Address :{self.ip_add}'
        return desc

class Switch(Router):
    def getdesc(self):
        '''return a formatted description of the switch'''
        desc = (f'Switch Model              :{self.model}\n'
            f'Software Version          :{self.swversion}\n'
            f'Switch Management Address :{self.ip_add}')
        return desc

rtr1 = Router('iosV', '15.6', '10.10.10.1')
rtr2 = Router('isr', '16.9', '10.11.11.1')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.8')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), sep='')
print('Sw1\n', sw1.getdesc(), '\n', sep='')
