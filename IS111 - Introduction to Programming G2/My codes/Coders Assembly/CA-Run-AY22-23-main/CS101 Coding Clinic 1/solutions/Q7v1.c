#include <stdio.h>

// V1: Using mathematical formula
int n_choose_k(int n, int k) {
    int pdt = 1;
    for (int i = k + 1; i <= n; i++) {
        pdt *= i;
    }
    for (int j = 1; j <= n - k; j++) {
        pdt /= j;
    }
    return pdt;
}

void print_pascal(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            printf("%d ", n_choose_k(i, j));
        }
        printf("\n");
    }
}

int main(void) {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    print_pascal(n);
}