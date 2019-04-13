#include <bits/stdc++.h>

using namespace std;

long long int n, m, a, b; 

int main(){
  scanf("%lli %lli %lli %llu", &n, &m, &a, &b);

  printf("%llu", min((m - n % m) * a, (n % m) * b));
  return 0;
}