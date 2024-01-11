#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "util.h"

void create_dim(list* l, size_t dims[3]);
void print_dim(size_t dims[3]);
size_t smallest_sa(size_t dims[3]);
size_t get_small_prem(size_t dims[3]);
size_t part_one(size_t dims[3]);

int main(void) {
	char* buffer = get_file_content("2.txt");
	if (buffer == NULL) {
		return 1;
	}
	size_t length = strlen(buffer);
	list* l = create_list();
	size_t sum_one = 0;
	size_t sum_two = 0;
	for (size_t i = 0; i < length; i++) {
		if (buffer[i] == '\n') {
			size_t dims[3];
			create_dim(l, dims);
			size_t volume = dims[0] * dims[1] * dims[2];
			size_t small_perm = get_small_prem(dims);
			size_t surface_areas[] = {
				dims[0] * dims[1],
				dims[1] * dims[2],
				dims[2] * dims[0]
			};
			sum_one += (
				(2 * surface_areas[0]) +
				(2 * surface_areas[1]) +
				(2 * surface_areas[2]) +
				smallest_sa(surface_areas)
			);
			destroy_list(l);
			l = create_list();
			if (l == NULL) {
				free(buffer);
				return 1;
			}
		} else {
			l = append(l, buffer[i]);
			if (l == NULL) {
				free(buffer);
				return 1;
			}
		}
	}
	destroy_list(l);
	free(buffer);
	printf("[PART ONE] SUM: %lu\n", sum_one);
	printf("[PART TWO] SUM: %lu\n", sum_one);
	return 0;
}

size_t smallest_sa(size_t dims[3]) {
	size_t small = dims[0];
	for (size_t i = 0; i < 3; i++) {
		if (dims[i] < small) {
			small = dims[i];
		}
	}
	return small;
}

void create_dim(list* l, size_t dims[3]) {
	size_t j = 0;
	for (size_t i = 0; i <= l->count; i++) {
		if (isdigit(l->content[i])) {
			if (i + 1 <= l->count && isdigit(l->content[i + 1])) {
				dims[j] = 10 * (l->content[i] - 48) + (l->content[i + 1] - 48);
				j++;
				i++;
			} else {
				dims[j] = l->content[i] - 48;
				j++;
			}
		} 
	}
}

size_t get_small_prem(size_t dims[3]) {
}

void print_dim(size_t dims[3]) {
	printf("[L] : %lu, [W] : %lu, [H] : %lu\n", dims[0], dims[1], dims[2]);
}
