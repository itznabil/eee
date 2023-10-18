clc;
clear all;
data=[1 0 0 -1
      1 2 0 -2.5
      1 3 0 -5
      2 0 0 -1.25
      2 3 0 -5
      3 4 0 -12.5];

sbn=data(:,1);
ebn=data(:,2);
G=data(:,3);
B=data(:,4);
yd1=max(sbn);
yd2=max(ebn);
nbus=max(yd1,yd2);
Ybus=zeros(nbus,nbus);
brn=length(sbn);
y=G+j*B;
 
for k=1:brn
    if sbn(k)>0 & ebn(k)>0
        
        Ybus(sbn(k),ebn(k))= -y(k);
        Ybus(ebn(k),sbn(k))= -y(k);
       
    end
end


for  t=1:nbus
   for p=1:brn
       if  sbn(p)==t | ebn(p)==t
           Ybus(t,t)= Ybus(t,t)+y(p);
       end
   end
end
    Ybus
    
    
    
    
    