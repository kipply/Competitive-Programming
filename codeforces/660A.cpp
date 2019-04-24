#include <bits/stdc++.h>

using namespace std;

int n; 
int a[1001]; 
int ans; 
vector<int> cute; 

int gcd(int a, int b) { 
   if (b == 0) 
      return a; 
   return gcd(b, a % b);  
} 

int main(){
  scanf("%d", &n); 

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }

  for (int i = 0; i < n - 1; i++) {
    cute.push_back(a[i]);
    if (gcd(a[i], a[i + 1]) != 1) {
      cute.push_back(1);
      ans++; 
    }
  }
  cute.push_back(a[n - 1]);

  printf("%d\n", ans); 
  for (int i = 0; i < n + ans; i++) {
    printf("%d ", cute[i]);
  }
  return 0;
}
 