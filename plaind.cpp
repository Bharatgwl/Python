#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s;
    cin >> s;
    int i = 0, j = s.size() - 1;
    bool flag = false;
    while (i <= j)
    {
        if (s[i++] != s[j--])
        {
            cout << "not a palindrome";
            flag = true;
            break;
        }
    }
    if(!flag){
        cout<<"it is a palindrome";
    }
}