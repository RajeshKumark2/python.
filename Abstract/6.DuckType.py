def write_to_file(file_obj, content):
    if not hasattr(file_obj, 'write'):
        raise TypeError("Expected file-like object with write() method")
    file_obj.write(content)
from io import StringIO
real_file = open("test.txt", "w")
memory_file = StringIO()
for target in [real_file, memory_file]:
    write_to_file(target, "Hello abstraction!")
    target.close()
print(memory_file.getvalue()) 




