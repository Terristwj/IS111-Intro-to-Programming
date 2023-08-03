#include <stdio.h>

int main(void) {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    int breadth = n * 2 - 1;
    // Print top row
    for (int i = 0; i < breadth; i++) {
        printf("#");
    }
    printf("\n");

    // Print "V"
    for (int i = 1; i < n; i++) {
        for (int j  = 0; j < i; j++) {
            printf(" ");
        }

        breadth -= 2;
        for (int k = 0; k < breadth; k++) {
            if (k == 0 || k == breadth - 1) {
                printf("#");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}