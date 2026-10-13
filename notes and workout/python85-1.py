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

# parser = argparse.ArgumentParser()
# parser.add_argument("path",type=Path,help="path of the file")
# parser.add_argument("--absolute",action="store_true",help="resolved path")
# args = parser.parse_args()
# file_path = args.path
# print(f"DEBUG - Received path: {file_path}")
# print(f"DEBUG - Absolute check: {file_path.absolute()}")
# print(f"DEBUG - Exists? {file_path.exists()}")
# print(f"DEBUG - Is file? {file_path.is_file()}")
# if not file_path.is_file():
#     parser.error(f"{args.path} file doesnt exist")
# print(file_path.stat().st_size,"bytes")
# if args.absolute:
#     print("absolute path :",file_path.resolve())

parser = argparse.ArgumentParser(description="task manager")
subparser = parser.add_subparsers(dest="command",required=True)
add_task=subparser.add_parser("add")
add_task.add_argument("task_id",type=int,help="task id")
add_task.add_argument("task",type=str,help="define the task you want to add")
list_task = subparser.add_parser("list")
remove_task = subparser.add_parser("remove")
remove_task.add_argument("task_idr",type = int ,help="provide the task id to removes task")
args= parser.parse_args()
tasks = {1:"workout",2:"running"}
if args.command == "add":
    if args.task_id not in tasks.keys():
        print("successfully added task")
        tasks[args.task_id]=args.task
        for taskid,task in tasks.items():
            print(f"{taskid}:{task}")
    else:
        for taskid,task in tasks.items():
            print(f"{taskid}:{task}")
        parser.error("faild to add task : task id already exist")
elif args.command =="list":
    if tasks:
        for taskid,task in tasks.items():
            print(f"{taskid}:{task}")
    else:
        print("there are no tasks available")
elif args.command =="remove":
    if args.task_idr not in tasks.keys():
        parser.error("task id does not exist")
    else:
        tasks.pop(args.task_idr)
        print("successfully remover task")
        for taskid,task in tasks.items():
            print(f"{taskid}:{task}")