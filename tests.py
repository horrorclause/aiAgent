# Test script for /functions/get_files_info.py and get_file_contents.py

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# # Test scenario #1
# fileInfo = get_files_info("calculator", ".")
# print(f"Result for current directory:\n{fileInfo}")

# # Test scenario #2
# fileInfo2 = get_files_info("calculator", "pkg")
# print(f"Result for pkg directory:\n{fileInfo2}")

# # Test scenario #3
# fileInfo3 = get_files_info("calculator", "/bin" )
# print(f"Result for the /bin directory:\n{fileInfo3}")

# # Test scenario #4
# fileInfo4 = get_files_info("calculator", "../" )
# print(f"Result for ../ :\n{fileInfo4}")

# # Test scenario #5
# fileInfo5 = get_files_info(".", "calculator" )
# print(f"Result for calculator directory:\n{fileInfo5}")

# # Test scenario #6
# fileInfo6 = get_files_info(".", "." )
# print(f"Result for aiAgent directory:\n{fileInfo6}")

print('\n[+] Beginning "get_file_content" tests:\n')

# Test Scenario #1
file = get_file_content("calculator", "lorem.txt")
print(f'Result for "lorem.txt" file:\n{file}\n')
