// Copyright © 2021 by Shun Huang. All rights reserved.
// Licensed under MIT License.
// See LICENSE in the project root for license information.


class MyInterface
{
    // Since this class contains a pure virtual class; it becomes an abstract
    // class, and cannot be instantiated.
    public:
        // Use a pure virtual function to define an interface.
        virtual int method(int parameter) = 0;
};

class DerivedClass: public MyInterface
{
    public:
        // If the derived class needs to be instantiated, the derived class
        // must implement its parent's pure virtual function.
        virtual int method(int parameter) override
        {
            // do something
        }
};

