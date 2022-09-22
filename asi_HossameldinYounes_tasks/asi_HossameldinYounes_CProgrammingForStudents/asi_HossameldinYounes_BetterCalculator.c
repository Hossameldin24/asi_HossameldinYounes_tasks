
#include <stdio.h>

int main() {
    double num1;
    double num2;
    char operater;

    printf("Enter a number: \n");
    scanf("%lf", &num1);
    
    printf("Enter an operator: \n");
    scanf("%c", &operater);
    
    printf("Enter a number: \n");
    scanf("%lf", &num2);
    
    if(operater == '+'){
        printf("%f", num1 + num2);
    }else if(operater == '-'){
        printf("%f", num1 - num2);
    }else if(operater == '*'){
        printf("%f", num1*num2);
    }else if(operater == '/'){
        printf("%f", num1/num2);
    }else{
        printf("wrong operator ");
    }


    return 0;
}