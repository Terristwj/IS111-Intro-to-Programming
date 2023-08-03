#include <stdio.h>

void swap_values_apart(int arr[], int size, int n) {
    int temp;
    for (int i = 0; i + n < size; i++) {
        temp = arr[i];
        arr[i] = arr[i+n];
        arr[i+n] = temp;
    }
}

void print_array(int arr[], int size) {
    if (size < 1) {
        return;
    }

    printf("[");
    for (int i = 0; i < size - 1; i++) {
        printf("%d, ", arr[i]);
    }
    printf("%d]\n", arr[size-1]);
}

int main(void) {
    {
        int arr[6] = {4, 12, 6, 13, 1, 0};
        int n = 3;
        int size = sizeof(arr)/sizeof(int);
        swap_values_apart(arr, size, n);
        print_array(arr, size);
    }
        
    {
        int arr[5] = {5, 2, 8, 9, 10};
        int n = 4;
        int size = sizeof(arr)/sizeof(int);
        swap_values_apart(arr, size, n);
        print_array(arr, size);
    }

    {
        int arr[3] = {3, 1, -3};
        int n = 5;
        int size = sizeof(arr)/sizeof(int);
        swap_values_apart(arr, size, n);
        print_array(arr, size);
    }
}