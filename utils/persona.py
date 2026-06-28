current_persona = None


def set_persona(persona):

    global current_persona

    current_persona = persona


def get_persona():

    return current_persona


def clear_persona():

    global current_persona

    current_persona = None