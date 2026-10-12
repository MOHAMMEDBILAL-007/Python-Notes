import argparse
from pathlib import Path
# parser = argparse.ArgumentParser(description="parsing the argument")
# parser.add_argument("name",help="name of the person to greet")
# parser.add_argument("--uppercase",action="store_true",help="if you need the message in uppercase")
# parser.add_argument("--output",action=)
# args = parser.parse_args()
# greet = f"hello {args.name} how are you !"
# if args.uppercase:
#     greet = greet.upper()
# print(greet)

parser = argparse.ArgumentParser()
parser.add_argument("path",type=Path,help="path of the file")
parser.add_argument("--absolute",action="store_true",help="resolved path")
args = parser.parse_args()
file_path = args.path
print(f"DEBUG - Received path: {file_path}")
print(f"DEBUG - Absolute check: {file_path.absolute()}")
print(f"DEBUG - Exists? {file_path.exists()}")
print(f"DEBUG - Is file? {file_path.is_file()}")
if not file_path.is_file():
    parser.error(f"{args.path} file doesnt exist")
print(file_path.stat().st_size,"bytes")
if args.absolute:
    print("absolute path :",file_path.resolve())