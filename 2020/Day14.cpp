#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

unordered_map<int, ll> um1;
unordered_map<ll, ll> um2;
vector<ll> Xmasks;
ll onesMask;
ll zerosMask;
ll xMask;

void addAddress(ll num, int pos, ll result) {
    if (pos == Xmasks.size()) {
        um2[num] = result;
        return ;
    }

    addAddress(num, pos + 1, result);
    addAddress(num + Xmasks[pos], pos + 1, result);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;

    while (getline(cin, s)) {
        replace(s.begin(), s.end(), '=', ' ');
        stringstream ss(s);

        string a, b;
        ss >> a >> b;

        if (!a.compare("mask")) {
            onesMask = 0;
            zerosMask = 0;
            xMask = 0;
            Xmasks.clear();

            int pos = 36;
            for (char c : b) {
                pos--;
                onesMask <<= 1;
                zerosMask <<= 1;
                xMask <<= 1;
                
                if (c == '1') {
                    onesMask++;
                }

                if (c != '0') {
                    zerosMask++;
                }

                if (c == 'X') {
                    Xmasks.push_back(1ll << pos);
                } else {
                    xMask++;   
                }
            }
        } else {
            a = regex_replace(a, regex("[^\\d]"), "");
            ll idx = stoi(a);
            ll number = stoi(b);

            // Part 1
            ll number1 =  number | onesMask;
            um1[idx] = number1 & zerosMask;

            // Part 2
            ll base = (idx | onesMask) & xMask; // value when X is all 0
            addAddress(base, 0, number);
        }
    }

    ll part1Result = 0;
    for (auto& it : um1) {
        part1Result += it.second;
    }

    ll part2Result = 0;
    for (auto& it : um2) {
        part2Result += it.second;
    }

    cout << "Part 1:\n";
    cout << part1Result << "\n\n";

    cout << "Part 2:\n";
    cout << part2Result << '\n';
}  