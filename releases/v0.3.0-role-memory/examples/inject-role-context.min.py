# pseudo-code only
def inject_role_context(role_path, memory_path):
    return open(role_path).read() + "

" + open(memory_path).read()
