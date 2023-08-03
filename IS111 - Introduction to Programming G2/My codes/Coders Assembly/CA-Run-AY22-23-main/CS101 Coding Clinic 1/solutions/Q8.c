#include <stdio.h>
#include <math.h>

int main(void) {
    int n;
    printf("Input: ");
    scanf("%d", &n);

    printf("Factors: ");
    // Corner case
    if (n == 0) {
        printf("()\n");
        return 0;
    }

    // Handle negative values
    n = n > 0 ? n : -n; 

    // Fencepost first factor
    printf("(%d, %d)", n, 1);

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            printf(", (%d, %d)", n / i, i);
        }
    }
    printf("\n");
}