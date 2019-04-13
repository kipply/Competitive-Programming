#include <bits/stdc++.h>

using namespace std;

long long int n, k, boxes[100001], hi;
long long int type, number; 

int main(){
  type = 1;
  scanf("%lld %lld", &n, &k);
  for (int i = 0; i < k; i++) {
    scanf("%lld", &boxes[i]);
    if ((n / boxes[i]) * boxes[i] > hi) {
      hi = (n / boxes[i]) * boxes[i]; 
      type = i + 1; 
      number = n / boxes[i]; 
    }
  }

  printf("%lld %lld", type, number);

  return 0;
}


