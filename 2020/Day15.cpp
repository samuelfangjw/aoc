#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> v = {1,20,11,6,12,0}; // input
    unordered_map<int, int> um;

    int turn = 1;

    while (turn <= v.size()) {
        um[v[turn-1]] = turn;
        turn++;
    }

    int prev = 0;

    while (turn <= 30000000){

        if (turn == 2020) {
            cout << "Part 1: " << prev << '\n';
        }

        if(turn == 30000000) {
            cout << "Part 2: " << prev << '\n';
        }

        if (um.find(prev) == um.end()) {
            um[prev] = turn;
            prev = 0;
        } else {
            int diff = turn - um[prev];
            um[prev] = turn;
            prev = diff;
        }

        turn++;
    }
}