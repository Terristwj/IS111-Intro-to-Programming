#include <stdio.h>

// V1: nested conditionals
int main(void) {
    int yr; 

    printf("Enter year: ");
    scanf("%d", &yr);

    if (yr % 4 == 0) {
        if (yr % 100 != 0 || yr % 400 == 0) {
            printf("%d is a leap year\n", yr);
        } else {
            printf("%d is not a leap year\n", yr);    
        }
        
    } else {
        printf("%d is not a leap year\n", yr);
    }

}