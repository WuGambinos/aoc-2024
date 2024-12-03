#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* read_file_to_string(char* filename) {
    FILE* file;
    char* content;
    long file_size;

    // Open the file in read mode
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    // Move the file pointer to the end to get the size of the file
    fseek(file, 0, SEEK_END);
    file_size = ftell(file);
    fseek(file, 0, SEEK_SET);  // Reset the file pointer to the beginning

    // Allocate memory for the content string
    content = (char*) malloc(file_size + 1);  // +1 for null terminator
    if (content == NULL) {
        printf("Memory allocation failed\n");
        fclose(file);
        return 1;
    }

    // Read the contents of the file into the string
    fread(content, 1, file_size, file);
    content[file_size] = '\0';  // Null terminate the string
    fclose(file);

    return content;
}

int parse_memory(char* s, bool day2) {
    char first_num[4] = "";
    char second_num[4] = "";
    char mul_sub[4];
    char do_sub[5];
    char dont_sub[8];
    int res = 0;
    int state = 0;
    int i = 0;
    int len = strlen(s);
    bool enabled = true;

    while (i < len) {
        memset(mul_sub, 0, 4);
        strncpy(mul_sub, &s[i], 3);
        mul_sub[3] = '\0';

        if (day2) {
            strncpy(do_sub, &s[i], 4);
            strncpy(dont_sub, &s[i], 7);
            do_sub[4] = '\0';
            dont_sub[7] = '\0';

            if (strcmp(do_sub, "do()") == 0) {
                enabled = true;
            } else if (strcmp(dont_sub, "don't()") == 0) {
                enabled = false;
            }
        }

        if (strncmp(mul_sub, "mul", 3) == 0) {
            state = 1;
            i += 3;
        } else if (state == 1 && s[i] == '(') {
            state = 2;
            i += 1;
        } else if (state == 2) {
            state = 3;
            int num_idx = 0;
            while (isdigit(s[i])) {
                first_num[num_idx] = s[i];
                num_idx += 1;
                i += 1;
            }
        }

        else if (state == 3 && s[i] == ',') {
            state = 4;
            i += 1;
        } else if (state == 4) {
            state = 5;
            int num_idx = 0;
            while (isdigit(s[i])) {
                second_num[num_idx] = s[i];
                num_idx += 1;
                i += 1;
            }
        } else if (state == 5 && s[i] == ')') {
            if (strcmp(first_num, "") != 0 && strcmp(second_num, "") != 0 &&
                enabled) {
                // printf("FIRST NUM: %s\n", first_num);
                // printf("SECOND NUM: %s\n\n", second_num);

                res += atoi(first_num) * atoi(second_num);
            }
            i += 1;

            memset(first_num, 0, 4);
            memset(second_num, 0, 4);

        } else {
            memset(first_num, 0, 4);
            memset(second_num, 0, 4);
            state = 0;
            i += 1;
        }
    }
    if (day2) {
        printf("DAY 2: %d\n", res);
    } else {
        printf("DAY 1: %d\n", res);
    }
    return res;
}

int main() {
    int total = 0;
    char* input = read_file_to_string("day3.txt");
    printf("File input:\n%s\n", input);
    parse_memory(input, false);
    parse_memory(input, true);
    free(input);

    return 0;
}