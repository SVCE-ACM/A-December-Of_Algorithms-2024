//(24) String Permutation Grouping
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return strcmp(*(const char**)a, *(const char**)b);
}

void permute(char *s, int l, int r, char **result, int *index) {
    if (l == r) {
        result[*index] = (char*)malloc(strlen(s) + 1);
        strcpy(result[*index], s);
        (*index)++;
    } else {
        for (int i = l; i <= r; i++) {
            if (i != l && s[i] == s[l]) continue;
            char temp = s[l];
            s[l] = s[i];
            s[i] = temp;
            permute(s, l + 1, r, result, index);
            temp = s[l];
            s[l] = s[i];
            s[i] = temp;
        }
    }
}

int main() {
    char s[13];
    scanf("%s", s);
    
    int n = strlen(s);
    char *result[479001600]; 
    int index = 0;
    
    permute(s, 0, n - 1, result, &index);
    
    qsort(result, index, sizeof(char*), compare);
    
    for (int i = 0; i < index; i++) {
        printf("%s\n", result[i]);
    }

    return 0;
}

