# include <stdio.h>


int main(int argc, char *argv[]){
 
  if (argc==3)
    printf("The argument supplied is %s\n", argv[0]);
  else if (argc>3)
    printf("There are too many arguments\n");
  
  printf("You had %d number of arguments\n", argc);

}

