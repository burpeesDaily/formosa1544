#define BOOST_TEST_MODULE QuickStartTest

#include "QuickStart.hpp"

#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>

BOOST_AUTO_TEST_SUITE(QuickStartSuite)

BOOST_AUTO_TEST_CASE(AdditionTest)
{
    QuickStart quickStart;

    BOOST_CHECK_EQUAL(quickStart.add(1, 1), 2);
}

BOOST_AUTO_TEST_SUITE_END()