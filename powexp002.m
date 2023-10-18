clc;
clear all;
 y=[20-50i  -10+20i  -10+30i
    -10+20i  26-52i  -16+32i
    -10+30i  -16+32i  26-62i];

nbus=length(y);
sbase=100;

data=[ 1   0   0   0       0        1.05   0    1
       2   0   0   256.6   110.2    1.00   0    2
       3   0   0   138.6   45.2     1.00   0    2];
   
   pgen=data(:,2); 
   qgen=data(:,3);
   pload=data(:,4);
   qload=data(:,5);  
   V=data(:,6);
   bustp=data(:,8);
   sgen=pgen+j*qgen;
   sload=pload+j*qload;
   sch=(sgen-sload)/sbase;
   P=real(sch);
   Q=imag(sch);
   yv=0;
 
 
 for k=1:7;
    for a=2:nbus
        for b=1:nbus;
            if(a~=b)
                yv=yv+y(a,b)*V(b);
                
            end
        end
        
        if  bustp(a)==3
            Q(a)= -img (conj(V(a))*((V(a)*y(a,a)+yv)));
            
        end
        
        sdv=(P(a)-j* Q(a))/conj(V(a)); 
            V(a)= (sdv - yv) / y(a,a);
            yv=0;
            
    end 
 end
 
 for c = 1:1
     for d = 1:nbus
         if (c~=d)
             yv=yv+y(c,d)*V(d);
         end
     end
 end
 V
 
                
                
 
 
 