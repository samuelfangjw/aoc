#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> v;
    string s;

    while(cin >> s) {
        v.push_back(s);
    }

    vector<int> dirX = {3, 1, 5, 7, 1};
    vector<int> dirY = {1, 1, 1, 1, 2};

    ll result = 1;

    for (int i = 0; i < dirX.size(); i++) {
        ll r = 0;
        ll d = 0;
        ll count = 0;

        while(d < v.size()) {
            if (v[d][r % v[0].length()] == '#') {
                count++;
            }
            r += dirX[i];
            d += dirY[i];
        }

        if (i == 0) {
            cout << "Part 1:\n";
            cout << count << "\n\n"; 
        }

        result *= count;
    }

    cout << "Part 2:\n";
    cout << result;
}