 
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv)
    if num_arg == 1:
        print("{:d} argument.".format(num_arg - 1))
    elif num_arg == 2:
        print("{:d} argument:".format(num_arg - 1))
    else:
        print("{:d} arguments:".format(num_arg - 1))
    for i in range(num_arg):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, sys.argv[i]))
