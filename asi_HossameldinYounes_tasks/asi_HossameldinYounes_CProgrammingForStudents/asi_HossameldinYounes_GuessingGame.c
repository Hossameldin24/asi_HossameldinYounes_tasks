#include <stdio.h>

int main() {
    
    int secretnumber=5;
    int guess,guesscount = 0;
    int guesslimit = 2;
    int outofguess = 0;
    
    printf("Enter your guess: ");
    scanf("%d",&guess);
    
    if(guess == secretnumber){
            printf("You win");
    }
    
    while(guess != secretnumber){
        if(guesscount < guesslimit){
            printf("Enter your guess: ");
            scanf("%d",&guess);
            guesscount++;
        }else{
            printf("You are out of guesses");
            break;
        }
    }
    return 0;
}