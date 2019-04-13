#include <bits/stdc++.h>

using namespace std;

long long int n, k; 

int main(){
  scanf("%lld %lld", &n, &k);
  int cute = n; 
  int twos = 0; 
  int fives = 0; 

  while (n % 5 == 0 || n % 2 == 0) {
    if (n % 2 == 0) { 
      twos++; 
      n /= 2; 
    } else if (n % 5 == 0) {
      fives++; 
      n /= 5; 
    }
  }
  n = cute;
  for (int i = 0; i < (k - twos); i++) {
    n *= 2; 
  }
  for (int i = 0; i < (k - fives); i++) {
    n *= 5; 
  }

  cout << n; 
  return 0; 
}