#include <bits/stdc++.h>

using namespace std;

long long int x, y; 

int main(){
  scanf("%llu %llu", &x, &y);
  if (log(x) > log(y)) cout << "<"; 
  else if (log(y) > log(x)) cout << ">"; 
  else cout << "=";
}
