def main():
    from utils.initialize import initialize
    from fluxoperator.fluxoperator import fluxoperator

    # Create Data folder and setup parameters for this build
    parms = initialize()

    # Determine which model to use
    if parms['model'] == 'fluxoperator':
        fluxoperator(parms)
    else:
        raise ImportError("Model \'%s\' does not yet excist." %parms['model'])

main()
