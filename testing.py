from zscript import *


#######################################################################################################################


# p_init = """L = 1350
# albedo = 0.3
# epsilon = 1
# sigma = 5.67*10^-8
# waterdepth = 4000
# heatcapground = 4.2*1000^2*waterdepth
# heatcapair = 100^2*30
#
# csurface = 6.916*10^7
# tsurface = 1.669*10^8
# circlearea = 6.39*10^13
# cshadow = 8.425*10^6
# tshadow = 4.910*10^7
# cair = 226
# cground = 247
# tair = 282
# tground = 303
# tgroundsolar = L*(1-albedo)*tshadow
# cgroundsolar = L*(1-albedo)*cshadow
# cgroundcap = heatcapground*csurface
# caircap = heatcapair*csurface
# tgroundcap = heatcapground*tsurface
# taircap = heatcapair*tsurface
# cgroundcon = cground*cgroundcap
# caircon = cair*caircap
# tgroundcon = tground*tgroundcap
# taircon = tair*taircap
# dt = 60*60*24
#
# tcair = 0
# tcground = 0
# tairspace == (epsilon*tsurface*sigma*tair^4)
# tairground == (epsilon*tsurface*sigma*tair^4)
# tgroundair == epsilon*tsurface*sigma*tground^4
#
# ctair = 0
# ctground = 0
# cairspace == (epsilon*csurface*sigma*cair^4)
# cairground == (epsilon*csurface*sigma*cair^4)
# cgroundair == epsilon*csurface*sigma*cground^4
#
# tairin == tgroundair + ctair
# tairout == tairground + tairspace + tcair
# tgroundin == tairground + ctground + tgroundsolar
# tgroundout == tcground + tgroundair
#
# cairin == cgroundair + tcair
# cairout == cairground + cairspace + tcair
# cgroundin == cairground + tcground + cgroundsolar
# cgroundout == ctground + cgroundair
# """
#
# p_loop = """
# tcair = tairin - tairout
# tcground = tgroundin - tgroundout
# ctair = cairin - cairout
# ctground = cgroundin - cgroundout
#
# cairdelta = cairin - cairout
# cgrounddelta = cgroundin - cgroundout
# tairdelta = tairin - tairout
# tgrounddelta = tgroundin - tgroundout
#
# caircon = caircon + cairdelta*dt
# cgroundcon = cgroundcon + cgrounddelta*dt
# taircon = taircon + tairdelta*dt
# tgroundcon = tgroundcon + tgrounddelta*dt
#
# cair = caircon/caircap
# cground = cgroundcon/cgroundcap
# tair = taircon/taircap
# tground = tgroundcon/tgroundcap
# """
#
# env = {}
# compilerun(p_init, env)
#
# for i in range(100):
#     print()
#     print()
#     print(i)
#     compilerun(p_loop, env)
#
# print('--------------------------------------------------------------------------------------------------------------')
# for k, v in env.items():
#     print(k, ': ', v(env))
# print('--------------------------------------------------------------------------------------------------------------')
# print(env)


#######################################################################################################################

p = '''
p = 9
c = p < 10
c
'''

print(list(compilerun(p, {})))

f = '''
for i=0; i < 10; i+1 | i in list
a = a + i
b = b + a + a
c = c + b + b
d = d + c + c
next

'''
'''x = []
for i in lexer(f):
    x.append(i)
    if i[0] == 'NL':
        print(x)
        x = []
'''
repl()
