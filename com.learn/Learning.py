message = "hello dongpf";
print(message);

message = message + "secend tow l";
print(message);
print(message.title());
print(message.upper());
print(message.lower());
print(2 + 3);
age = 30;
news = "happy " + str(age) + "rd birthday;";
print(news);

animals = ['dog', ' cat ', ' tiger ', 'dragon'];
print(animals);
animals[-1] = "tomcat";
animals.append("grandpa");
print(animals[2].strip());
print(animals);
print(animals[-1].strip());


family = [];
family.append("mom");
family.append("dady");
family.append("big brother");
family.append("me")
family.append("small sister");
print(family)

family.insert(0 , "grand father")
print(family);
del family[0];
print(family)
print(family.pop())
print(family)

family.append("little sister")
family.reverse();
print(family);

print(len(family))

for p in family:
    print(p);   
    print("good come backe");

print("end of the world");


listrange = list(range(1,100,9))
print(listrange)
sequenc = [];
for i in range(1, 10):
    i = i * 10;
    sequenc.append(i);
print(sequenc);

print(max(sequenc))
print(min(sequenc))
print(sum(sequenc))

seq = [value ** 2 for value in range(1, 10)];

for index in seq:
    if index == 25:
        print("25的条件成功")
    elif index == 64:
        print("64的条件成功")
    else:
        print(str(index) + " 失败")


print(seq);

print(seq[1:6])

for age in seq[-2:]:
    print(age);

if 43 not in seq and 4 in seq:
    print("43 不在队列里面")

if 43 not in seq or 490 in seq:
    print("490 不在队列里面")

print(43 == 12)

# customerID = [];
# strFile = open("/Users/onlys/temp_file/customer.csv")
# lines = 0;
# for lin in strFile:
#     # print("hello --> " + lin)
#     news = lin.split(",")[0]
#     customerID.append(str(news))
#     lines = lines + 1
# print("文件->" + lin)
# print("文件->" + str(lines))
# print("文件->" + customerID)
# # print("文件->" + len(set(customerID)))
# print(strFile.read())
# strFile.close()


strDmap = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value5"}

print(strDmap['key1']);

strkeys = strDmap.keys()
for key in strkeys:
    print(key + "  " + strDmap[key])
    strDmap[key] = strDmap[key] + "!!!"
print(strDmap['key1']);
print(strDmap);


for key, value in strDmap.items():
    print(key + " == " + value)




# for (oneMap, value) in strDmap:
#     print(oneMap + " 值 " + value)


