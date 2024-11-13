/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;

int main(){
    int a=0,b=1;
    int c;
    int n;
    cout<<"Enter the Number:";
    cin>>n;
    
    cout<<"Fibonacci Series ----->"<<"  ";
    cout<<a<<" ";
    cout<<<<" ";
    
    
    for(int i = 0 ; i<n-2;i++){
        c=a+b;
        cout<<c<<" ";
        
        a=b;
        b=c;
    }
}