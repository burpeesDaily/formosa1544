#include "MyLib.hpp"

#include <iostream>


int main()
{
    int a = 10;
    int b = 20;

    std::cout << a << " + " << b << " = " << MyLib::add(a, b) << std::endl;
    return 0;
}
