import file

# 10
# Python
import sys
sys.path.append('../../')
import jupman

# this is a solution, jupman tags should get suppressed:

# work!
#jupman-raise
print('hi')
#/jupman-raise

# removed in exercise, kept in solution
#jupman-strip
y = "stripped!"
#/jupman-strip

# removed in exercise, removed in solution
#jupman-purge
y = "purged!"
#/jupman-purge