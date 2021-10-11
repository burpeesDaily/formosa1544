// Copyright © 2021 by Shun Huang. All rights reserved.
// Licensed under MIT License.
// See LICENSE in the project root for license information.

#include <memory>

class BaseClass
{
    public:
        virtual void doWork()
        {
            // do some work
        }
};


class DerivedClassA: public BaseClass
{
    public:
        virtual void doWork() override
        {
            // do some work
        }
};

class DerivedClassB: public BaseClass
{
    public:
        virtual void doWork() override
        {
            // do some work
        }
};

void myFunction(std::shared_ptr<BaseClass> p)
{
    // The appropriate doWork() to be called will be determined by
    // the instance of p at the runtime.
    p->doWork();
}
