#ifndef UTIL_H_
#define UTIL_H_

#include <stdio.h>
#include <stdlib.h>

char* get_file_content(char* file_path);

char* get_file_content(char* file_path) {
	FILE *f = fopen(file_path, "r");
	if (f == NULL) return NULL;
	fseek(f, 0L, SEEK_END);
	size_t fsize = ftell(f);
	fseek(f, 0L, SEEK_SET);
	
	char *buffer = (char* )malloc(fsize);
	if (buffer == NULL) {
		return NULL;
	}
	fread(buffer, fsize, 1, f);
	return buffer;
}

#endif // !UTIL_H_
