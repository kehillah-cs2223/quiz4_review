# Complete the functions `ask_for_name` and `write_to_file` so that the program
# gets a user's name and creates an html file that says hello to them.

def ask_for_name():
    # Ask the user for their name
    return ### YOUR CODE HERE

def build_html(name):
    return f"<html><h1>Hello, {name}</h1><html>"

def write_to_file(html):
    # Write the string `html` to the file `hello.html`
    return ### YOUR CODE HERE

############# Tests below (don't change these!) #############
name = ask_for_name()
html = build_html(name)
write_to_file(html)

