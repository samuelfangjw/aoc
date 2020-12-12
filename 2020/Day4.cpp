#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

ll p1Result = 0;
ll p2Result = 0;

void solve(string p) {
    vector<string> keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

    for (string s : keys) {
        if (!regex_search(p, regex(s))) {
            return ;
        }
    }

    p1Result++;

    replace(p.begin(), p.end(), ':', ' ');
    stringstream ss(p);
    regex onlyDigits("[^\\d]");

    string key, value, s;
    while(ss >> key) {
        ss >> value;

        // byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if (key.compare("byr") == 0) {
            if (regex_search(value, onlyDigits)) {
                return ;
            }

            int i = stoi(value);
            if (i < 1920 || i > 2002) {
                return ;
            }
        }

        // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if (key.compare("iyr") == 0) {
            if (regex_search(value, onlyDigits)) {
                return ;
            }

            int i = stoi(value);
            if (i < 2010 || i > 2020) {
                return ;
            }
        }

        // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if (key.compare("eyr") == 0) {
            if (regex_search(value, onlyDigits)) {
                return ;
            }

            int i = stoi(value);
            if (i < 2020 || i > 2030) {
                return ;
            }
        }

        // hgt (Height) - a number followed by either cm or in:
        // If cm, the number must be at least 150 and at most 193.
        // If in, the number must be at least 59 and at most 76.

        if (key.compare("hgt") == 0) {
            smatch match;
            if (!regex_match(value, match, regex("([\\d]+)(cm|in)"))) {
                return ;
            }
            
            if (match[2].compare("cm") == 0) {
                int i = stoi(match[1]);
                if (i < 150 || i >  193) {
                    return ;
                }
            } else {
                int i = stoi(match[1]);
                if (i < 59 || i >  76) {
                    return ;
                }
            }
        }

        // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if (key.compare("hcl") == 0) {
            if (!regex_match(value, regex("#([0-9]|[a-f])+"))) {
                return ;
            }

            if (value.length() != 7){
                return ;
            }
        }

        // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if (key.compare("ecl") == 0) {
            if (!regex_match(value, regex("amb|blu|brn|gry|grn|hzl|oth"))) {
                return ;
            }
        }

        // pid (Passport ID) - a nine-digit number, including leading zeroes.
        if (key.compare("pid") == 0) {
            if (regex_match(value, onlyDigits)) {
                return ;
            }

            if (value.length() != 9) {
                return ;
            }
        }

        // cid (Country ID) - ignored, missing or not.
    }

    p2Result++;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    string pass = "";

    while (getline(cin, s)) {
        // empty line reached, process passport
        if (s.empty()) {
            solve(pass);
            pass = "";
        } else {
            s += " ";
            pass += s;
        }
    }

    solve(pass);

    cout << "Part 1:\n" << p1Result << "\n\n";
    cout << "Part 2:\n" << p2Result;
}