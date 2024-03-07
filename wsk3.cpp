#include <bits/stdc++.h>

int f(int a, int &b)
{
    b = b * 3;
    return a * 2;
}
void print(const int arr[], int n)
{
    for (int i = 0; i < n; i++)
        std::cout << *(arr + i) << " ";
    std::cout << std::endl;
}
int main()
{
    int arr[5] = {5, 2, 6, 8, 9};
    print(arr, 5);

    std::cout << std::endl;
    std::cout << *arr << std::endl;
    std::cout << *(arr + 1) << std::endl;

    std::sort(arr, arr + 5);
    print(arr, 5);

    int a = 3, b = 4;
    std::cout << f(a, b) << std::endl;
    std::cout << b;
}
