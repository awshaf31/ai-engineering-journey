File_name = input("File name: ").strip().lower()

if File_name.endswith(".jpeg") or File_name.endswith(".jpg"):
    print("image/jpeg")
elif File_name.endswith(".gif"):
    print("image/gif")
elif File_name.endswith(".png"):
    print("image/png")
elif File_name.endswith(".pdf"):
    print("application/pdf")
elif File_name.endswith(".zip"):
    print("application/zip")
elif File_name.endswith(".txt"):
    print("text/plain")
else :
    print("application/octet-stream")
