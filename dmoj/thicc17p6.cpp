#include "bits/stdc++.h"
using namespace std;

int N, T, A, B, C, S;
vector< pair<int, int> > G[200001];
int V[200001], R[200001];

pair<int, int> DFS(int X, int D, int P){
    R[X] = max(R[X], D);
    if (V[X] == 1 && P)
        return make_pair(D, X);
    pair<int, int> M;
    for (auto i: G[X])
        if (i.first != P)
            M = max(M, DFS(i.first, D + i.second, X));
    return M;
}

int main(){
    scanf("%d%d", &N, &T);
    for (int i = 0; i < N - 1; i++){
        scanf("%d%d%d", &A, &B, &C);
        G[A].push_back(make_pair(B, C));
        G[B].push_back(make_pair(A, C));
        V[A]++, V[B]++, S += 2 * C;
    }
    DFS(DFS(DFS(1, 0, 0).second, 0, 0).second, 0, 0);
    for (int i = 1; i <= N; i++)
        if (V[i] == T)
            printf("%d %d\n", i, S - R[i]);
}