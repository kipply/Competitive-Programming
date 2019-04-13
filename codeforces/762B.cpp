#include <bits/stdc++.h>

using namespace std;

long long int a, b, c, m, ans, ansans; 
vector< pair<int, string> > mouses; 

int main(){
  scanf("%d %d %d", &a, &b, &c);
  char t[10]; 
  int cute; 
  scanf("%d", &m);
  for (int i = 0; i < m; i++) {
    scanf("%d %s", &cute, &t[0]); 
    mouses.push_back(pair<int, string>(cute, t)); 
  }

  sort(mouses.begin(), mouses.end());
  for (int i = 0; i < m; i++) {
    if (mouses[i].second == "USB" && a > 0) { 
      ans++; 
      ansans += mouses[i].first; 
      a -= 1; 
    } else if (mouses[i].second == "PS/2" && b > 0) {
      ans++; 
      ansans += mouses[i].first; 
      b -= 1; 
    } else if (c > 0){
      ans++; 
      ansans += mouses[i].first; 
      c -= 1; 
    }
  }
  printf("%lld %lld", ans, ansans); 
  return 0; 
}