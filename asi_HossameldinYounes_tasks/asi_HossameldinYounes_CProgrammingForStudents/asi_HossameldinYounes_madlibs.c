
#include <stdio.h>

int main() {
    char colour[20];
    char noun[20];
    char celebrity[20];

    printf("Enter a colour");
    scanf("%s", colour);
    printf("Enter a plural noun");
    scanf("%s", noun);
    printf("Enter a celebrity");
    scanf("%s", celebrity);
    
    printf("roses are %s", colour);
    printf("%s are blue", noun);
    printf("i love %s", celebrity);

    return 0;
}