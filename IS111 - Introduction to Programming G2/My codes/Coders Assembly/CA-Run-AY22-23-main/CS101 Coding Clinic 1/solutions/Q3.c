#include <stdio.h>

int main(void) {
    int input;
    int prev;

    int max_streak_length = 0;
    int max_streak_sum = 0;

    int curr_streak_length;
    int curr_streak_sum;

    printf("Enter n: ");
    scanf("%d", &input);

    if (input >= 0) {
        curr_streak_length = 1;
        curr_streak_sum = input;
        prev = input;
    }

    while (input >= 0) {
        printf("Enter n: ");
        scanf("%d", &input);

        if (input > prev) {
            curr_streak_length++;
            curr_streak_sum += input;
        } else {
            if (curr_streak_length > max_streak_length) {
                max_streak_length = curr_streak_length;
                max_streak_sum = curr_streak_sum;
            }

            curr_streak_length = 1;
            curr_streak_sum = input;
        }
        prev = input;
    }

    printf("Longest streak sum: %d\n", max_streak_sum);
}
