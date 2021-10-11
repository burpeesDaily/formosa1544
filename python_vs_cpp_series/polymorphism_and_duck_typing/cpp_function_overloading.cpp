// Copyright © 2021 by Shun Huang. All rights reserved.
// Licensed under MIT License.
// See LICENSE in the project root for license information.

#include <string>


void myOverloadingFunction(int parameter)
{
    // Do something
}


void myOverloadingFunction(std::string parameter)
{
    // Do something
}


void myOverloadingFunction(int parameter1, std::string parameter2, float parameter3)
{
    // Do something
}
