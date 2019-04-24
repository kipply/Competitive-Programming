#include <bits/stdc++.h>

using namespace std;

unsigned long long int n, m, k; 

int gcd(int a, int b) { 
   if (b == 0) return a; 
   return gcd(b, a % b);  
} 

int main(){
  scanf("%lld %lld %lld", &n, &m, &k); 
  unsigned long long int og_k = k; 
  if((2 * n * m) % k){
    cout << "NO" << endl;
    return 0;
  }

  if (k % 2 == 0) {
    k /= 2;
  }     
  
  int cute = gcd(n, k);
  k /= cute; 
  int a = n / cute;
    
  cute = gcd(m, k);
  k /= cute;
  int b = m / cute;
    
  
  if (og_k % 2) {
    if (a < n){
      a += a;
    }
    else {
      b += b;
    }
  }
  
  cout << "YES" << endl;
  cout << "0 0" << endl;
  cout << 0 << ' ' << b << endl;
  cout << a << ' ' << 0 << endl;

  return 0;
}
 