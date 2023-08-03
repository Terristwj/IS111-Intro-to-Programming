#include <stdio.h>

// V1: Without arrays
void print_ascending_pairs(int n) {
    // Corner case
    if (n < 10) {
        printf("none\n");
        return;
    }

    int n_copy = n;
    int min = n_copy % 100;
    int max = min;

    n_copy /= 10;

    // Use n_copy to find min and max
    while (n_copy >= 10) {
        int new_pair = n_copy % 100;
        if (new_pair > max) {
            max = new_pair;
        } else if (new_pair < min) {
            min = new_pair;
        }
        n_copy /= 10;
    }

    // Start from printing smallest pair(min), then next smallest, stopping at largest pair(max)
    int to_print = min;
    while (to_print != max) {
        printf("%02d, ", to_print);
        n_copy = n;
        int next_to_print = max;

        while (n_copy >= 10) {
            int new_pair = n_copy % 100;
            if (new_pair < next_to_print && new_pair > to_print) {
                next_to_print = new_pair;
            }
            n_copy /= 10;
        }

        to_print = next_to_print;
    }

    // Fencepost
    printf("%02d\n", max);
}

int main(void) {
    print_ascending_pairs(1);
    print_ascending_pairs(709);
    print_ascending_pairs(12345);
}