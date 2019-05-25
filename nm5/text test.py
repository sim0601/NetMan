'''with open('IPadds.txt', 'w') as f:
    print("Writing IP's to file")
    n= 1
    for n in range(5):
        f.write("Appended line %d \n" %(n+1))'''
'''a='hello'
b='hi there'
with open('IPadds.txt', 'a+') as f:
    print("Writing IP's to file")
    f.write(a+"\n")
    f.write(b)'''

ip_add = {}
a=1
b=2
ip_add['R1'] = {}
ip_add['R1']['Addresses'] = {}
ip_add['R1']['Addresses']['v4'] = {}
ip_add['R1']['Addresses']['mac'] = {}
ip_add['R1']['Addresses']['v4']['fa0/0'] = {a}
ip_add['R1']['Addresses']['mac']['fa0/0'] = {a}
ip_add['R1']['Addresses']['v4']['fa0/1'] = {b}
ip_add['R1']['Addresses']['mac']['fa0/1'] = {a}
print(ip_add)

with open('iptest.txt', 'w') as f:
    f.write(str(ip_add))
#int_status['r2_stat'] = {'3', '4'}
#int_status['r3_stat'] = {'5', '6'}
#int_status['r4_stat'] = {'7', '8'}
#int_status['r5_stat'] = {'9', '10'}

#int_status = {r1_stat,r2_stat,r3_stat,r4_stat,r5_stat}
#print(type(int_status))
#print(r1)
#print(r2_stat)
#print(r3_stat)
#print(r4_stat)
#print(r5_stat)



import time
import matplotlib.pyplot as plt

'''line1=[1,3,5,7]
plt.plot(line1)
line2=[2,6,7,8]
plt.plot(line2)

plt.legend(['line1', 'line2'], loc='upper left')
plt.margins(0.025)
plt.savefig("test.jpg")
plt.show()

print(time.ctime())

line3=[]

start = 0

for i in range(4):
    line3.append((time.ctime()))
    time.sleep(5)
    #start = start +5
#print(start)
print(line3)
plt.plot(line3)
plt.margins(0.025)
plt.legend(['CPU Utilization'], loc='upper left')
plt.savefig("CPU.jpg")
plt.show()'''
