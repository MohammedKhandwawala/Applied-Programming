//author:mohammed khandwawala(e16b117)
#include<stdio.h>
#include<math.h>
int main()
        {
        double n[1000];
        double alpha = M_PI;
        int k;
        n[0] = 0.2;
        double fractpart,intpart;
        for(k = 1; k <= 999; k++)
                {
                n[k] =  (n[k-1] + M_PI) * 100.0;
                fractpart = modf(n[k], &intpart);
                n[k] = fractpart;
                }
        for(k = 0; k <= 999; k++)
                {
                printf("%.4lf \n", n[k]);
                }
        }
