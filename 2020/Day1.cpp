#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll i;
    unordered_set<ll> us;
    vector<int> v;

    while (cin >> i) {
        if (us.find(2020 - i) != us.end()) {
            cout << "Part 1:\n";
            cout << i << ' ' << 2020-i << '\n';
            cout << i * (2020 - i) << "\n\n";
        }
        us.insert(i);
        v.push_back(i);
    }


    for (int j = 0; j < v.size(); j++) {
        for (int k = j+1; k < v.size(); k++) {
            if (us.find(2020 - v[j] - v[k]) != us.end()) {
                cout << "Part 2:\n";
                cout << v[j] << " " << v[k] << " " << 2020-v[j]-v[k] << '\n';
                cout << v[j] * v[k] * (2020 - v[j] - v[k]);
                return 0;
            }
        }
    }
}
