BUILDDIR = build
INCDIRS = include
SRCDIR = src
TESTDIR = test

OBJS = $(addprefix $(BUILDDIR)/, $(patsubst %.cpp, %.o, $(notdir $(wildcard $(SRCDIR)/*.cpp))))
TESTOBJS = $(addprefix $(BUILDDIR)/, $(patsubst %.cpp, %.o, $(notdir $(wildcard $(TESTDIR)/*.cpp))))

LIBQUICKSTART_FNAME = $(BUILDDIR)/libQuickStart.a
TEST_FNAME = $(BUILDDIR)/test_main

CXXFLAGS += $(INCDIRS:%=-I%) -std=c++1y
LDFLAGS += $(LIBQUICKSTART_FNAME) -lboost_unit_test_framework

.PHONY: all clean

all: $(LIBQUICKSTART_FNAME) $(TEST_FNAME)

$(LIBQUICKSTART_FNAME): $(OBJS)
	$(AR) $(ARFLAGS) $@ $^

$(TEST_FNAME): $(TESTOBJS) $(LIBQUICKSTART_FNAME)
	$(CXX) -o $(TEST_FNAME) $^ $(LDFLAGS)

$(BUILDDIR)/%.o:$(SRCDIR)/%.cpp | $(BUILDDIR)
	$(COMPILE.cc) $< $(OUTPUT_OPTION)
	$(COMPILE.cc) -MM -MP -MT $@ $< -o $(BUILDDIR)/$*.d

$(BUILDDIR):
	@mkdir $(BUILDDIR)

$(BUILDDIR)/%.o:$(TESTDIR)/%.cpp | $(BUILDDIR)
	$(COMPILE.cc) $< $(OUTPUT_OPTION)
	$(COMPILE.cc) -MM -MP -MT $@ $< -o $(BUILDDIR)/$*.d

run_test:
	$(TEST_FNAME)

clean:
	$(RM) $(BUILDDIR)/*.d $(BUILDDIR)/*.o $(LIBQUICKSTART_FNAME) $(TEST_FNAME)
