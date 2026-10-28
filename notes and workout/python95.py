import re

# string1 = "the sea near"
# pattern1 = r"near"
# print(bool(re.match(pattern1,string1)))

pattern1 = r"[a-z]+ear"
string1= """The Second Battle of Newtonia was fought on October 28, 1864, near Newtonia, Missouri, between cavalry of the Union Army and the rear guard of the Confederate Army of Missouri. In September 1864, the Confederates launched Price's Raid (pictured), an attempt to create a popular uprising against Union control of Missouri. After being forced to retreat, the Confederates halted to rest near Newtonia. On the afternoon of October 28, Union pursuers caught up and surprised the Confederates. The main Confederate army withdrew, leaving a rear guard under Brigadier General Joseph O. Shelby. Shelby initially had a numerical advantage, and used it to outflank Blunt's shorter line. Blunt was considering a retreat shortly before sundown when reinforcements arrived in the form of Brigadier General John B. Sanborn and his brigade. Sanborn joined Blunt's line, and the Union troops counterattacked. Shelby ordered a retreat and was not pursued until October 30. Modern historians credit the Union with a victory at Newtonia."""
# match =re.search(pattern1,string1)
# quord=match.span()
# print(string1[quord[0]:quord[1]])


# matches = re.finditer(pattern1,string1)
# list1=[]
# for match in matches: 
#     list1.append(match.span())
# for i in list1:
#     print(string1[i[0]:i[1]])


# string2="JHEDIEUHDEIU"
# string3="dkd"
# pattern2 =r"[A-Za-z0-9]+"
# print(bool(re.fullmatch(pattern2,string3)))


# allmatch = re.findall(pattern1,string1)
# print(allmatch)


date_pattern = r"(\d{4})-(\d{2})-(\d{2})"
# date ="2023-03-04"
# matching = re.fullmatch(date_pattern,date)
# print(bool(matching))
# if matching:
#     print(matching.group(0))
#     print(matching.group(1))
#     print(matching.group(2))
#     print(matching.group(3))


# pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
# matching = re.fullmatch(pattern,date)
# print(bool(matching))
# if matching:
#     print(matching.group("year"))
#     print(matching.group("month"))
#     print(matching.group("day"))


# text = "Room 123, Floor 4"
# result = re.sub(r"\d", "X", text)
# print(result)

