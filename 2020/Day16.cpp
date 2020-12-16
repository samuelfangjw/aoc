#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<bool> valid(1000, false);
    vector<vector<bool>> fields(20, vector<bool>(1000, false));

    string s;
    int fieldNo = 0;
    while (getline(cin, s) && !s.empty()) {
        s = regex_replace(s, regex("[^\\d]"), " ");
        stringstream ss(s);

        int two = 2;
        while (two--) {
            int a, b;
            ss >> a >> b;
            while (a <= b) {
                valid[a] = true;
                fields[fieldNo][a] = true;
                a++;
            }
        }

        fieldNo++;
    }

    getline(cin, s);
    getline(cin, s);
    replace(s.begin(), s.end(), ',', ' ');
    stringstream ss(s);

    vector<ll> myTicket(20);
    for (int i = 0; i < 20; i++) {
        ss >> myTicket[i];
    }

    getline(cin, s);
    getline(cin, s);

    ll part1 = 0;
    ll part2 = 1;

    vector<pair<int, int>> possibleCount(20);
    vector<vector<bool>> possibleFields(20, vector<bool>(20, true));

    for (int i = 0; i < 20; i++) {
        possibleCount[i] = {20, i};
    }

    while (getline(cin, s)) {
        replace(s.begin(), s.end(), ',', ' ');
        stringstream ss(s);
        vector<ll> ticketValues;

        bool discard = false;
        ll token;
        while (ss >> token) {
            ticketValues.push_back(token);
            if (!valid[token]) {
                discard = true;
                part1 += token;
            }
        }

        if (!discard) {
            for (int i = 0; i < 20; i++) {
                for (int j = 0; j < 20; j++) {
                    if (!fields[j][ticketValues[i]]) {
                        possibleFields[j][i] = false;
                        possibleCount[j].first--;
                    }
                }
            }
        }
    }

    sort(possibleCount.begin(), possibleCount.end());
    
    vector<bool> confirmedFields(20, false);

    for (auto p : possibleCount)  {
        int nextIdx = p.second;

        for (int i = 0; i < 20; i++) {
            if (!confirmedFields[i] && possibleFields[nextIdx][i]) {
                confirmedFields[i] = true;
                if (nextIdx < 6) {
                    part2 *= myTicket[i];
                }
                break;
            }
        }
    }

    cout << "Part 1: " << part1 << '\n';
    cout << "Part 2: " << part2 << '\n';
}