from pathlib import Path

folder = Path('./Temp')
filename = folder / 'test.txt'
file = filename.open()
print(file.read())
file.close()

current_path = Path()
print(current_path)
print(current_path.cwd())
#/Users/athlony/Documents/GitHub/GoIT_Python/Temp/test.txt

file = current_path / 'bin' / 'utils' / 'paint.drawio.svg'
print(file)
print(current_path.joinpath('bin', 'utils', 'paint.drawio.svg'))