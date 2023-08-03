#include <stdio.h>

// V2: Complex conditionals
int main(void) {
    int yr; 

    printf("Enter year: ");
    scanf("%d", &yr);

    if (yr % 400 == 0 || (yr % 4 == 0 && yr % 100 != 0)) {
        printf("%d is a leap year\n", yr);
    } else {
        printf("%d is not a leap year\n", yr);
    }

}