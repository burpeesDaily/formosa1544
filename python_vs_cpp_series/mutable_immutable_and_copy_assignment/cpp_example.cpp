// Copyright © 2021 by Shun Huang. All rights reserved.
// Licensed under MIT License.
// See LICENSE in the project root for license information.


class MyClass
{
    public:
        int variable1 = 0;
        mutable int variable2 = 0;
};


void main()
{
    int nonConstVariable = 0; // Non-const object
    const int constVariable = 0; // Const object
    constexpr int secondsPerHour = 60 * 60; // Const expression

    const MyClass myClass; // Const object
    myClass.variable2 = 10; // Ok because variable2 is mutable
    myClass.variable1 = 10; // Error; myClass object is const
}
