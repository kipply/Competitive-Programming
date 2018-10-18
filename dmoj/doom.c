// GIB POINTS

#include <inttypes.h>
int t;
double dorado;
int main(){
  printf("%.24g\n", dorado);
  scanf("%d", &t);
  for (int _ = 0; _ < t; _++){
    scanf("%lf", &dorado);
    double dordor = dorado / 2;
    int64_t i = *(int64_t *) &dorado; // cast dorado?
    i = 0x5FE6EB50C7B537A9 - (i >> 1); // what a kawaiiii number
    dorado = *(double *) &i;
    dorado = dorado * (1.5 - (dordor * dorado * dorado));
    dorado = dorado * (1.5 - (dordor * dorado * dorado));
    dorado = dorado * (1.5 - (dordor * dorado * dorado));
    dorado = dorado * (1.5 - (dordor * dorado * dorado));
    dorado = dorado * (1.5 - (dordor * dorado * dorado));
    printf("%.24g\n", dorado);
  }
}
