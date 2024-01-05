#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long t;
    cin>>t;
    while(t--)
    {
        long long n;
        cin>>n;
        long long c=0;
        while(n)
        {
            c+=(n);
            n>>=1;
        }
        cout<<c<<endl;
    }
}
