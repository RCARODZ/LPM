/*
LPM made in C
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define VERSION 0.1

// Find out how to create a logger in C

int main(int argc, char *argv[]){
    if(argc == 1){
        pintf("LPM - Local Password Manager V%d\n", VERSION);
        printf(" %s | -a [account] -p [password] /test");
    } else if(strcmp(argv[1], "/test")){
        // Enter testing environmnet
    }

    return 0;
}
