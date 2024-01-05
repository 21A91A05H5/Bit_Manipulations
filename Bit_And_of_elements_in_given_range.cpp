/*
n numbers
a array
q queries
 -> l and r range values
 ->print '&' all values in that range [l,r]
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int x,i,n;
	cin>>n;
	int a[n],res[n][32];
	for(i=0;i<n;i++){
	    cin>>a[i];
	}
	for(int i=31;i>=0;i--)
	{
		for(int j=0;j<n;j++)
		{
			if(a[j]&(1<<i)) res[j][i]=1;
			else res[j][i]=0;
		}
	}
	for(int i=31;i>=0;i--)
	{
		for(int j=1;j<n;j++)
		{
			res[j][i]+=res[j-1][i];
		}
	}
	int q;
	cin>>q;
	while(q--)
	{
		int l,r,x=0,result;
		cin>>l>>r;
		int di=r-l;
		if(l==0)
		{
			for(int i=0;i<32;i++)
			{
				if((res[r][i]-res[l][i])%2==1)
				{
					x=x|(1<<i);
				}
			}
		}
		else
		{
			for(int i=0;i<32;i++)
			{
				if((res[r][i]-res[l-1][i])%2==1)
				{
					x=x|(1<<i);
				}
			}
		}
		cout<<x<<endl;
	}
}
