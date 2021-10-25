// Copyright © 2021 by Shun Huang. All rights reserved.
// Licensed under MIT License.
// See LICENSE in the project root for license information.

#include <iostream>


int global_variable = 0; // global variable

int myFunction(int parameter=0)
{
    int local_variable = 0; // local variable can only be accessed within block.

    if (parameter > 0)
    {
        local_variable += parameter;
    }
    else
    {
        local_variable += global_variable; // global variable can be accessed everywhere
    }

    global_variable = local_variable; // update the global variable within a function

    return local_variable;
}

double myFunction2()
{
    // local variable but has the same name as the global_variable.
    // In this case, the local one takes higher priority.
    double global_variable = 1.23;
    return global_variable;
}

void main()
{
    std::cout << global_variable << std::endl;
    // 0     The global global_variable
    std::cout << myFunction(10) << std::endl;
    // 10    The local_variable
    std::cout << global_variable << std::endl;
    // 10    The global global_variable updated by myFunction()
    std::cout << myFunction2() << std::endl;
    // 1.23  The local global_variable inside myFunction2()
    std::cout << global_variable << std::endl;
    // 10    The global global_variable was not affected by myFunction2()
}
