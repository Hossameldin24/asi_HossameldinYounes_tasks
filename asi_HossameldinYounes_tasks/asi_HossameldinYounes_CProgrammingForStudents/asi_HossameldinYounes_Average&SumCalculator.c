
#include <stdio.h>

int main() {
    int num1;
    int num2;
    int num3;

    printf("Enter a number: ");
    scanf("%d", &num1);
    
    printf("Enter a number: ");
    scanf("%d", &num2);
    
    printf("Enter a number: ");
    scanf("%d", &num3);
    
    printf("sum is %d \n", num1 + num2 + num3);
    printf("average is %f", (num1 + num2 + num3)/3.0);


    return 0;
}