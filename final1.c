 
//#include <iostream> 
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>



const char* path="FINALc";
int main(void){
//  mkdir(path,0777);  
//  mkdir("FINALc/copies",0777);
//  mkdir("FINALc/encrypted",0777);
//  mkdir("FINALc/decrypted",0777);
    FILE *source;
    FILE *target;
    source= fopen("final1.c", "r");
    target=fopen("FINALc/final1.c", "w");
    char c;
    while ( (c=fgetc(source)) != EOF) {
        fputc(c, target);

    }
    printf("Sucess!\n");
        
    
}
