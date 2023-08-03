#include <stdio.h>

// V2: With arrays
void bubble_sort(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - 1 - i; j++) {
            if (arr[j] > arr[j+1]) {
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }
}

void print_ascending_pairs(int n) {
    // Corner case
    if (n < 10) {
        printf("none\n");
        return;
    }

    // Get count of number pairs
    int count = 1;
    for (int i = 10; i * 10 <= n; i *= 10) {
        count++;
    }

    // Declare and initialise array of number pairs
    int pairs[count];
    for (int i = 0; i < count; i++) {
        pairs[i] = n % 100;
        n /= 10;
    }

    // Sort in ascending order
    bubble_sort(pairs, count);
    
    for (int i = 0; i < count - 1; i++) {
        printf("%02d, ", pairs[i]);
    }

    // Fencepost
    printf("%02d\n", pairs[count-1]);
}

int main(void) {
    print_ascending_pairs(1);
    print_ascending_pairs(709);
    print_ascending_pairs(12345);
}