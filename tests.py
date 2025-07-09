# Test script for /functions/get_files_info.py and get_file_contents.py

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

'''
Start of get_files_info test
'''

print('\n\n[+] Beginning "get_files_info" tests:\n')

# Test scenario #1
fileInfo = get_files_info("calculator", ".")
print(f"Result for current directory:\n{fileInfo}")

# Test scenario #2
fileInfo2 = get_files_info("calculator", "pkg")
print(f"Result for pkg directory:\n{fileInfo2}")

# Test scenario #3
fileInfo3 = get_files_info("calculator", "/bin" )
print(f"Result for the /bin directory:\n{fileInfo3}")

# Test scenario #4
fileInfo4 = get_files_info("calculator", "../" )
print(f"Result for ../ :\n{fileInfo4}")

# Test scenario #5
fileInfo5 = get_files_info(".", "calculator" )
print(f"Result for calculator directory:\n{fileInfo5}")

# Test scenario #6
fileInfo6 = get_files_info(".", "." )
print(f"Result for aiAgent directory:\n{fileInfo6}")

print('\n\n[-] Ending "get_files_info" tests [-]\n')


'''
Start of get_file_content test
'''

print('\n\n[+] Beginning "get_file_content" tests:\n')

# Test Scenario #1
print('\n[+] Test Scenario #1\n')
file = get_file_content("calculator", "lorem.txt")
print(f'Result for "lorem.txt" file:\n{file}\n')

# Test Scenario #2
print('\n[+] Test Scenario #2\n')
file2 = get_file_content("calculator", "main.py")
print(f'Result for "main.py" file:\n{file2}\n')

# Test Scenario #3
print('\n[+] Test Scenario #3\n')
file3 = get_file_content("calculator", "pkg/calculator.py")
print(f'Result for "pkg/calculator.py" file:\n{file3}\n')

# Test Scenario #4
print('\n[+] Test Scenario #4\n')
file4 = get_file_content("calculator", "/bin/cat")
print(f'Result for "/bin/cat" file:\n{file4}\n')

print('\n\n[-] Ending "get_file_content" tests [-]\n')


'''
Start of write_file test
'''

print('\n\n[+] Beginning "write_file" tests:\n')

print('\n[+] Test Scenario #1\n')
write1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f'Result for "lorem.txt" file:\n\n{write1}\n')

print('\n[+] Test Scenario #2\n')
write2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f'Result for "pkg/morelorem.txt" file:\n\n{write2}\n')

print('\n[+] Test Scenario #3\n')
write3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f'Result for "/tmp/temp.txt" file:\n\n{write3}\n')