#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

int p1Count = 0;
int p2Count = 0;
vector<bool> v1(26, false);
vector<bool> v2(26, true);

void solve() {
    for (auto i : v1) {
        if (i) {
            p1Count++;
        }
    }

    for (auto i : v2) {
        if (i) {
            p2Count++;
        }
    }

    v1.assign(26, false);
    v2.assign(26, true);
}

void insert(string s) {
    vector<bool> v3(26, false);

    for (char c : s) {
        v1[c-'a'] = true;
        v3[c-'a'] = true;
    }


    for (int i = 0; i < 26;i++) {
        v2[i] = v2[i] & v3[i];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    
    while (getline(cin, s)) {
        if (s.empty()) {
            solve();
            s = "";
        } else {
            insert(s);
        }
    }

    solve();

    cout << "Part 1:\n";
    cout << p1Count << "\n\n";
    cout << "Part 2:\n";
    cout << p2Count << '\n';
}