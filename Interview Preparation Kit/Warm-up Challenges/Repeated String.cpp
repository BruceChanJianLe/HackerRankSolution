#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {

    long int count_instring, count_total;
    count_instring = count_total = 0;

    if ((n % s.length()) == 0){
        for (int i = 0; i < s.length(); i++){
            if (s[i] == 'a'){
                count_instring += 1;
            }
        }
        count_total = (n / s.length()) * count_instring;
        
    }
    else{
        for (int i = 0; i < s.length(); i++){
            if (s[i] == 'a'){
                count_instring += 1;
            }
        }
        count_total = (n / s.length()) * count_instring;

        count_instring = 0;

        for (int i = 0; i < (n % s.length()); i++){
            if (s[i] == 'a'){
                count_total += 1;
            }
        }
    }
    return count_total;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
