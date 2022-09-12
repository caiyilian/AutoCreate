import re

def code2List(code, used_lib, used_class): #把代码的内容转化成列表
    try:
        exec("".join(["from ", used_lib, " import ", used_class]))
    except:
        pass
    code_copy = code
    List = []
    if '=' in code:
        List.append(code[:code.find('=')])
        code_copy = code[code.find('('):]
    while True: #循环得到所有未定义的变量，也就是我们需要的变量
        try:
            try:
                exec(code_copy)  # 先执行一下这个语句，如果NameError，就表示有未定义的变量
                break  # 如果没有报错，就表示这个语句里面已经没有未定义的变量了,那就可以结束循环了
            except TypeError as e:
                if str(e) == "'NoneType' object is not callable":
                    fun = code_copy[:code_copy.find('(')]
                    code_copy = code_copy[code_copy.find(fun) + len(fun):]
                    List.remove(fun)
            except NameError as e:
                List.append(str(e)[6:-16])  # 报错了，那我们就根据报错信息得到这个未定义的变量
            exec(List[-1] + '=None') #为这个未定义的变量赋值None
        except AttributeError as e: #如果报这个错，就表示某个变量没有属性
            fun = str(e)[str(e)[:-1].rfind("'") + 1:-1] #这里一定会报错这个变量没有这个属性，因为这个变量我们是赋值为None，肯定是没有任何属性的
            code_copy = code_copy[code.find(fun) + len(fun):]
# 以上的功能是让程序执行报错部分的后面的部分代码，比如用户输入's.change_vol_spd_gender_DUI(MODE1, MODE2, MODE3, NUM1, STR1)'
# 那么我们会先报s没有定义，然后我们会s赋值None之后，继续执行就会报s没有change_vol_spd_gender_DUI这个属性，
# 这时候我们就要让程序跳过change_vol_spd_gender_DUI，而去执行(MODE1, MODE2, MODE3, NUM1, STR1)即可

    for index, var in enumerate(List):
        for Type in ['NUM', 'STR', 'MODE']:
            if Type in var:
                List[index] = (var, (code.find(var), code.find(var) + len(var)), Type)
                break
        else:
            List[index] = (var, (code.find(var), code.find(var) + len(var)), 'Var')
    pre_last = 0
    List_copy = List.copy()
    TEXT_NUM = 0
    index = 0
    for index, tur in enumerate(List):
        now_first = tur[1][0]
        if now_first != pre_last:
            List_copy.insert(index + TEXT_NUM, (code[pre_last:now_first], (pre_last, now_first), 'TEXT'))
            TEXT_NUM += 1
        pre_last = tur[1][1]

    if pre_last<len(code):
        List_copy.insert(index + TEXT_NUM+1, (code[pre_last:], (pre_last, len(code)), 'TEXT'))
    return List_copy

def content2List(content): #块的内容转化成列表
    List = []#创建一个列表，把块的内容转化为我们想要的格式之后，装到这个列表里面
    for mode in re.compile(r'[{](.*?)[}]').finditer(content):
        List.append((mode.group(), mode.span(), 'MODE')) #整理成我们想要的格式

    content_copy = content#复制一下块的内容

    for mode in List:
        ct = content_copy.replace(mode[0], '-' * len(mode[0])) #把复制的块的内容里面的所有跟模式有关的块比如{"100%":100, "50%":50}换成相同长度的-
    else:
        if List==[]:
            ct = content_copy
    for var in re.compile('[a-zA-Z_]{1}[a-zA-Z_\d]{0,}').finditer(ct): #提取替换之后的块的内容里面的所有单词，就是变量
        for Type in ['NUM', 'STR']: #是数字类型还是字符串类型
            if Type in var.group():
                List.append((var.group(), var.span(), Type)) #整理成我们想要的格式
                break
        else:#如果都不是，就是普通的变量类型
            List.append((var.group(), var.span(), 'Var'))
    List = sorted(List, key=lambda x: x[1][0]) #为我们排一下序
    List_copy = List.copy() #复制一下这个列表，因为我们将对列表的内容进行修改，为了不影响循环的进行所以不能修改循环主体的列表
    pre_last = 0
    TEXT_NUM = 0
    index = 0 #如果不初始化为0，如果块里面没有变量，就会报错
    for index, tur in enumerate(List): #把非变量类型的，也就是文本类型的提取出来
        now_first = tur[1][0]
        if now_first != pre_last:
            List_copy.insert(index + TEXT_NUM, (content[pre_last:now_first], (pre_last, now_first), 'TEXT'))
            TEXT_NUM += 1
        pre_last = tur[1][1]
    if pre_last<len(content):
        List_copy.insert(index + TEXT_NUM+1, (content[pre_last:], (pre_last, len(content)), 'TEXT'))
    return List_copy

def write2blocks(name,Content,UpDown_connect,blocks_file,color):
    Block_str = '\n\nBlockly.Blocks["' + name + '"]={\n  init: function () {\n  this.setColour(' + color + ');\n  '
    mode = 1
    for Str in Content:
        if (Str[2] == 'TEXT') and Str[0] != '':
            Block_str += 'this.appendDummyInput().appendField(\'' + Str[0] + '\');\n  '
        elif Str[2] == 'Var':
            Block_str += 'this.appendValueInput(\'' + Str[0] + '\').setCheck(\'var\');\n  '
        elif Str[2] == 'NUM':
            Block_str += 'this.appendValueInput(\'' + Str[0] + '\', Number).setCheck(\'Number\');\n  '
        elif Str[2] == 'STR':
            Block_str += 'this.appendValueInput(\'' + Str[0] + '\',String).setCheck(\'String\')\n  '
        elif Str[2] == 'MODE':
            Block_str += 'var MODE' + str(mode) + '=' + str([list(mode) for mode in eval(Str[0]).items()])
            Block_str += ';\n  this.appendDummyInput(\'\').appendField(new Blockly.FieldDropdown(MODE' + str(
                mode) + '),\'MODE' + str(mode) + '\');\n  '
            mode += 1

    if UpDown_connect:
        Block_str += 'this.setInputsInline(true);\n  this.setPreviousStatement(true, null);\n  this.setNextStatement(true, null);\n  },\n};'
    else:
        Block_str += 'this.setInputsInline(true);\n  this.setOutput(true);\n  },  \n};\n'

    # 写入文件里面
    print(blocks_file)
    with open(blocks_file, 'a', encoding='utf-8') as f:
        f.write(Block_str)
        
def write2generators(name,used_lib,used_class,Demo,UpDown_connect,generators_file,addText):
    Generator_str = '\n\nBlockly.Python["' + name + '"]= function () {\n  '
    if (used_lib) and (used_class):
        Generator_str += 'Blockly.Python.definitions_[\'' + used_lib + '_' + used_class + '\']=\'from ' + used_lib + ' import ' + used_class + '\';\n '
    elif used_lib:
        Generator_str += 'Blockly.Python.definitions_[\'' + used_lib + '\']=\'import ' + used_lib + '\';\n '

    for Str in Demo:
        if Str[2] in ['Var', 'STR', 'NUM']:
            Generator_str += 'var ' + Str[0] + '=Blockly.Python.valueToCode(this,\'' + Str[
                0] + '\',Blockly.Python.ORDER_ATOMIC);\n  '
        elif Str[2] == 'MODE':
            Generator_str += 'var ' + Str[0] + '=this.getFieldValue(\'' + Str[0] + '\');\n'
    Generator_str += 'var code='
    Demo = addText(Demo)
    for i, Code in enumerate(Demo):
        if Code[2] == "TEXT":
            Generator_str += '\'' + Code[0] + '\''
        else:
            Generator_str += ('' if i == 0 else '+') + Code[0] + (
                '+' if i != len(Demo) - 1 else '')  # 如果变量是开头就不用在其前面加上加号，在结尾就不用在其后面加上加号
        if i == len(Demo) - 1:
            if UpDown_connect:
                Generator_str += '+\'' + r'\n' + '\';\n ' + (
                    'return code;\n};')
            else:
                Generator_str += '+\'' + '\';\n ' + (
                    'return [code, Blockly.Python.ORDER_ATOMIC];\n};')

    # 写入文件里面
    with open(generators_file, 'a', encoding='utf-8') as f:
        f.write(Generator_str)
