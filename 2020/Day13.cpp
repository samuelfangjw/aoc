#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int depart;
    cin >> depart;

    string s;
    cin >> s;

    replace(s.begin(), s.end(), ',', ' ');
    stringstream ss(s);

    string token;
    vector<int> buses;
    ll product = 1;

    while (ss >> token) {
        if (token.compare("x") == 0) {
            buses.push_back(0); // using 0 to represent x
            continue;
        }

        int next = stoi(token);
        buses.push_back(next);
        product *= next;
    }

    // Part 1
    int smallest = INT32_MAX;
    int busID = -1;
    for (int bus : buses) {
        if (bus == 0) {
            continue;
        }
        int waiting = (bus - (depart % bus)) % bus;
        if (waiting < smallest) {
            smallest = waiting;
            busID = bus;
        }
    }

    cout << "Part 1:\n";
    cout << busID * smallest << "\n\n";

    //Part 2
    ll earliest = 0;

    for (int i = 0; i < buses.size(); i++) {
        int busNo = buses[i];
        if (busNo == 0) {
            continue;
        }

        ll initial = product / busNo;
        ll target = ((busNo - (i % busNo)) % busNo);
        int j = 0;

        while (++j) {
            if ((initial * j) % busNo == target) {
                break;
            }
        }

        earliest += (initial * j);
        earliest %= product;
    }

    cout << "Part 2:\n";
    cout << earliest << '\n';
}