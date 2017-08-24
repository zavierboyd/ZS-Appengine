import zscript as zs

fib = '''a := random
b := (1, 1)
a_ = a + b
b_ = a
trace a
trace b
graph a
next 10'''
env = zs.Env()

print(zs.compilerun(fib, env))
i = 0
gen = zs.compilerun('next 0', env)[0]
while i < 100:
    print(next(gen))
    i += 1