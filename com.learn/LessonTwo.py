customerID = [];
strFile = open("/Users/onlys/temp_file/customer.csv")
lines = 0;
for lin in strFile:
    # print("hello --> " + lin)
    news = lin.split(",")[0]
    customerID.append(str(news))
    lines = lines + 1
print("文件->" + lin)
print("文件->" + str(lines))
print("文件->" + str(customerID))
# print("文件->" + len(set(customerID)))
