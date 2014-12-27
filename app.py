import os
import sys
import getopt

print "My name is " + __name__

def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    # This is a comment to test diffget
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)

# Another comment to test Gwrite / Gread
    # process options
    for o,a in opts:
        if o in ('-h', '--help'):
            print __doc__
            sys.exit(0)

    # process arguments
    for arg in args:
        process(arg)  # process() is define elsewhere

# this change was done on master and was not on new-feature branch
# this was added as part of new-feature branch to test git rebase -i
# this was 2nd change in test for git rebase -i

if __name__ == "__main__":
    main()

# Another change in master not in new feature branch
