#include <bits/stdc++.h>

using namespace std;

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {
    // Set max sum as the lowest posible
    int max_sum = -9 * 7;
    
    // Loop at the ceter of the hour glass
    for (int i = 1; i < (arr.size() - 1); i++)
    {
        for (int j = 1; j < (arr.size() - 1); j++)
        {
            int current_sum = 0;
            current_sum += arr[i - 1][j - 1];
            current_sum += arr[i - 1][j];
            current_sum += arr[i - 1][j + 1];
            current_sum += arr[i][j];
            current_sum += arr[i + 1][j - 1];
            current_sum += arr[i + 1][j];
            current_sum += arr[i + 1][j + 1];
            if(current_sum > max_sum)
            {
                max_sum = current_sum;
            }
            
        }
    }
    return max_sum; 
    


}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
