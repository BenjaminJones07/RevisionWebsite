from re import sub, findall, M # Substitute RegEx, Find all matches RegEx, Multiline flag
import os # Does import file exist

# Working Tags:
# - Blockquote
# - Unordered lists
# - Headings (1, 2, 3, 4)
# - Images
# - Links

def markdown(s):
    s = "{0}\n\n".format(s)
    [s := s.replace("; include \"{0}\"".format(x), x if not os.path.isfile(x) else open(x).read()) for x in findall(r"^; include \"(.+){1}?\"$", s, flags=M)] # Include md file
    s = sub(r"> (.*)", r"<blockquote class='blockquote'>\1</blockquote>", s) # Replace blockquotes
    s = sub(r"(- (?:.|\n)*?)\n\n", r"\n<ul class='list'>\n\1\n</ul>\n<br>\n", s) # Create lists
    s = sub(r"^# (.*)$", r"<h1>\1</h1>", s, flags=M) # Heading 1
    s = sub(r"^## (.*)$", r"<h2>\1</h2>", s, flags=M) # Heading 2
    s = sub(r"^### (.*)$", r"<h3>\1</h3>", s, flags=M) # Heading 3
    s = sub(r"^#### (.*)$", r"<h4>\1</h4>", s, flags=M) # Heading 4
    s = sub(r"^!\[(.*)?]\((.*)?\)$", r"<br><br><img src='\2' alt='\1' class='center'><br>", s, flags=M) # Images
    s = sub(r"\[((?:.)*?)\]\(((?:.)*?)\)", r"<a href='\2'>\1</a>", s) # Links (MUST BE AFTER IMAGES TO ALLOW FOR INLINE LINKS)
    return sub(r"- (.*)", r"<li>\1</li>", s).strip("\n") # Add list elements 