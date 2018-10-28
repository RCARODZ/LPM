#include <sys/socket.h>
#include <stdio.h>

struct somestruct{
    char next;
    int test:4;
    int test2:12;
} __packeds;

int main(int argc, char *argv[]){
    printf("working...\n");
    struct somestruct t;
    printf("%d\n", t.test2);
    return 0;
}