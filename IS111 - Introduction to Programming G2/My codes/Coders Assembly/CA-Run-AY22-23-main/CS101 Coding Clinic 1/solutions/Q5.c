#include <stdio.h>

int main(void) {
    int n;
    
    printf("Input the number of terms: ");
    scanf("%d", &n);

    double harmonic_sum = 0;

    for (int i = 1; i < n; i++) {
        printf("1/%d + ", i);
        harmonic_sum += 1.0 / i;
    }
    harmonic_sum += 1.0 / n;

    // Fencepost
    printf("1/%d = %.4lf\n", n, harmonic_sum);
}