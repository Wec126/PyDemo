def linear(interval=1, offset=0):

    docstring = "Track at iterations {" + f"{offset} + n * {interval} " + "| n >= 0}."

    def schedule(global_step):
        shifted = global_step - offset
        if shifted < 0:
            return False
        else:
            return shifted % interval == 0

    schedule.__doc__ = docstring

    return schedule
