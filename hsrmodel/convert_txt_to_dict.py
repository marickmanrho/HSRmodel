def txt_to_dict(path):
    # Initialize Dictionary
    parms = {}

    # Read the parameters.txt file
    with open(path, "r") as read_file:
        cmplt_para_file = read_file.readlines()

    # Discard comments and create dictionary
    for line in cmplt_para_file:
        this_line = line.strip()    # Remove whitespace
        if not this_line or this_line[0]=='#':
            # If the line is empty it returns a bolean we check against. If the
            # first character is a pound sign, we treat is as comment.
            continue
        else:
            # We keep everything else

            # split the line in what is before and after the equal sign.
            this_line = this_line.split('=')

            # Write new dictionary item
            exec('parms[\'%s\']=%s' % (this_line[0].strip(), this_line[1].strip()))

    return parms
