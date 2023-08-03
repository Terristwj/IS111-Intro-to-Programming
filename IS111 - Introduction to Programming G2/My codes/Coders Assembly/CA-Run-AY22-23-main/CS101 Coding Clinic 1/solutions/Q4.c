#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(0));

    int result = rand() % 100 + 1;
    int n;
    int guesses = 0;

    do {
        printf("Enter n: ");
        scanf("%d", &n);

        if (n > 100 || n < 1) {
            printf("Out of bounds! Enter a number from 1 to 100\n\n");
        } else if (n > result) {
            printf("Too high!\n\n");
        } else if (n < result) {
            printf("Too low!\n\n");
        }

        guesses++;
    } while (n != result);

    printf("Jackpot! %d guesses taken\n", guesses);
}