#include <stdio.h>

// V3: Using 1 array
void print_pascal(int num) {
    // Fully declare the size of the array until you want it to be 
    int current_array[num];
    current_array[0] = 1;
    int temp_prev;
    int temp_curr;

    // For each line
    for (int i = 1; i <= num; i++) {
        // Print out everything in current_array[]
        for (int j = 0; j < i; j++) {
            printf("%d ", current_array[j]);
        }
        printf("\n");
        // Get new current_array[] i.e. from i elements, get to i+1 elements
        temp_prev = current_array[0];
        for (int k = 1; k < i; k++) {
            temp_curr = current_array[k];
            current_array[k] += temp_prev;
            temp_prev = temp_curr;
        }
        current_array[i] = 1;
    }
}

int main(void) {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    print_pascal(n);
}