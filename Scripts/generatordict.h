/*
Define functionality for pgenerator
*/

typedef struct Account{
    int id;             //identification number for the account
    char *name;         //account name
    char *username;     //username
    char *password;     //account password
}Account, *PAccount;

typedef struct LPM{
    Account acc;
    char *porcID;
    char *time;
}LPM, *PLPM;

void *generate(char *uname, char *acc, char *pass);

void definetime();



