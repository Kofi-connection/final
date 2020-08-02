#include <stdio.h>
#include <stdlib.h>

int main(){
 char ch;
 char filename[128]= "FINALc/copies/FINALinstruction";
 char filename2[128]="FINALc/encrypted/FINALinstruction";
 FILE *fn;
 FILE *fw;
 int arr [3994];
 int key=150;
 int i=0;
 int j=0;
 int count=0;
 fn=fopen(filename,"r");
 
 while((ch = fgetc(fn)) != EOF){
     ch = ch + key;
     if (ch>256){
       ch=ch%256;
     }
     else if (ch<0) {
         ch = ch % 256;
     }
     key=key-1;
     arr[i]=ch;
     i=i+1;
    // count=count+1;
     fw =fopen(filename2, "w");
        for (j=0;j<3994;j++)
           fputc(arr[j],fw);
     fclose(fw);
}

 fclose(fn);
 
 return 0; 

}

