#include <bits/stdc++.h>

using namespace std;

int n, t; 

vector<int> cute; 

int main(){
  scanf("%d", &t);
  cout.flush(); 
  fflush(stdout); 

  for (int reee = 0; reee < t; reee++) {
    scanf("%d", &n);

    cout.flush(); 
    fflush(stdout); 

    int d = -1; 

    cute.clear(); 
    for (int i = 2; i < n + 1; i++) {
      cute.push_back(i); 
    }

    printf("%d %d %d ", 1, n - 1, 1); 
    for (int i = 0; i < cute.size(); i++) {
      printf("%d ", cute[i]); 
    }
    printf("\n"); 
    cout.flush(); 
    fflush(stdout); 

    scanf("%d", &d); 

    int hi = cute.size(); 
    int lo = 0; 

    while (lo < hi) { 
      int g = (lo + hi + 1) / 2; 
      printf("1 %d 1 ", g - lo); 
      for (int i = lo; i < g; i++) {
        printf("%d ", cute[i]); 
      }
      printf("\n"); 
      cout.flush(); 
      fflush(stdout); 

      int res; 
      scanf("%d", &res); 
      if (res == d) {
        hi = g - 1; 
      } else {
        lo = g; 
      }
      cout.flush(); 
      fflush(stdout); 

    }

    cout.flush(); 
    fflush(stdout); 

    vector<int> final_q; 

    for (int i = 1; i < n + 1; i++) {
      if (i != cute[lo]) {
        final_q.push_back(i); 
      }
    }

    printf("%d %d %d ", 1, n - 1, cute[lo]);
    for (int i = 0; i < final_q.size(); i++) {
      printf("%d ", final_q[i]); 
    }
    printf("\n"); 
    cout.flush(); 
    fflush(stdout); 
    // cout << "reeee"; 

    int ans = 0; 
    scanf("%d", &ans); 

    cout.flush(); 
    fflush(stdout); 
    printf("-1 %d\n", ans); 

    cout.flush(); 
    fflush(stdout); 
  }
  return 0;
}