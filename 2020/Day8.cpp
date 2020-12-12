#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> vals;
    vector<string> commands;
    string s;
    string i;
    
    while(cin >> s) {
        cin >> i;
        commands.push_back(s);
        vals.push_back(stoi(i));
    }  

    // Part 1
    int j = 0;
    ll part1Acc = 0;
    vector<bool> visited1(vals.size(), false);

    while (true) {
        if (visited1[j]) {
            break;
        }

        visited1[j] = true;

        if (commands[j].compare("acc") == 0) {
            part1Acc += vals[j];
        }

        if (commands[j].compare("jmp") == 0) {
            j += (vals[j] - 1);
        }

        j++;
    }

    cout << "Part 1:\n";
    cout << part1Acc << "\n\n";

    // Part 2: Brute Force :)
    cout << "Part 2:\n";
    for (int k = 0; k < vals.size(); k++) {
        vector<bool> visited(vals.size(), false);
        int part2Acc = 0;

        if (commands[k].compare("nop") == 0) {
            commands[k] = "jmp";
            bool res = true;

            for (int j = 0; j < vals.size(); j++) {
                if (visited[j]) {
                    res = false;
                    break;
                }
                if (commands[j].compare("acc") == 0) {
                    part2Acc += vals[j];
                } else if (commands[j].compare("jmp") == 0) {
                    j += vals[j];
                    j--;
                } else {
                    continue;
                }

                visited[j] = true;
            }

            if (res) {
                cout << part2Acc;
            }

            commands[k] = "nop";

        } else if (commands[k].compare("jmp") == 0) {
            commands[k] = "nop";
            bool res = true;

            for (int j = 0; j < vals.size(); j++) {
                if (visited[j]) {
                    res = false;
                    break;
                }
                if (commands[j].compare("acc") == 0) {
                    part2Acc += vals[j];
                } else if (commands[j].compare("jmp") == 0) {
                    j += vals[j];
                    j--;
                } else {
                    continue;
                }

                visited[j] = true;
            }

            if (res) {
                cout << part2Acc;
            }

            commands[k] = "jmp";
        }
    }
}