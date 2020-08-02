#include <stdio.h>
#include <stdlib.h>


int main(){
 char filename2[128]= "FINALc/decrypted/FINALinstruction"; 
 char filename[128]= "FINALc/encrypted/FINALinstruction";
 FILE *fp =fopen(filename, "r");
 FILE *f; 
 int key=150;
 int arr[3994];
 int i=0;
 int j=0;
 if (fp == NULL){
    return 0;
 }
 do {
   char c = fgetc(fp);
   if (feof(fp)){
     break;
   }
   c=c-key;
   if (c>256){
     c= c % 256;
   }
   else if (c<0){
     c=c%256;
   }
   key=key-1;
   arr[i]=c;
   i=i+1;
  // printf("%c", c);
   f= fopen(filename2, "w");
      for (j=0; j<3994;j++)
         fputc(arr[j],f);
   fclose(f);
 }
 while(1);
 fclose(fp);
 return (0);
}
