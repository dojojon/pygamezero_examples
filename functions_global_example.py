# define a module variable
something_global = "I am a global variable"

# function without using global
def do_something_without_global():
    # Create a new local variable something_global
    something_global = "Creates a new local variable"
    print(something_global)

# function using global
def do_something_with_global():
    global something_global
    something_global = "This updates the global variable as we use 'global'"
    print(something_global)

print(something_global)

do_something_without_global()

print(something_global)

do_something_with_global()

