#include <bits/stdc++.h>
using namespace std;

int main() {

    int g, p;
    set <int> gates;

    scanf("%d", &g);
    scanf("%d", &p);

    for (int i = 1; i <= g; i++)
        gates.insert(i);
    bool f = true;
    int plane, ans = 0;
    set<int>::iterator gate;
    for (int i = 0; i < p; i++){
        scanf("%d", &plane);
        gate = gates.upper_bound(plane);
        if (gate != gates.begin() && f){
            gates.erase(--gate);
            ans++;
        }
        else
            f = false;
    }
    cout << ans;
}
