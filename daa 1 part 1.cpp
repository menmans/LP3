/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;

int fibonacci(int n){
    
    if(n<=1){
        return n;
    }
    
    return fibonacci(n-1)+fibonacci(n-2);
}

int main(){
    
    int a;
    cout<<"Enter the Number:";
    cin>>a;
    
    cout<<"Fibonacci Series ----->"<<" ";
    for(int i = 0 ; i<a;i++){
        cout<<fibonacci(i)<<" ";
    }
}