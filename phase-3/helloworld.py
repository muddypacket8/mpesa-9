library = {
    
        "author": "Samuel",
        "genre": "comedy",
        "year": 1972
    },
library ["genre"] = "sparrow"
library.update({"year": 2020})
library.pop("genre")

print(library)
    
