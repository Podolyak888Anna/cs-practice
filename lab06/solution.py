paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

# count_by_extension(paths)   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
# deepest_path(paths)         # "docs/img/logo.png"

# human_size(900)             # "900 Б"
# human_size(1536)            # "1.5 КБ"
# # human_size(5 * 1024 * 1024) # "5.0 МБ"

def count_by_extension(paths):
    extensions = {} 
    for path in paths:
        if "." in path:
            extension = path.split(".")[-1].lower()
        else: 
            extension = ""
        extensions[extension] = extensions.get(extension, 0) + 1 
    return extensions 
print(count_by_extension(paths)) 