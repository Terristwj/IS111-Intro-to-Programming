#include <stdio.h>

// V2: Using 2 arrays
void print_pascal(int num) {
    // Fully declare the size of the array at the final iteration 
    int current_array[num];
    current_array[0] = 1;

    int next_array[num];
    next_array[0] = 1;
    next_array[1] = 1;
    
    // For each line
    for (int i = 1; i <= num; i++) {
        // Print out everything in current_array[]
        for (int j = 0; j < i; j++) {
            printf("%d ", current_array[j]);
        }
        printf("\n");

        // Copy over next_array[] to current_array[]
        for (int k = 0; k <= i + 1; k++) {
            current_array[k] = next_array[k];
        }

        // Use current_array[] to get new next_array[]
        for (int l = 0; l < i; l++) {
            next_array[l + 1] = current_array[l] + current_array[l + 1];
        }
        next_array[i + 1] = current_array[i];
    }
}

int main(void) {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    print_pascal(n);
}