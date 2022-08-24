import sys 
import getopt


def transform():
    config = ""
    template = ""
    objtype = ""

    argv = sys.argv

    help = "{0} --objtype <objecttype> --config <config-file> ".format(
        argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hi:o:c:", [
                                "help", "objtype=", "config=", ])
    except:
        print(help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit(2)
        elif opt in ("-o", "--objtype"):
            objtype = arg
        elif opt in ("-c", "--config"):
            config = arg
        
    vars = [objtype, config]
    for var in vars:
        if var == "":
            print('Please provide the correct arguments:')
            print(help)
            sys.exit(2)
    return vars


def map_data():
    config = ""
    template = ""
    objtype = ""

    argv = sys.argv

    help = "{0} --objtype <objecttype> --config <config-file> --template <jsonnet-template-filepath>".format(
        argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hi:o:c:t:", [
                                "help", "objtype=", "config=", "template="])
    except:
        print(help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit(2)
        elif opt in ("-o", "--objtype"):
            objtype = arg
        elif opt in ("-c", "--config"):
            config = arg
        elif opt in ("-t", "--template"):
            template = arg

    vars = [objtype, config, template]
    for var in vars:
        if var == "":
            print('Please provide the correct arguments:')
            print(help)
            sys.exit(2)
    return vars


def query_api():

    config = ""
    argv = sys.argv

    help = "{0}  --config <config-file> ".format(
        argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "c:h:", ["help",  "config="])
    except:
        print(help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit(2)
       
        elif opt in ("-c", "--config"):
            config = arg
       

    vars = [config]
    for var in vars:
        if var == "":
            print('Please provide the correct arguments:')
            print(help)
            sys.exit(2)
    return vars
