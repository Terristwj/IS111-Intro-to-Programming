#include <stdio.h>

int main(void) {
    int n;

    printf("Enter n: ");
    scanf("%d", &n);

    int i = 1;
    while (i * 10 < n) {
        i *= 10;
    }

    int sum = 0;
    while (i > 1) {
        sum += n / i;
        printf("%d + ", n / i);
        n %= i;
        i /= 10;
    }

    // Fencepost
    sum += n;
    printf("%d = %d\n", n, sum);
}