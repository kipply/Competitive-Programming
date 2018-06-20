#include <iostream>
#include <string>
#include <cstdint>
using namespace std;

int t;
double dorado;
int main(){
  scanf("%d", &t);
  for (int _ = 0; _ < t; _++){
    scanf("%lf", &dorado);
    double dordor = dorado / 2;
    int64_t i = *(int64_t *) &dorado; // cast dorado to int_64t?
    i = 0x5fe6eb50c7b537a9 - (i / 2); // what a kawaiiii number
    dorado = *(double *) &i;
    dorado = dorado * (1.5 - (dordor * dorado * dorado));
    dorado = dorado * (1.5 - (dordor * dorado * dorado));
    printf("%lf\n", dorado);
  }
}
