#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {

  FILE *fptr;

  fptr = fopen("day1_test.txt", "r");
  char line[100];

  int left_nums[20];
  int right_nums[20];


  int curr = 0 ;
  if (fptr != NULL) {
    // Read the content and print it
    while (fgets(line, 100, fptr)) {
      //printf("%s", line);
      char* split = strtok(line, " ");
      printf("LEFT: %s\n", split);
      while (split != NULL) {
          split = strtok(NULL, " ");
          printf("RIGHT: %s\n", split);
          if (split != NULL) {
              /*
              left_nums[curr] = atoi(split);
              right_nums[curr] = atoi(split);
              */
              curr++;
          }
      }
      exit(1);
    }
  } else {
    printf("NOT ABLE TO OPEN FILE");
  }

  fclose(fptr);

  return 0;
}
