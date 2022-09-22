
#include <stdio.h>

int main() {
  
    int height,i,x,y;
    printf("Enter height of pyramid: ");
    scanf("%d",&height);
    
    for(i=1; i<=height; i++){
        for (x=1; x<= (height-i); x++)
            printf(" ");
    
        for (y=1; y<= (2*i-1); y++)
            printf("*");
        
        printf("\n");

    }
    return 0;
}