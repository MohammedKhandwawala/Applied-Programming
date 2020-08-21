//author:Mohammed Khandwawala(ee16b117)
#include <stdio.h>
int main()
        {
        int n = 1;
        int nold = 1;
        int new , i;
        printf("%d\t%d\n",1,nold);
        printf("%d\t%d\n",2,n);
        for(i = 3; i <= 10; i++)
                {
                new = n + nold;
                nold = n;
                n = new;
                printf("%d\t%d\n",i,n);
                }
                
        }
