import os,json,sys
from random_name import Random_name
from code_transform import code2List, content2List,write2blocks,write2generators

if "blockly-electron" in os.path.dirname(os.path.realpath(sys.executable)): #使用者用exe时的路径
    thisFile_path = os.path.dirname(os.path.realpath(sys.executable))
elif "blockly-electron" in __file__:#开发者debug使用的路径
    thisFile_path = __file__
else:
    raise FileNotFoundError(
        "路径错误，请把这个文件放到有blockly-electron的地方"
    )

start = thisFile_path.find("blockly-electron")
path = os.path.join(thisFile_path[:start+16], "resources/assets/blocklyFiles/")


copy_path = os.path.join(thisFile_path[:start+16], "resources/assets/copy_blocklyFiles/")

def delete_file(path): #删除文件夹，用于给下面的save_copy()调用
    # 如果调用shutil库的删除文件夹函数的话一行代码搞定，但会增加自动生成编程块软件的大小，所以能自己实现的尽量自己实现
    if os.path.isdir(path):
        files = os.listdir(path)
        # 遍历并删除文件
        for file in files:
            p = os.path.join(path, file)
            if os.path.isdir(p):
                # 递归调用，直至删除所有文件，再删除空的文件夹，因为文件夹如果不为空，无法直接删除，会报错
                delete_file(p)
            else:
                os.remove(p)
                    
        # 删除文件夹
        try:
            os.rmdir(path)
        except: #增加大分支然后删除大分支之后会遇到文件夹被打开无法删除，那就别删除了，后面再会有一个try-except来捕获另一个错误
            pass

    else:
        os.remove(path)

def save_copy(src, target): #保存副本
    filelist = os.listdir(src)
    if os.path.isdir(target): #如果之前已经保存了一个副本，就把之前的副本删除，然后再把这次的副本加进去
        delete_file(target) #删除文件夹的函数
    try:
        os.mkdir(target) #创建一个新的文件夹来装副本
    except(FileExistsError): #这个捕获就对应了上面说的那个文件夹被打开无法删除
        pass
     #接下来的操作就是复制原文件夹到副本文件夹了
    for file in filelist:
        path = os.path.join(src, file)
        if ('blocks' not in path) and ('generators' not in path) and ('jsons' not in path):
            continue
        if os.path.isdir(path):  # 判断是否为文件夹
            target1 = os.path.join(target, file)
            os.mkdir(target1)  # 在目标文件下在创建一个文件夹
            save_copy(path, target1) #递归复制文件，直至复制完整个文件夹
        else:
            with open(path, 'rb') as rstream:
                container = rstream.read()
                path1 = os.path.join(target, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)

def revoke_operate():#撤销本次块的操作——删除或者增加块
    try:
        for i in ['jsons', 'blocks', 'generators']:
            save_copy(copy_path+i, path+i)
            delete_file(copy_path+i)
    except FileNotFoundError:
        return False

def Block_Label_num(List):
    block_num = 0
    label_num = 0
    for Dict in List:
        if Dict['kind'] == 'block':
            block_num+=1
        elif Dict['kind'] == 'label':
            label_num+=1
    return (block_num,label_num)

def classname_fileUrl():
    Dict = {}
    for file in os.listdir(path + 'jsons'):
        with open(path + 'jsons/' + file, 'r', encoding='utf-8') as f:
            try:
                file_dict = json.loads(f.read())
            except:
                return path + 'jsons/' + file
            try:
                _ = file_dict['category']['contents'][0]['name'] #如果一个类里面没有任何块了，不加这个就出现逻辑错误

                parentName = file_dict['category']["name"] #父节点名字
                for index in range(len(file_dict['category']['contents'])):
                    selfName = file_dict['category']['contents'][index]['name']
                    blocks_file = path + 'blocks' + file_dict['blocklyFilesUrls'][0][
                                                    file_dict["blocklyFilesUrls"][0].rfind('/'):]
                    generators_file = path + 'generators' + file_dict['blocklyFilesUrls'][1][
                                                            file_dict["blocklyFilesUrls"][1].rfind('/'):]
                    json_file = path + 'jsons/' + file
                    block_num = Block_Label_num(file_dict['category']['contents'][index]['contents'])
                    Dict[file_dict['category']['contents'][index]['name']] = [blocks_file,generators_file,
                                                                              json_file,block_num, parentName,selfName]
            except:
                try:
                    parentName = file_dict['category']["name"] #没有分支，父节点名字就是本身
                    blocks_file = path + 'blocks' + file_dict['blocklyFilesUrls'][0][
                                                    file_dict["blocklyFilesUrls"][0].rfind('/'):]
                    generators_file = path + 'generators' + file_dict['blocklyFilesUrls'][1][
                                                            file_dict["blocklyFilesUrls"][1].rfind('/'):]
                    json_file = path + 'jsons/' + file
                    block_num = Block_Label_num(file_dict['category']['contents'])
                    Dict[file_dict['category']['name']] = [blocks_file,generators_file,json_file,block_num, parentName, parentName]

                except(KeyError):
                    continue
    return Dict

def findDict(List, index):
    List = list(filter(lambda x :x['kind']=='block', List)) #先把列表中kind是label的字典过滤掉

    Dict = List[index-1]
    blockxml = Dict['blockxml']
    start = blockxml.find("'") + 1
    end = blockxml.find("'", start)
    block_name = blockxml[start:end]
    return Dict, block_name

def changeOtherFile(num,NewFileName,add=1):
    pathList = os.listdir(path+"jsons")
    if "idea" in pathList:
        pathList.remove(".idea")
    for index, file in enumerate(pathList):
        if int(file[:4].lstrip("0")) < int(num.lstrip("0")) or file == NewFileName+".json":
            continue
        new_file = ("0"*4+str(int(file[:4].lstrip("0"))+add))[-4:]+file[4:-5]
        file = file[:-5]
        os.rename(path+"jsons/"+file+".json", path+"jsons/"+new_file+".json")
        os.rename(path + "blocks/" + file+ "_b.js", path + "blocks/" + new_file + "_b.js")
        os.rename(path + "generators/" + file+ "_g.js", path + "generators/" + new_file + "_g.js")
        with open(path+"jsons/"+new_file+".json", 'r', encoding='utf-8') as f:
            Dict1 = json.loads(f.read()) #修改json文件里面的blocklyFilesUrls
            Str1 = Dict1["blocklyFilesUrls"][0]
            Str2 = Dict1["blocklyFilesUrls"][1]
            start1 = Str1.rfind("/") + 1
            start2 = Str2.rfind("/") + 1
            Dict1["blocklyFilesUrls"][0] = Str1[:start1] + ("0" * 4 + str(int(Str1[start1:start1 + 4]) + add))[
                                                          -4:] + Str1[start1 + 4:]
            Dict1["blocklyFilesUrls"][1] = Str2[:start2] + ("0" * 4 + str(int(Str2[start2:start2 + 4]) + add))[
                                                          -4:] + Str2[start2 + 4:]
        with open(path+"jsons/"+new_file+".json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(Dict1, indent=4, ensure_ascii=False))

def addText(List):#如果代码内容有相邻两个都是TEXT，就合并他们
    newList = List.copy()
    for index, tur in enumerate(List):
        if tur[2]=='TEXT'and (index != len(List)-1):
            if List[index+1][2]=='TEXT':
                newList.pop(index)
                newList[index] = (tur[0]+List[index+1][0],(tur[1][0],List[index+1][1][1]), 'TEXT')
                break
    if len(newList)==len(List):
        return newList
    return addText(newList)     

def checkCodeContentSame(code, content):
    varIsSame = sorted([x[0] for x in code if x[2]=='Var'])==sorted([x[0] for x in content if x[2]=='Var'])
    NumIsSame = sorted([x[0] for x in code if x[2]=='NUM'])==sorted([x[0] for x in content if x[2]=='NUM'])
    StrIsSame = sorted([x[0] for x in code if x[2] == 'STR']) == sorted([x[0] for x in content if x[2] == 'STR'])
    if varIsSame==False:
        return "普通变量"
    elif NumIsSame==False:
        return '数字类型的变量'
    elif StrIsSame==False:
        return '字符串类型的变量'
    else:
        return True

class Operate(): #增加块
    def __init__(self, content, demo, classNameTur, used_lib,
                 used_class, UpDown_connect, classname_fileUrl_dict,
                 isHaveBranchList, colorTur, positionTur): #Tur就表示是元组(是否保持默认，不保持默认的话的值)
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.colorTur = colorTur #(是否保持默认颜色，选择生成的块的颜色)
        self.positionTur = positionTur #(是否保持默认生成到最后一个，选择生成的块相对第几个块，相对第几个块之前还是之后)
        self.classNameTur = classNameTur
        self.classname_fileUrl_dict = classname_fileUrl_dict
        #classname_fileUrl_dict是一个字典{类名: [blocks文件地址, generators文件地址, json文件地址, (块block的数量, 标签label的数量)]...}
        for _, value in classname_fileUrl_dict.items():
            if value[4]==self.classNameTur[0]:
                self.blocks_file = value[0]
                self.generators_file = value[1]
                self.json_file = value[2]
        self.class_name = self.classNameTur[0] if self.classNameTur[1]=="无小分支" else self.classNameTur[1]
        self.used_lib = used_lib
        self.used_class = used_class
        self.UpDown_connect = UpDown_connect #是否上下接
        self.name = Random_name(6).generate_name() #随机获得名字
        self.special = False #如果要生成的块在机器学习或者硬件控制这种特殊的类里面，就需要区别对待
        self.color = self.find_color() #找到这个类里面块的颜色，在这个类上造块也用这个颜色
        self.Demo = code2List(demo[0], self.used_lib, self.used_class)
        self.isHaveBranchList = isHaveBranchList #查找哪个类有多个分支
        for index, tur in enumerate(code2List(demo[0], self.used_lib, self.used_class)): #如果不加这个循环，他就会以为类名是普通的变量名
            if tur[0] == self.used_lib or tur[0] == self.used_class:
                self.Demo[index] = (tur[0], tur[1], 'TEXT')
        self.Content = content2List(content[0])
        self.checkSame = checkCodeContentSame(self.Demo,self.Content)




    def find_color(self): #找到这个类里面块的颜色，如果保持默认的话，造出来的块的颜色也跟这个类里面的块的颜色一样，否则就按照选择的颜色来
        if self.colorTur[0]:
            with open(self.blocks_file, encoding='utf-8') as f:
                file_content = f.read()
                start = file_content.find('this.setColour(') + len('this.setColour(')
                end = file_content.find(')', start)
                color = file_content[start:end]
                if color.replace(' ','')=='':
                    color = 20
                return color
        else:
            return '"'+self.colorTur[1]+'"'

    def Write2Generators(self):
        write2generators(self.name,self.used_lib,self.used_class,self.Demo,self.UpDown_connect,self.generators_file,addText)

    def Write2Blocks(self,color):
        write2blocks(self.name, self.Content, self.UpDown_connect, self.blocks_file,color)


    def Write2Json(self):
        Dict = {}
        Dict["kind"] = "block"
        Json_str = '<block type=\'' + self.name + '\'>'
        for i in self.Content:
            if i[2] == 'Var':
                Json_str += '<value name=\'' + i[0] + '\'><block type=\'variables_get\'><field name=\'VAR\'>' + i[
                    0] + '</field></block></value>'
            elif i[2] == 'NUM':
                Json_str += '<value name=\'' + i[
                    0] + '\'><block type=\'math_number\'><field name=\'NUM\'>0</field></block></value>'
            elif i[2] == 'STR':
                Json_str += '<value name=\'' + i[
                    0] + '\'><block type=\'text\'><field name=\'TEXT\'></field></block></value>'

        Json_str += '</block>'
        Dict["blockxml"] = Json_str
        # 写入文件里面
        f = open(self.json_file, 'r+', encoding='utf-8')
        try:
            Dict1 = json.loads(f.read())
            if self.isHaveBranchList[self.classNameTur[0]][0]>0:
                List = Dict1["category"]["contents"][[branch[0] for branch in self.isHaveBranchList[self.classNameTur[0]][1:]].index(self.classNameTur[1])][
                    "contents"]
                if len(List)==0:
                    Dict1["category"]["contents"][
                        [branch[0] for branch in self.isHaveBranchList[self.classNameTur[0]][1:]].index(
                            self.classNameTur[1])][
                        "contents"].append(Dict)
                else:
                    Dict3, _ = findDict(List, self.positionTur[1])
                    Dict1["category"]["contents"][[branch[0] for branch in self.isHaveBranchList[self.classNameTur[0]][1:]].index(self.classNameTur[1])][
                        "contents"].insert(List.index(Dict3) + (0 if self.positionTur[2] == "之前" else 1), Dict)
            else:
                List = Dict1["category"]["contents"]
                if len(List)==0:
                    Dict1["category"]["contents"].append(Dict)
                else:
                    Dict3, _ = findDict(List, self.positionTur[1])
                    Dict1["category"]["contents"].insert(List.index(Dict3)+(0 if self.positionTur[2]=="之前" else 1) , Dict)
        except:
            pass
        f.close()
        with open(self.json_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(Dict1, indent=4, ensure_ascii=False)) #ensure_ascii=False防止中文乱码

    def generate(self):
        self.Write2Generators()
        self.Write2Blocks(self.color)
        self.Write2Json()

class Delete(): #删除块
    def __init__(self,class_nameTur, delete_index, classname_fileUrl_dict):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.class_nameTur = class_nameTur
        self.delete_index = delete_index
        for _, value in classname_fileUrl_dict.items():
            if value[4]==self.class_nameTur[0]:
                self.blocks_file = value[0]
                self.generators_file = value[1]
                self.json_file = value[2]
                self.block_num = value[3][0]
                self.label_num = value[3][1]
                break



    def Delete_Json(self):
        with open(self.json_file, 'r', encoding='utf-8') as f:
            try:
                Dict = json.loads(f.read())
                if self.class_nameTur[1]=="无小分支":
                    Dict1, self.name = findDict(Dict["category"]["contents"], self.delete_index)
                    Dict["category"]["contents"].pop(Dict["category"]["contents"].index(Dict1))
                else:
                    for index, dic in enumerate(Dict["category"]["contents"]):
                        if dic["name"]==self.class_nameTur[1]:
                            Dict1, self.name = findDict(Dict["category"]["contents"][index]["contents"], self.delete_index)
                            Dict["category"]["contents"][index]["contents"].pop(Dict["category"]["contents"][index]["contents"].index(Dict1))
                            break
            except:
                f.close()
                raise
        
        with open(self.json_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(Dict, indent=4, ensure_ascii=False))

    def Delete_Blocks(self):
        with open(self.blocks_file, encoding='utf-8') as f:
            start = None
            lines = f.readlines()
            for index, line in enumerate(lines):
                if (start == None) and (('Blockly.Blocks.'+self.name+' ' in line) or ('Blockly.Blocks.'+self.name+'=' in line) or ('Blockly.Blocks'+"[\'"+self.name+"\']" in line) or ('Blockly.Blocks'+'[\"'+self.name+'\"]' in line)):
                    start = index
                    continue
                if start != None and 'Blockly.Blocks' in line:
                    end = index
                    break
            else:
                if start==None:
                    return False
                end = -1

        with open(self.blocks_file, mode='w', encoding='utf-8') as f:
            if end!=-1:
                for index, line in enumerate(lines):
                    if index in range(start, end):
                        continue
                    f.writelines(line)
            else:
                for index, line in enumerate(lines):
                    if index >=start:
                        break
                    f.writelines(line)

    def Delete_generators(self):
        with open(self.generators_file, encoding='utf-8') as f:
            start = None
            lines = f.readlines()
            for index, line in enumerate(lines):
                if (start == None) and (
                        ('Blockly.Python.' + self.name+' ' in line) or  ('Blockly.Python.' + self.name+'=' in line) or ('Blockly.Python' + "[\'" + self.name + "\']" in line) or ('Blockly.Python' + "[\"" + self.name + "\"]" in line)):
                    start = index
                    continue
                if start != None and 'function' in line:
                    end = index
                    break
            else:
                if start == None:
                    return False
                end = - 1

        with open(self.generators_file, mode='w', encoding='utf-8') as f:
            if end != -1:
                for index, line in enumerate(lines):
                    if index in range(start, end):
                        continue
                    f.writelines(line)
            else:
                for index, line in enumerate(lines):
                    if index >= start:
                        break
                    f.writelines(line)

    def delete(self):
        if self.delete_index == 0:
            revoke_operate()
            return '无', '没有任何事情发生'
        self.Delete_Json()
        if self.Delete_Blocks()==False:
            revoke_operate()
            return '错误', 'blocks文件中没有这个块'
        elif self.Delete_generators() == False:
            revoke_operate()
            return '错误', 'generators文件中没有这个块'
        return True

class Add_bigBranch():#增加大分支
    def __init__(self, new_branch_name, color, position_Tur , fileNameTur):
        self.new_branch_name = new_branch_name #新分支的名字
        self.color = ("0"*6+color)[-6:] #新分支的颜色
        self.position_Tur = position_Tur #(是否保持默认生成到最后一个，选择生成的分支相对第几个分支，相对第几个块之前还是之后)
        self.position_Tur = (position_Tur[0], position_Tur[1], "之后" if position_Tur else "之前")
        self.fileNameTur = fileNameTur #(是否随机取名，不随机的话取得名字是什么)
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.getFileName()

    def getFileName(self):
        self.index = ("0"*4+str(len(os.listdir(path+"jsons"))+1))[-4:] if self.position_Tur[0] else ("0" * 4 + str(self.position_Tur[1] + (0 if self.position_Tur[2] == '之前' else 1)))[
                                   -4:] #文件名前面的序号
        name = (Random_name(6).generate_name() if self.fileNameTur[0] else self.fileNameTur[1])
        self.NewFileName =  self.index+name



    def new_File(self):
        with open("".join([path, 'jsons/', self.NewFileName,".json"]), mode='w', encoding='utf-8') as f:
            try:
                Dict = {"blocklyFilesUrls":["".join(["../assets/blocklyFiles/blocks/",self.NewFileName, "_b.js" ]),
                                            "".join(["../assets/blocklyFiles/blocks/",self.NewFileName, "_g.js" ])],
                        "category": {
                            "kind": "category",
                            "name": self.new_branch_name,
                            "colour": self.color,
                            # "icon": "./"+self.new_branch_name+".png",
                            "icon":"新的.png",
                            "contents": []
                            }
                        }
                f.write(json.dumps(Dict, indent=4, ensure_ascii=False))
            except:
                f.close()
                raise
        for name in [("blocks/","_b.js"),("generators/", "_g.js")]:
            with open("".join([path, name[0], self.NewFileName, name[1]]), mode='w', encoding='utf-8') as f:
                f.write("'use strict';")

        if not self.position_Tur[0]:
            changeOtherFile(self.index, self.NewFileName)

class Add_smallBranch():
    def __init__(self, color, position_Tur, name, classname_fileUrl_dict):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.color = color #这个小分支的颜色
        self.position_Tur = position_Tur #(所属大分支， 最终生成在这个大分支的第几个位置)
        self.name = name #这个小分支的名字
        self.singleBranch = False
        for _, value in classname_fileUrl_dict.items():
            if value[4] == self.position_Tur[0]:
                self.json_file = value[2]
                if value[4]==value[5]:
                    self.singleBranch = True
                break

    def generate_branch(self, QBox):
        with open(self.json_file, 'r', encoding='utf-8') as f:
            try:
                reply = 65536 #默认是否
                Dict = json.loads(f.read())
                # 如果一个大分支里面没有小分支，而且内部有编程块，然后我们为他添加小分支，就需要考虑是否把原有的编程块移植到新的小分支
                if self.singleBranch:
                    if Dict['category']['contents']:
                        reply = QBox("确认一下","这个分支存在编程块，是否添加到新生成的小分支内？")

                if reply==65536: #如果是否
                    Dict["category"]["contents"].insert(int(self.position_Tur[1])-1, {
                        "kind": "category",
                        "name": self.name,
                        "colour": self.color,
                        "icon":"./"+self.name+".png",
                        "contents":[]
                    })

                else:
                    List_trans = Dict['category']['contents']
                    Dict["category"]["contents"] = [{
                        "kind": "category",
                        "name": self.name,
                        "colour": self.color,
                        "icon": "./" + self.name + ".png",
                        "contents": []
                    }]
                    for block in List_trans:
                        Dict["category"]["contents"][0]["contents"].append(block)
            except:
                f.close()
                raise
        with open(self.json_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(Dict, indent=4, ensure_ascii=False))

class DeleteBranch():
    def __init__(self, branchTur, classname_fileUrl_dict):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.branchTur = branchTur #(是否是大分支，大分支名字， 小分支名字)
        self.classname_fileUrl_dict = classname_fileUrl_dict

        if self.branchTur[0]==False:#删除小分支的时候
            smallBranchList = [value[5] for key,value in self.classname_fileUrl_dict.items() if value[4]==self.branchTur[1]]
            self.branchTur = (False, self.branchTur[1], smallBranchList.index(self.branchTur[2])+1)

    def Delete(self):
        if self.branchTur[0]:
            List = os.listdir(path+"/jsons")
            if ".idea" in List:
                List.remove(".idea")
            index = self.branchTur[2]-1
            json_file = path+"/jsons/"+List[index]
            block_file = path+"/blocks/"+List[index][:-5]+"_b.js"
            generator_file = path + "/generators/" + List[index][:-5] + "_g.js"
            for file in [json_file, block_file, generator_file]:
                os.remove(file)
            changeOtherFile(("0"*4+str(index+1))[-4:], NewFileName='', add=-1)
        else:
            for _, value in self.classname_fileUrl_dict.items():
                if value[4]==self.branchTur[1]:
                    json_file = value[2]
            with open(json_file, 'r', encoding='utf-8') as f:
                Dict = json.loads(f.read())
                Dict["category"]["contents"].pop(self.branchTur[2]-1)
            with open(json_file, 'w', encoding='utf-8') as f:
                f.write(json.dumps(Dict, indent=4, ensure_ascii=False))


class Add_label():
    def __init__(self, nameTur, positionTur,textContent,classname_fileUrl_dict):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.nameTur = nameTur #(大分支，小分支)
        self.positionTur = positionTur #(是否默认， 相对第几个，之前还是之后)
        self.textContent = textContent #标签内容
        self.classname_fileUrl_dict = classname_fileUrl_dict
    def generateLabel(self):
        addDict = {"kind": "label","text": self.textContent}
        for _, value in self.classname_fileUrl_dict.items():
            if value[4]==self.nameTur[0]:
                json_file = value[2]
                break
        with open(json_file, 'r', encoding='utf-8') as f:
            Dict = json.loads(f.read())
            if self.nameTur[1]=='无小分支':
                if self.positionTur[0]:
                    Dict["category"]["contents"].append(addDict)
                else:
                    Dict1, _ = findDict(Dict["category"]["contents"], self.positionTur[1])
                    Dict["category"]["contents"].insert(Dict["category"]["contents"].index(Dict1)+(0 if self.positionTur[2]=="之前" else 1), addDict)
            else:
                for index, dic in enumerate(Dict["category"]["contents"]):
                    if dic["name"]==self.nameTur[1]:
                        if self.positionTur[0]:
                            Dict["category"]["contents"][index]["contents"].append(addDict)
                        else:
                            Dict1, _ = findDict(Dict["category"]["contents"][index]["contents"], self.positionTur[1])
                            Dict["category"]["contents"][index]["contents"].insert(Dict["category"]["contents"][index]["contents"].index(Dict1)
                                                                                   +(0 if self.positionTur[2]=="之前" else 1), addDict)
        with open(json_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(Dict,  indent=4, ensure_ascii=False))

class DeleteLabel():
    def __init__(self, nameTur, index,classname_fileUrl_dict):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.nameTur = nameTur #(大分支，小分支)
        self.index = index
        self.classname_fileUrl_dict = classname_fileUrl_dict

    def deleteLabel(self):
        for key, value in self.classname_fileUrl_dict.items():
            if self.nameTur[0]==value[4]:
                json_file = value[2]
                break
        with open(json_file, 'r', encoding='utf-8') as f:
            Dict = json.loads(f.read())
            if self.nameTur[1]=="无小分支":
                temp = 0
                for index, dic in enumerate(Dict["category"]["contents"]):
                    if dic["kind"]=="label":
                        temp += 1
                        if temp==self.index:
                            break
                Dict["category"]["contents"].pop(index)
            else:
                for index, dic in enumerate(Dict["category"]["contents"]):
                    if dic["name"]==self.nameTur[1]:
                        break
                temp = 0
                for index1, dic in enumerate(Dict["category"]["contents"][index]["contents"]):
                    if dic["kind"] == "label":
                        temp += 1
                        if temp == self.index:
                            break
                Dict["category"]["contents"][index]["contents"].pop(index1)
            with open(json_file, 'w', encoding='utf-8') as f:
                f.write(json.dumps(Dict, indent=4, ensure_ascii=False))

class importBranch():
    def __init__(self,fileUrl, positionTur):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.fileUrl = fileUrl
        self.maxBranchNum = len([jsons for jsons in os.listdir(path+'jsons') if jsons.endswith('.json')])
        if positionTur[1]:
            self.position = ("0"*4+str(self.maxBranchNum+1))[-4:]
        else:
            self.position = ("0"*4+str(positionTur[0] + (1 if positionTur[2]=="之后" else 0)))[-4:]

    def formatDetect(self):
        filesList = os.listdir(self.fileUrl)
        for needFile in ['blocks', 'generators', 'jsons']:
            if needFile not in filesList:
                return 1, needFile+"不在文件夹里面"
        jsonFilesList = [jsonFile for jsonFile in os.listdir(os.path.join(self.fileUrl,"jsons")) if jsonFile.endswith(".json")]
        if len(jsonFilesList)==0:
            return 2, "jsons文件夹里面没有分支"
        elif len(jsonFilesList)==1:
            with open(os.path.join(self.fileUrl,"jsons",jsonFilesList[0]),'r',encoding='utf-8') as f:
                Dict = json.loads(f.read())
                self.blocksUrl = os.path.join(self.fileUrl,Dict["blocklyFilesUrls"][0][Dict["blocklyFilesUrls"][0].find("blocks"):])
                self.generatorUrl = os.path.join(self.fileUrl,Dict["blocklyFilesUrls"][1][Dict["blocklyFilesUrls"][1].find("generators"):])
                self.jsonsUrl = os.path.join(self.fileUrl,"jsons",jsonFilesList[0])

                for index, file in enumerate([self.blocksUrl,self.generatorUrl]):
                    if not os.path.exists(file):
                        return 3, file+"文件不存在"
                self.blocksName = Dict["blocklyFilesUrls"][0].split("blocks")[-1][1:] #blocks的文件名
                self.generatorsName = Dict["blocklyFilesUrls"][1].split("generators")[-1][1:] #generators的文件名
                self.jsonsName = jsonFilesList[0]
                return 0,"没有错误"
        else:
            return -1,"还没有考虑多个分支同时导入的情况"

    # def __isExist(self,fileUrl):
    #     if os.path.exists(fileUrl):
    #         if os.path.getsize(fileUrl) != 0: #文件存在且不为空
    #             return True
    #     return False

    def __changeOrigiFiles(self):
        jsonsPathList = ["".join([path, "jsons/", Path]) for Path in os.listdir(path + "jsons")]
        blocksPathList = ["".join([path, "blocks/", Path]) for Path in os.listdir(path + "blocks")]
        generatorsPathList = ["".join([path, "generators/", Path]) for Path in os.listdir(path + "generators")]
        #改名字
        for position in range(int(self.position) - 1, self.maxBranchNum):
            with open(jsonsPathList[position],'r',encoding="utf-8") as f:
                Dict = json.loads(f.read())
                for i in range(2):
                    PathStr = Dict['blocklyFilesUrls'][i]
                    Dict['blocklyFilesUrls'][i] = PathStr[:PathStr.rfind("/")+1] +\
                                                            ("0"*4+str(int(PathStr.split("/")[-1][:4])+1))[-4:]+\
                                                            PathStr.split("/")[-1][4:]
            with open(jsonsPathList[position],'w',encoding="utf-8") as f:
                f.write(json.dumps(Dict,  indent=4, ensure_ascii=False))
            os.rename(jsonsPathList[position], jsonsPathList[position][:jsonsPathList[position].rfind("/") + 1] +
                      ("0" * 4 + str(int(jsonsPathList[position].split("/")[-1][0:4]) + 1))[-4:] +
                      jsonsPathList[position].split("/")[-1][4:])
            os.rename(blocksPathList[position], blocksPathList[position][:blocksPathList[position].rfind("/") + 1] +
                      ("0" * 4 + str(int(blocksPathList[position].split("/")[-1][0:4]) + 1))[-4:] +
                      blocksPathList[position].split("/")[-1][4:])
            os.rename(generatorsPathList[position],
                      generatorsPathList[position][:generatorsPathList[position].rfind("/") + 1] +
                      ("0" * 4 + str(int(generatorsPathList[position].split("/")[-1][0:4]) + 1))[-4:] +
                      generatorsPathList[position].split("/")[-1][4:])

    def Import(self):
        #需要rename的是self.position:self.maxBranchNum
        self.__changeOrigiFiles()

        with open(path+"blocks/"+self.position+self.blocksName,'w',encoding='utf-8') as targetFile:
            with open(self.blocksUrl,'r',encoding='utf-8') as sourceFile:
                targetFile.write(sourceFile.read())

        with open(path+"generators/"+self.position+self.generatorsName,'w',encoding='utf-8') as targetFile:
            with open(self.generatorUrl,'r',encoding='utf-8') as sourceFile:
                targetFile.write(sourceFile.read())

        with open(path+"jsons/"+self.position+self.jsonsName,'w',encoding='utf-8') as targetFile:
            with open(self.jsonsUrl,'r',encoding='utf-8') as sourceFile:
                Dict = json.loads(sourceFile.read())
                Dict['blocklyFilesUrls'][0] ="../assets/blocklyFiles/blocks/"+self.position+self.blocksName
                Dict['blocklyFilesUrls'][1] = "../assets/blocklyFiles/generators/" + self.position + self.generatorsName
                targetFile.write(json.dumps(Dict,  indent=4, ensure_ascii=False))

class EmportBranch():
    def __init__(self,fileUrl, position):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.fileUrl = fileUrl #输出的路径
        self.position = position #要输出的分支是第几个
    def __getFolderName(self,FolderName):
        if os.path.exists(os.path.join(self.fileUrl,FolderName)):
            return self.__getFolderName(FolderName='outBranch'+str(int((FolderName.split("outBranch")[-1]))+1))
        return FolderName


    def Emport(self):
        FolderName = self.__getFolderName("outBranch0")
        os.mkdir(os.path.join(self.fileUrl,FolderName))
        jsonsName = [files for files in os.listdir(path + "jsons") if files.endswith(".json")][self.position-1]
        blocksName = [files for files in os.listdir(path + "blocks") if files.endswith(".js")][self.position-1]
        generatorsName = [files for files in os.listdir(path + "generators") if files.endswith(".js")][self.position-1]

        for folder in ["blocks","generators", "jsons"]:
            os.mkdir(os.path.join(self.fileUrl, FolderName,folder))
            with open(os.path.join(self.fileUrl, FolderName, folder, eval(folder+'Name')[4:]),'w',encoding='utf-8') as source:
                with open(os.path.join(os.path.join(path,folder,eval(folder+'Name'))),'r',encoding='utf-8') as target:
                        source.write(target.read())
        with open(os.path.join(self.fileUrl, FolderName, folder, jsonsName[4:]),'r',encoding='utf-8') as f:
            Dict = json.loads(f.read())
            for i in range(2):
                Str = Dict['blocklyFilesUrls'][i]
                Dict['blocklyFilesUrls'][i] =  Str[:Str.rfind("/")+1]+Str[Str.rfind("/")+5:]
        with open(os.path.join(self.fileUrl, FolderName, folder, jsonsName[4:]), 'w', encoding='utf-8') as f:
            f.write(json.dumps(Dict,  indent=4, ensure_ascii=False))
        return os.path.join(self.fileUrl,FolderName)

    def delete(self,Folder):
        delete_file(Folder)

class ModifyBlock():
    def __init__(self,branchNameTur,position, libNameTur,classNameTur,colorTur,NoChangeShape,
                 demoTur,contentTur,classname_fileUrl_dict):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.branchNameTur = branchNameTur
        self.position = position
        self.classNameTur = classNameTur
        self.libNameTur = libNameTur
        self.colorTur = colorTur
        self.NoChangeShape = NoChangeShape
        self.demoTur = demoTur
        self.contentTur = contentTur
        self.classname_fileUrl_dict = classname_fileUrl_dict
        for key,value in classname_fileUrl_dict.items():
            if value[4]==branchNameTur[0]:
                self.jsonPath = value[2]
                self.blockPath = value[0]
                self.generatorPath = value[1]
        self.deleter = Delete(branchNameTur,self.position,classname_fileUrl_dict)

    def getInfo(self,QBox):
        with open(self.jsonPath,'r',encoding='utf-8') as jsonFile:
            Dict = json.loads(jsonFile.read())
            #获取块的名字
            if self.branchNameTur[1]=="无小分支":
                self.targetDict = [block for block in Dict['category']['contents'] if block['kind']=='block'][
                    self.position-1]
            else:
                for index,smallBranch in enumerate(Dict['category']['contents']):
                    if smallBranch['name'] == self.branchNameTur[1]:
                        self.targetDict = [block for block in smallBranch['contents'] if block['kind'] == 'block'][
                            self.position - 1]
                        break
            start = self.targetDict['blockxml'].find("type")
            over = self.targetDict['blockxml'].find(">")
            self.blockName = self.targetDict['blockxml'][start + 6:over - 1] #得到块的名字

        # 获取blocks内容
        with open(self.blockPath, 'r', encoding='utf-8') as blockFile:
            start = None
            lines = blockFile.readlines()
            for index, line in enumerate(lines):
                if (start == None) and (('Blockly.Blocks.' + self.blockName + ' ' in line) or (
                        'Blockly.Blocks.' + self.blockName + '=' in line) or (
                                                'Blockly.Blocks' + "[\'" + self.blockName + "\']" in line) or (
                                                'Blockly.Blocks' + '[\"' + self.blockName + '\"]' in line)):
                    start = index
                    continue
                if start != None and 'Blockly.Blocks' in line:
                    end = index
                    break
            else:
                if start == None:
                    return False
                end = -1
            blockContent = lines[start:end]
            for line in blockContent:
                if "this.setOutput(true,null);" in line:
                    UpDown_connect = False
                    break
            else:
                UpDown_connect = True

            #修改颜色
            if self.colorTur[1]==False:
                self.color = '"'+('0'*6+self.colorTur[0])[-6:]+'"'
            else:
                for index,line in enumerate(blockContent):
                    if 'this.setColour(' in line:
                        break
                start1 = blockContent[index].find("(")
                over1 = blockContent[index].find(")")
                self.color = blockContent[index][start1+1:over1] #原本的颜色
            if self.contentTur[1]==True: #如果不修改块的内容
                for index,line in enumerate(blockContent):
                    if 'this.setColour(' in line:
                        break
                start1 = blockContent[index].find("(")
                over1 = blockContent[index].find(")")
                blockContent[index] =  blockContent[index][:start1+1] + str(self.color)  +blockContent[index][over1:]
                Content = lines[:start]+blockContent+lines[end:]
                blockFile.close()
                with open(self.blockPath, 'w', encoding='utf-8') as blockFile:
                    blockFile.writelines(Content)
            else:#修改块的内容
                self.deleter.name = self.blockName
                self.deleter.Delete_Blocks() #删除旧的块的内容
                write2blocks(self.blockName,content2List(self.contentTur[0][0]), #生成新的块的内容
                             (not UpDown_connect) if self.NoChangeShape==False else UpDown_connect,self.blockPath,self.color)

        ###########修改代码内容##############

        with open(self.generatorPath, 'r', encoding='utf-8') as generatorFile:
            start = None
            lines = generatorFile.readlines()
            for index, line in enumerate(lines):
                if (start == None) and (
                        ('Blockly.Python.' + self.blockName + ' ' in line) or (
                        'Blockly.Python.' + self.blockName + '=' in line) or (
                                'Blockly.Python' + "[\'" + self.blockName + "\']" in line) or (
                                'Blockly.Python' + "[\"" + self.blockName + "\"]" in line)):
                    start = index
                    continue
                if start != None and 'function' in line:
                    end = index
                    break
            else:
                if start == None:
                    return False
                end = - 1
            generatorContent = lines[start:end]
            #获取引用库名称和引用类名称
            for index,line in enumerate(generatorContent):
                if "import" in line:
                    if "from" in line:
                        LibName = line[line.find('from')+5:line.find("import")-1]
                        ClassName = line[line.find("import")+7:-3]
                    else:
                        ClassName = ''
                        LibName = line[line.find("import")+7:]
                    break
            else:
                index = -1
                LibName=''
                ClassName=''
            LibName = LibName if self.libNameTur[1] else self.libNameTur[0]
            ClassName = ClassName if self.classNameTur[1] else self.classNameTur[0]
            if self.demoTur[1]:
                if LibName and ClassName=='':
                    if index==-1:
                        generatorContent.insert(1,'Blockly.Python.definitions_[\'' + LibName + '\']=\'import ' + LibName + '\';\n ')
                    else:
                        for index1,line in enumerate(generatorContent):
                            if "Blockly.Python.definitions_" in line:
                                break
                        if index1 != index:
                            generatorContent.pop(index)
                        generatorContent[index1] = 'Blockly.Python.definitions_[\'' + LibName + '\']=\'import ' + LibName + '\';\n '
                elif LibName=='' and ClassName=='':
                    for index, line in enumerate(generatorContent):
                        if "Blockly.Python.definitions_" in line:
                            generatorContent.pop(index)
                            break
                    for index, line in enumerate(generatorContent):
                        if "import" in line:
                            generatorContent.pop(index)
                            break
                elif LibName and ClassName:
                    if index == -1:
                        generatorContent.insert(1,
                        'Blockly.Python.definitions_[\'' + LibName + '_' + ClassName + '\']=\'from ' + LibName + ' import ' + ClassName + '\';\n ')
                    else:
                        for index1,line in enumerate(generatorContent):
                            if "Blockly.Python.definitions_" in line:
                                break
                        if index1 != index:
                            generatorContent.pop(index)
                        generatorContent[index1] = 'Blockly.Python.definitions_[\'' + LibName + '_' + ClassName + '\']=\'from ' + LibName + ' import ' + ClassName + '\';\n '
                else:
                    QBox("错误","引用类名称不为空时，引用库名称不能为空")
                self.deleter.name = self.blockName
                self.deleter.Delete_generators()
                generatorFile.close()
                lines = lines[:start] + generatorContent + lines[end:]
                with open(self.generatorPath, 'a', encoding='utf-8') as generatorFile:
                    generatorFile.writelines(lines)
            else:
                self.deleter.name = self.blockName
                self.deleter.Delete_generators()
                write2generators(self.blockName,LibName,ClassName,addText(code2List(self.demoTur[0][0], LibName, ClassName)),
                                 (not UpDown_connect) if self.NoChangeShape == False else UpDown_connect,
                                 self.generatorPath,addText)

class ModifyBigBranchPosition():
    def __init__(self,bigBranchName,moveDirection,moveStep,classname_fileUrl_dict):
        save_copy(path, copy_path)  # 保存副本,用于撤回操作
        self.bigBranchName = bigBranchName
        self.moveDirection = moveDirection
        self.moveStep = moveStep * (1 if self.moveDirection=="下移" else -1)
        self.classname_fileUrl_dict = classname_fileUrl_dict
        for key,value in self.classname_fileUrl_dict.items():
            if value[4]==bigBranchName:
                self.blockPath = value[0]
                self.generatorPath = value[1]
                self.jsonPath = value[2]
                self.nowIndex =int(value[0].split("/")[-1][:4]) #目标大分支当前的序号
                self.targetIndex = self.nowIndex + self.moveStep
                if moveDirection=="下移":
                    self.needChangeOtherFileIndexList = list(range(self.nowIndex, self.targetIndex))
                else:
                    self.needChangeOtherFileIndexList = list(range(self.targetIndex-1,self.nowIndex-1))
                break
        fileNameList = [x for x in os.listdir(os.path.join(path,"jsons")) if x.endswith(".json")]
        self.needChangeOtherFilePathList = []
        for index in self.needChangeOtherFileIndexList:
            self.needChangeOtherFilePathList.append(os.path.join(path,"jsons",fileNameList[index]))
        self.changeSelf() #改变目标大分支
        self.changeOther()#改变其他大分支

    def changeSelf(self):
        with open(self.jsonPath,'r',encoding='utf-8') as jsonFile:
            Dict = json.loads(jsonFile.read())
            for i in range(2):
                PathStr = Dict['blocklyFilesUrls'][i]
                Dict['blocklyFilesUrls'][i] = PathStr[:PathStr.rfind("/") + 1] + \
                                              ("0" * 4 + str(int(PathStr.split("/")[-1][:4]) + self.moveStep))[-4:] + \
                                              PathStr.split("/")[-1][4:]
        with open(self.jsonPath, 'w', encoding='utf-8') as jsonFile:
            jsonFile.write(json.dumps(Dict, indent=4, ensure_ascii=False))
        os.rename(self.blockPath,self.blockPath[:self.blockPath.rfind("/") + 1] + \
                                          ("0" * 4 + str(int(self.blockPath.split("/")[-1][:4]) + self.moveStep))[-4:] + \
                                          self.blockPath.split("/")[-1][4:])
        os.rename(self.generatorPath, self.generatorPath[:self.generatorPath.rfind("/") + 1] + \
                  ("0" * 4 + str(int(self.generatorPath.split("/")[-1][:4]) + self.moveStep))[-4:] + \
                  self.generatorPath.split("/")[-1][4:])
        os.rename(self.jsonPath, self.jsonPath[:self.jsonPath.rfind("/") + 1] + \
                  ("0" * 4 + str(int(self.jsonPath.split("/")[-1][:4]) + self.moveStep))[-4:] + \
                  self.jsonPath.split("/")[-1][4:])

    def changeOther(self):
        for jsonPath in self.needChangeOtherFilePathList:
            jsonPath = jsonPath.replace("\\","/")
            with open(jsonPath, 'r', encoding='utf-8') as jsonFile:
                Dict = json.loads(jsonFile.read())
                blockPath = os.path.join(jsonPath.replace(r"\\", "/").split("assets")[0], Dict["blocklyFilesUrls"][0][3:])
                generatorPath = os.path.join(jsonPath.replace(r"\\", "/").split("assets")[0], Dict["blocklyFilesUrls"][1][3:])
                for i in range(2):
                    PathStr = Dict['blocklyFilesUrls'][i]
                    Dict['blocklyFilesUrls'][i] = PathStr[:PathStr.rfind("/") + 1] + \
                                                  ("0" * 4 + str(int(PathStr.split("/")[-1][:4]) +(1 if self.moveDirection=="上移" else -1)))[
                                                  -4:] + \
                                                  PathStr.split("/")[-1][4:]
            with open(jsonPath, 'w', encoding='utf-8') as jsonFile:
                jsonFile.write(json.dumps(Dict, indent=4, ensure_ascii=False))
            os.rename(blockPath, blockPath[:blockPath.rfind("/") + 1] + \
                      ("0" * 4 + str(int(blockPath.split("/")[-1][:4]) + (1 if self.moveDirection=="上移" else -1)))[-4:] + \
                      blockPath.split("/")[-1][4:])
            os.rename(generatorPath, generatorPath[:generatorPath.rfind("/") + 1] + \
                      ("0" * 4 + str(int(generatorPath.split("/")[-1][:4]) + (1 if self.moveDirection=="上移" else -1)))[-4:] + \
                      generatorPath.split("/")[-1][4:])
            os.rename(jsonPath, jsonPath[:jsonPath.rfind("/") + 1] + \
                      ("0" * 4 + str(int(jsonPath.split("/")[-1][:4]) + (1 if self.moveDirection=="上移" else -1)))[-4:] + \
                      jsonPath.split("/")[-1][4:])

