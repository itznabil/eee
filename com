###### LAB-4:
import math
ncore = float(input('Enter ncore:'))
nclad = float(input('Enter nclad:'))
NA = math.sqrt(ncore**2-nclad**2)
print('Numerical aperture: ',round(NA,5))

###### LAB 3: 
import math
EIRPu = float(input('Enter the uplink EIRP: '))
EIRPd = float(input('Enter the downlink EIRP: '))
GTRu = float(input('Enter the uplink GTR: '))
GTRd = float(input('Enter the downlink GTR: '))
FSLu = float(input('Enter the uplink FSL: '))
FSLd = float(input('Enter the downlink FSL: '))
RFLu = float(input('Enter the uplink RFL: '))
RFLd = float(input('Enter the downlink RFL: '))
AAu = float(input('Enter the uplink AA: '))
AAd = float(input('Enter the downlink AA: '))
AMLu = float(input('Enter the uplink AML: '))
AMLd= float(input('Enter the downlink AMl: '))
lossu = FSLu + RFLu + AAu + AMLu
print('Uplink loss: ',lossu)
lossd = FSLd + RFLd + AAd + AMLd
print('downlink loss: ',lossd)
CNRu = EIRPu + GTRu - lossu + 228.6
print('Total carrier to noise ratio for uplink is','{:.2f}'.format(CNRu),'decilog')
CNRd = EIRPd + GTRd - lossd + 228.6
print('Total carrier to noise ratio for downlink is','{:.2f}'.format(CNRd),'decilog')
CNRt = (CNRu*CNRd)/(CNRu+CNRd)
print('Total carrier to noise ratio is','{:.2f}'.format(CNRt),'decilog')

###### LAB-2:
import math
pt = float(input('Enter the input power in watts: '))
pt = 10*math.log(pt,10)
gt = float(input('Enter the transmitting antenna gain in db: '))
gr = float(input('Enter the received antenna gain in db: '))
EIRP = gt + pt
f = float(input('Enter the frequency : '))
d = float(input('Enter the distance in km: '))
fsl = 32.4 + 20*math.log(d, 10) + 20*math.log(f,10) 
rfl = float(input('Enter the received feeder loss in db: '))
aa = float(input('Enter the atmospheric absorption loss in db: '))
aml = float(input('Enter the antenna misalignment loss in db: '))
pl = float(input('Enter the polarization loss in db: '))
losses = fsl + rfl + aa + aml + pl
print(f'Total loss:{losses} db')
p = EIRP + gr - losses
print(f'Total loss power:{p} db')

###### LAB-1: 
import math
f = float(input('Enter the frequency in mhz:')) 
d = float(input('Enter the distance in km:'))
gt = float(input('Enter the transmitting antenna gain in db:'))
gr = float(input('Enter the receiving antenna gain in db:'))
pt = float(input('Enter the transmitted power in db: '))

fsl = 32.44 + 20*math.log(d,10) + 20*math.log(f,10)
print('The path loss is: ','{:.2f}'.format(fsl),'db')
pr = gt + gr + pt - fsl
print('The received power is: ','{:.2f}'.format(pr),'db')
prw = math.pow(10,(pr/10))
print('The received power is: ',prw,'watts')
