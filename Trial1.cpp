/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;
char name[]="Memory";

int main()
{
int i=5;
//   // cout<<"Hello World";
//     for (i=5; i>=0; i--)
    // {
    //     cout<<name[i];
    //   cout<<"\n";
    // }
    i=5;
    while (i>=0)
    {
        if (name[i]=='e')
        {
        //cout<<name[i];
        cout<<"\n";
        
        
            cout<<"Found the E\n";
            //cout<<name[i];
            break;
        }
        i--;
    }
    return 0;
}



