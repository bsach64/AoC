#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "util.h"

void modify_current_floor(char token, int* current_floor_ptr);
int part_one(char* buffer, size_t length);
size_t part_two(char* buffer, size_t length);

// '(' up one level
// ')' down one level

int main(void) {
	int current_floor = 0;
	char* buffer = get_file_content("1.txt");
	if (buffer == NULL) {
		return 1;
	}
	size_t length = strlen(buffer);
	printf("[Part ONE]: %i\n", part_one(buffer, length));
	printf("[Part TWO]: %lu\n", part_two(buffer, length));
	free(buffer);
}

int part_one(char* buffer, size_t length) {
	int current_floor = 0;
	for (int i = 0; i < length; i++) {
		modify_current_floor(buffer[i], &current_floor);
	}
	return current_floor;
}

size_t part_two(char* buffer, size_t length) {
	size_t position = 0;
	int current_floor = 0;
	for (int i = 0; i < length; i++) {
		position++;
		modify_current_floor(buffer[i], &current_floor);
		if (current_floor == -1) {
			return position;
		}
	}
	return position;
}

void modify_current_floor(char token, int* current_floor_ptr) {
	if (token == '(') {
		(*current_floor_ptr)++;
	} else if (token == ')') {
		(*current_floor_ptr)--;
	}
}
