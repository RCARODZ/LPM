/*
LPM made in C

To Do:
Needs to add logger info to the current logger but for testing its going to write on
another logger.

need to come up with an algorithm to generate passwords.

Find out how to create a logger in C

handling arguments in C
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
// #include <argp.h> for defining arguments, it cant be found.
#define VERSION 0.1
#ifdef _WIN32   //Code for windows computer
int main(){
    printf("Windows Version");
    return 0;
}
#endif  //End windows version

#ifdef __APPLE__    // C code for apple computer

//Define Time
size_t t;
struct tm *timestamp;

//Functions
void logger(int code, char* buffer);
char* generator(char* username, char* password);   // Generate Password


int main(int argc, char *argv[]){
    if(argc == 1){
        printf("LPM - Local Password Manager V:%f\n", VERSION);
        printf(" %s | -a [account] -p [password] /test");
    } else if(strcmp(argv[1], "/test")){
        // Enter testing environmnet
    } else if(strcmp(argv[1], "-a")){
        printf("entered account...\n");
        printf("%s\n", argv[1]);
    }

    return 0;
}

//code to determine warning, error or info and the buffer is the string with the message.
void logger(int code, char* message){
    //Define code
    FILE *logfile;
    char* mesg;
    if(code == 0)   //Error
    {
        mesg = strcat("[ERROR]:", message);
        fopen("pgeneratorclog.log", "a+");
        
    }  
    if(code == 1)   //Warning
    {

    }
    if(code == 2)   //Info
    {

    }
}

char* generator(char* username, char* password){
    //Generate the password using inputs

}

#endif  //End Appleversion
