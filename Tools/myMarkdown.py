from re import sub, findall, M

def markdown(s):
    s = "{0}\n\n".format(s)
    s = sub(r"> (.*)", r"<blockquote class='blockquote'>\1</blockquote>", s) # Replace blockquotes
    s = sub(r"(- (?:.|\n)*?)\n\n", r"\n<ul class='list'>\n\1\n</ul>\n<br>\n", s) # Create lists
    s = sub(r"^# (.*)$", r"<h1>\1</h1>", s, flags=M) # Heading 1
    s = sub(r"^## (.*)$", r"<h2>\1</h2>", s, flags=M) # Heading 2
    s = sub(r"^### (.*)$", r"<h3>\1</h3>", s, flags=M) # Heading 3
    s = sub(r"^#### (.*)$", r"<h4>\1</h4>", s, flags=M) # Heading 4
    s = sub(r"^!\[(.*)?]\((.*)?\)$", r"<br><br><img src='\2' alt='\1' class='center'><br>", s, flags=M) # Images
    s = sub(r"\[((?:.)*?)\]\(((?:.)*?)\)", r"<a href='\2'>\1</a>", s) # Links
    [s := s.replace(x, "<p>{0}</p>".format(x)) for x in findall(r"((?:.|\n)*?)\n\n", s) if "<ul" not in x] # Paragraph all else
    return sub(r"- (.*)", r"<li>\1</li>", s).strip("\n") # Add list elements