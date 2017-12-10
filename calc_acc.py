def acc(v,u,t):
    """ function to calculate acceleration"""
    return ((v-u)/t)

print("we know\n\tv = u + at\n\ta = (v-u)/t")
v=25
u=0
t=10
unit="m/s"
print("for v = {0}{3}, u = {1}{3} and t = {2}s\nwe have,\n\ta = {4}m/s\u00b2".format(v,u,t,unit,acc(v,u,t)))
