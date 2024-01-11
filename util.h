#ifndef UTIL_H_
#define UTIL_H_

#define INTIAL_SIZE 5
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
	int count;
	size_t size;
	char* content;
} list;


char* get_file_content(char* file_path);
list* create_list();
list* append(list* l, char data);
void print_list(list *l);
void destroy_list(list *l);

list* create_list() {
	list* l = (list*) malloc(sizeof(list));
	if (l == NULL) return NULL;
	l->count = -1;
	l->size = 0;
	l->content = NULL;
	return l;
}


list* append(list* l, char data) {
	if (l == NULL) {
		l = create_list();
		if (l == NULL) {
			return NULL;
		}
	}
	if (l->size == 0) {
		l->content = (char*) malloc(sizeof(char) * INTIAL_SIZE);
		if (l->content == NULL) {
			free(l);
			return NULL;
		}
		l->size = INTIAL_SIZE;
		l->count++;
		l->content[l->count] = data;
		return l;
	}
	if (l->count + 1 == l->size) {
		size_t new_size = l->size * 2;
		char* new_content = (char*) realloc(l->content, sizeof(char) * new_size);
		if (new_content == NULL) {
			free(l);
			return NULL;
		}
		l->size = new_size;
		l->content = new_content;
		l->count++;
		l->content[l->count] = data;
		return l;
	}
	l->count++;
	l->content[l->count] = data;
	return l;
}

void print_list(list* l) {
	if (l == NULL) return;
	if (l->count < 0) return;
	for (size_t i = 0; i <= l->count; i++) {
		printf("%c", l->content[i]);
	}
}


void destroy_list(list* l) {
	free(l->content);
	free(l);
}


char* get_file_content(char* file_path) {
	FILE *f = fopen(file_path, "r");
	if (f == NULL) return NULL;
	fseek(f, 0L, SEEK_END);
	size_t fsize = ftell(f);
	fseek(f, 0L, SEEK_SET);
	
	char *buffer = (char* )malloc(fsize + 1);
	if (buffer == NULL) {
		return NULL;
	}
	fread(buffer, fsize, 1, f);
	buffer[fsize] = '\0';
	fclose(f);
	return buffer;
}

#endif // !UTIL_H_
