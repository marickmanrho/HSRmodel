def main():
    from initialization.initialize import initialize
    from hsrmodel import hsrmodel

    # Create Data folder and setup parameters for this build
    parms = initialize()

    # Run HSR model
    hsrmodel(parms)

main()
