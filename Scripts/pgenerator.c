/*
LPM made in C

To Do:
Needs to add logger info to the current logger but for testing its going to write on
another logger.

need to come up with an algorithm to generate passwords.
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
// #include <argp.h> for defining arguments, it cant be found.

//#define VERSION 
//Define Time
size_t time;
struct tm *timestamp;


// Find out how to create a logger in C
// handling arguments in C

void logger(int code, char* buffer);

int main(int argc, char *argv[]){
    if(argc == 1){
        pintf("LPM - Local Password Manager V%d\n", VERSION);
        printf(" %s | -a [account] -p [password] /test");
    } else if(strcmp(argv[1], "/test")){
        // Enter testing environmnet
    }

    return 0;
}

//code to determine warning, error or info and the buffer is the string with the message.
void logger(int code, char* buffer){
    //Define code
    FILE *logfile;
    if(code == 0)   //Error
    {
        fopen("pgeneratorclog.log", "a+");
        
    }
}