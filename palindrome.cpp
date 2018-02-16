#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    cout<< "Enter the word \n";
    char word [20];
    cin>> word;
    int arraysize;
    arraysize=strlen(word);
    for (int i=0;i<arraysize;i++)
    {
        if (word[i]!=word[arraysize-(i+1)])
        {
            cout<<word;
            cout<<" Is not a palindrome\n";
            return 0;
        }
    }
    cout<<word;
    cout<<" Is a palindrome\n";

    return 0;
}

