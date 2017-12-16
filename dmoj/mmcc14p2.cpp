#include "bits/stdc++.h"
using namespace std;
int cactus[10005], vals[2005], n, m, q, a, b;
long long g[2005][6005];
string t;

int find(int x, int y, int lo, int hi){
    int mid, res = -1;
    while(lo < hi + 1) {
        mid = (lo + hi) >> 1;
        if (g[x][mid] == g[y][mid]) {
            lo = mid + 1;
            res = mid;
        } else
            hi = mid - 1;
    }
    return res;
}

void build(int l, int r, int idx = 1){
    if(l == r) {
        cactus[idx] = m - 1;
        return;
    }
    int mid = (l + r) >> 1;

    build(l, mid, idx << 1);
    build(mid + 1, r, (idx << 1) + 1);

    cactus[idx] = find(vals[l], vals[r], 0, min(cactus[idx << 1], cactus[(idx << 1) + 1]));
}

void update(int st, int en, int x, int idx = 1) {
    if (st == en) return;
    int mid = (st + en) >> 1;
    if (x < mid + 1) update(st, mid, x, idx << 1);
    else update(mid + 1, en, x, (idx << 1) + 1);

    int mini = min(cactus[idx << 1], cactus[(idx << 1) + 1]);
    cactus[idx] = find(vals[st], vals[en], 0, mini);
}

int query(int st, int en, int l, int r, int idx){
    if(st > r || en < l) return -2;
    if(st >= l && en <= r) return cactus[idx];

    int mid = (st + en) >> 1;
    int ll = query(st, mid, l, r, idx << 1);
    int rr = query(mid + 1, en, l, r, (idx << 1) + 1);

    if(ll == -2) return rr;
    else if(rr == -2) return ll;
    return find(vals[max(l, st)], vals[min(r, en)], 0, min(ll, rr));
}

void kawaiiCactus(string a, int idx){
    long long curr = 1;
    for(int i = 0; i < m; i++){
        curr = curr * 31 + (long long) (a[i] - '0');
        g[idx][i] = curr;
    }
}

int main(){
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++){
        cin >> t;
        kawaiiCactus(t, i + 1);
        vals[i + 1] = i + 1;
    }
    build(1, n);
    scanf("%d", &q);
    for(; q--;) {
        scanf("%d %d", &a, &b);
        cout << ((query(1, n, a, b, 1) + 1) * (b - a + 1)) << "\n";
        swap(vals[a], vals[b]);
        update(1, n, b);
        update(1, n, a);
    }
    return 0;
}
