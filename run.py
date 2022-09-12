import os,sys
dirname = os.path.dirname(os.path.realpath(sys.executable))
plugin_path = os.path.join(dirname, 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
from add import Ui_MainWindow
from operate import Operate, Delete,revoke_operate, classname_fileUrl, \
    Add_bigBranch,path,Add_smallBranch, DeleteBranch, Add_label, DeleteLabel,\
    importBranch,EmportBranch,ModifyBlock,ModifyBigBranchPosition
from PySide2.QtWidgets import QApplication,QMainWindow,  QMessageBox,QColorDialog,QFileDialog



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化界面
        #############增加块####################
        self.addBlockExampleButtom = self.ui.addBlockExampleButtom  # 实例那个按钮
        self.addBlockClearButtom = self.ui.addBlockClearButtom  # 清空的那个按钮
        self.addBlockBranchComboBox1 = self.ui.addBlockBranchComboBox1  # 增加块那个页面所在分支名称的那个文本框的右边那个下拉框1
        self.addBlockBranchComboBox2 = self.ui.addBlockBranchComboBox2 # 增加块那个页面所在分支名称的那个文本框的右边那个下拉框2
        self.addBlockLibName = self.ui.addBlockLibName  # 引用库名称的那个文本框
        self.addBlockClassName = self.ui.addBlockClassName  # 引用类名称的那个文本框
        self.addBlockCodeTextEdit = self.ui.addBlockCodeTextEdit  # 代码
        self.addBlockContentTextEdit = self.ui.addBlockContentTextEdit  # 块的内容
        self.addBlockGeneraButtom = self.ui.addBlockGeneraButtom  # 开始生成编程块
        self.addBlockBackButtom = self.ui.addBlockBackButtom  # 生成块界面的返回到上一步
        self.addBlockPositionSpinBox = self.ui.addBlockPositionSpinBox #块的创建位置相对与哪个块的那个数字框
        self.addBlockPositionComboBox = self.ui.addBlockPositionComboBox #块的创建相对那个块之前还是之后
        self.addBlockPositionCheckBox = self.ui.addBlockPositionCheckBox  # 默认把生成的块放在最后
        self.addBlockColorButtom = self.ui.addBlockColorButtom #选择块的颜色按钮
        self.addBlockColorSpinBox = self.ui.addBlockColorSpinBox #块的颜色值
        self.addBlockColorCheckBox = self.ui.addBlockColorCheckBox #是否让块的颜色保持默认
        #####################################

        #############删除块/分支####################
        #删除块
        self.deleteBlockBranchComboBox1 = self.ui.deleteBlockBranchComboBox1  # 删除块所在类名称的那个文本框的右边那个下拉框1
        self.deleteBlockBranchComboBox2 = self.ui.deleteBlockBranchComboBox2 # 删除块所在类名称的那个文本框的右边那个下拉框2
        self.deleteBlockPositionSpinBox = self.ui.deleteBlockPositionSpinBox #要删除的序号
        self.deleteBlockDeleteButtom = self.ui.deleteBlockDeleteButtom  # 删除块那个按钮
        self.deleteBlockBackButtom = self.ui.deleteBlockBackButtom #删除块/分支界面的返回到上一步
       #删除大分支
        self.deleteBigBranchComboBox = self.ui.deleteBigBranchComboBox #删除第几个大分支
        self.deleteBigBranchButtom = self.ui.deleteBigBranchButtom #删除大分支按钮
        #删除小分支
        self.deleteSmallBranchName = self.ui.deleteSmallBranchName #要删除的小分支所在大分支
        self.deleteSmallBranchName2 = self.ui.deleteSmallBranchName2 #删除的小分支的名字
        self.deleteSmallBranchButtom = self.ui.deleteSmallBranchButtom #删除小分支按钮
        #####################################

        #############增加分支####################
        #增加大分支
        self.addBigBrachPotionSpinBox = self.ui.addBigBrachPotionSpinBox #创建的位置相对第几个分支
        self.addBigBrachPotionComboBox = self.ui.addBigBrachPotionComboBox #创建的位置相对上面选的那个块的前面还是后面
        self.addBigBrachPotionCheckBox = self.ui.addBigBrachPotionCheckBox #生成的分支是否默认放在最后面


        self.addBigBrachName = self.ui.addBigBrachName #要创建的大分支的名字
        self.addBigBrachColorButtom = self.ui.addBigBrachColorButtom #选择大分支颜色的按钮
        self.addBigBrachColorSpinBox = self.ui.addBigBrachColorSpinBox #选择的大分支的颜色值
        self.addBigBrachNameButtom = self.ui.addBigBrachNameButtom #开始生成新的大分支按钮
        self.addSmallBrachBackButtom = self.ui.addSmallBrachBackButtom #生成大分支页面的返回上一步按钮
        self.addBigBrachFileName = self.ui.addBigBrachFileName #造新分支需要产生新文件，这个是文件名
        self.addBigBrachNameCheckBox = self.ui.addBigBrachNameCheckBox #是否需要给新产生的文件随机取名字


        #增加小分支
        self.addSmallBrachColorButtom = self.ui.addSmallBrachColorButtom #选择小分支颜色
        self.addSmallBrachColorSpinBox = self.ui.addSmallBrachColorSpinBox  # 选择小分支的颜色值
        self.addSmallBrachPotionComboBox = self.ui.addSmallBrachPotionComboBox #小分支创建在哪个大分支上
        self.addSmallBrachPotionSpinBox = self.ui.addSmallBrachPotionSpinBox #分支创建在那个选定大分支的第几个位置
        self.addSmallBrachName = self.ui.addSmallBrachName #创建的小分支的名字
        self.addSmallBrachGeneraButtom = self.ui.addSmallBrachGeneraButtom#创建小分支按钮
        #######################################

        #############增/删标签####################
        #增加标签
        self.addLabelBranchComboBox1 = self.ui.addLabelBranchComboBox1 #所在分支名字
        self.addLabelPositionSpinBox = self.ui.addLabelPositionSpinBox #标签创建位置相对某个块
        self.addLabelPositionComboBox = self.ui.addLabelPositionComboBox #分支创建在那个块之前还是之后
        self.addLabelContent = self.ui.addLabelContent #标签内容
        self.addLabelButtom = self.ui.addLabelGenraButtom #增加标签按钮
        self.addLabelComboBox2 = self.ui.addLabelBranchComboBox2 #增加标签的那个下拉框2
        self.addLabelPositionCheckBox = self.ui.addLabelPositionCheckBox #默认放在最后面
        self.addLabelBackButtom = self.ui.addLabelBackButtom #增加标签的那个页面的返回上一步按钮
        #删除标签
        self.deleteLabelBranchComboBox1 = self.ui.deleteLabelBranchComboBox1 #所在分支名字
        self.deleteLabelPositionSpinBox = self.ui.deleteLabelPositionSpinBox #要删除第几个标签
        self.deleteLabelDeleteButtom = self.ui.deleteLabelDeleteButtom #删除标签按钮
        self.deleteLabelBranchComboBox2 = self.ui.deleteLabelBranchComboBox2 #删除标签的那个下拉框2
        ###############导入/导出大分支##############
        self.importBranchFileUrl = self.ui.importBranchFileUrl
        self.importBranchSelectButtom = self.ui.importBranchSelectButtom
        self.importBranchPosition = self.ui.importBranchPosition
        self.importBranchCheckBox = self.ui.importBranchCheckBox
        self.importBranchPositionComboBox = self.ui.importBranchPositionComboBox
        self.importBranchGerateButtom = self.ui.importBranchGerateButtom
        self.exportBranchFileUrl = self.ui.exportBranchFileUrl
        self.exportBranchSelectButtom = self.ui.exportBranchSelectButtom
        self.exportBranchGeneraButtom = self.ui.exportBranchGeneraButtom
        self.exportBranchComboBox = self.ui.exportBranchComboBox
        ###############修改块##############
        self.modifyBlockBranchComboBox1 = self.ui.modifyBlockBranchComboBox1
        self.modifyBlockBranchComboBox2 = self.ui.modifyBlockBranchComboBox2
        self.modifyBlockPositionSpinBox = self.ui.modifyBlockPositionSpinBox
        self.modifyBlockLibName = self.ui.modifyBlockLibName
        self.modifyBlockClassName = self.ui.modifyBlockClassName
        self.modifyBlockColorButtom = self.ui.modifyBlockColorButtom
        self.modifyBlockColorSpinBox = self.ui.modifyBlockColorSpinBox
        self.modifyBlockConnectCheckBox = self.ui.modifyBlockConnectCheckBox
        self.modifyBlockCodeTextEdit = self.ui.modifyBlockCodeTextEdit
        self.modifyBlockContentTextEdit = self.ui.modifyBlockContentTextEdit
        self.modifyBlockCodeCheckBox = self.ui.modifyBlockCodeCheckBox
        self.modifyBlockContentCheckBox = self.ui.modifyBlockContentCheckBox
        self.modifyBlockModifyButtom = self.ui.modifyBlockModifyButtom
        self.modifyBlockColorCheckBox = self.ui.modifyBlockColorCheckBox
        self.modifyBlockLibCheckBox =self.ui.modifyBlockLibCheckBox
        self.modifyBlockClassCheckBox = self.ui.modifyBlockClassCheckBox
        ###############修改大分支位置##############
        self.modifyBranchPositionComboBox = self.ui.modifyBranchPositionComboBox
        self.modifyBranchPositionSpinBox = self.ui.modifyBranchPositionSpinBox
        self.modifyBranchPositionButtom = self.ui.modifyBranchPositionButtom
        self.modifyBranchNameComboBox = self.ui.modifyBranchNameComboBox
        #######################################
        self.init() #初始化
        self.bind() #绑定事件
        self.show() #展示窗口

    def init(self):
        try:
            self.add_classname()
        except:
            QMessageBox.about(self, '找不到文件', '你要确定你的blocklyFiles存在而且放对地方了')
            exit()
        ##增加块##
        self.addBlockPositionCheckBox.setChecked(True)
        self.addBlockPositionSpinBox.setEnabled(False)
        self.addBlockPositionComboBox.setEnabled(False)
        self.addBlockColorCheckBox.setChecked(True)
        self.addBlockColorButtom.setEnabled(False)
        self.addBlockColorSpinBox.setEnabled(False)
        ##增加大分支##
        self.addBigBrachPotionCheckBox.setChecked(True)
        self.addBigBrachPotionSpinBox.setEnabled(False)
        self.addBigBrachPotionComboBox.setEnabled(False)
        self.addBigBrachNameCheckBox.setChecked(True)
        self.addBigBrachFileName.setEnabled(False)
        ########给下拉框加东西###################
        self.addBigBranchName(self.addBlockBranchComboBox1, self.deleteBlockBranchComboBox1, self.addLabelBranchComboBox1,
                              self.deleteLabelBranchComboBox1, self.addSmallBrachPotionComboBox,
                              self.deleteSmallBranchName, self.modifyBlockBranchComboBox1,self.exportBranchComboBox,
                              self.deleteBigBranchComboBox,self.modifyBranchNameComboBox)
        self.addSmallBranchName(self.addBlockBranchComboBox1, self.addBlockBranchComboBox2)
        self.addSmallBranchName(self.deleteBlockBranchComboBox1, self.deleteBlockBranchComboBox2)
        self.addSmallBranchName(self.addLabelBranchComboBox1, self.addLabelComboBox2)
        self.addSmallBranchName(self.deleteLabelBranchComboBox1, self.deleteLabelBranchComboBox2)
        self.addSmallBranchName(self.modifyBlockBranchComboBox1, self.modifyBlockBranchComboBox2)
        self.addSmallBranchName(self.deleteSmallBranchName, self.deleteSmallBranchName2)
        #增加标签
        self.addLabelPositionCheckBox.setChecked(True)
        self.addLabelPositionSpinBox.setEnabled(False)
        self.addLabelPositionComboBox.setEnabled(False)
        #导入/导出大分支
        self.importBranchPosition.setEnabled(False)
        self.importBranchCheckBox.setChecked(True)
        #####修改块#######
        self.modifyBlockLibName.setEnabled(False)
        self.modifyBlockClassName.setEnabled(False)
        self.modifyBlockColorSpinBox.setEnabled(False)
        self.modifyBlockColorButtom.setEnabled(False)
        self.modifyBlockCodeTextEdit.setEnabled(False)
        self.modifyBlockContentTextEdit.setEnabled(False)
        ######删除小分支#######
        self.deleteSmallBranchButtom.setEnabled(False)
        #####修改大分支#####
        self.modifyBranchPositionFun()

        self.setMax()

    def update(self,reflashBranch=False):
        if ".idea" in os.listdir(path + "/jsons"):
            os.remove("idea")
        self.add_classname()
        for bigBranchName in list(self.classname_fileUrl_dict.values()):
            self.bigBranchDict[bigBranchName[4]] = [0]
        for bigBranchName in list(self.classname_fileUrl_dict.values()):
            if bigBranchName[4] != bigBranchName[5]:
                self.bigBranchDict[bigBranchName[4]][0] += 1
                self.bigBranchDict[bigBranchName[4]].append([bigBranchName[5], bigBranchName[3]])
            else:
                self.bigBranchDict[bigBranchName[4]].append(bigBranchName[3])
        self.setMax()
        if reflashBranch:
            self.reflashBigBranchName(self.addBlockBranchComboBox1, self.deleteBlockBranchComboBox1,
                                      self.addLabelBranchComboBox1,
                                      self.deleteLabelBranchComboBox1, self.addSmallBrachPotionComboBox,
                                      self.deleteSmallBranchName, self.modifyBlockBranchComboBox1,
                                      self.exportBranchComboBox,
                                      self.deleteBigBranchComboBox, self.modifyBranchNameComboBox)

    def setMax(self):
        self.totalBigBranchLength = len(os.listdir(path + "/jsons")) - (0 if ".idea" not in os.listdir(path) else 1)
        #########给数字框设置最值################
        self.change_max(self.addBlockPositionSpinBox, self.addBlockBranchComboBox1, self.addBlockBranchComboBox2, changeSmall=True)
        self.change_max(self.modifyBlockPositionSpinBox, self.modifyBlockBranchComboBox1, self.modifyBlockBranchComboBox2,
                        changeSmall=True)
        self.change_max(self.addSmallBrachPotionSpinBox, self.addSmallBrachPotionComboBox, None)
        self.change_max(self.deleteBlockPositionSpinBox, self.deleteBlockBranchComboBox1, self.deleteBlockBranchComboBox2)
        # self.change_max(self.deleteSmallBranchPosition, self.deleteSmallBranchName, None, delete=True,buttom=self.deleteSmallBranchButtom)
        self.change_max(self.addLabelPositionSpinBox, self.addLabelBranchComboBox1, self.addLabelComboBox2,
                        changeSmall=True, labelMode=True)
        self.change_max(self.deleteLabelPositionSpinBox, self.deleteLabelBranchComboBox1,
                                self.deleteLabelBranchComboBox2, changeSmall=True, labelMode=True)
        self.addBigBrachPotionSpinBox.setMaximum(
            self.totalBigBranchLength
        )
        # self.deleteBigBranchPosition.setMaximum(
        #     len(os.listdir(path + "/jsons")) - (0 if ".idea" not in os.listdir(path) else 1))
        self.importBranchPosition.setMaximum(
            self.totalBigBranchLength
        )
        # self.exportBranchSpinBox.setMaximum(
        #     len(os.listdir(path + "/jsons")) - (0 if ".idea" not in os.listdir(path) else 1))


    def bind(self,onlyComBoBox=False):
        if onlyComBoBox:
            self.addBlockBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.addBlockPositionSpinBox, self.addBlockBranchComboBox1,
                                        self.addBlockBranchComboBox2, changeSmall=True))
            self.modifyBlockBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.modifyBlockPositionSpinBox, self.modifyBlockBranchComboBox1,
                                        self.modifyBlockBranchComboBox2, changeSmall=True))
            self.deleteBlockBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.deleteBlockPositionSpinBox,
                                        self.deleteBlockBranchComboBox1, self.deleteBlockBranchComboBox2,
                                        changeSmall=True))
            self.addLabelBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.addLabelPositionSpinBox, self.addLabelBranchComboBox1,
                                        self.addLabelComboBox2,
                                        changeSmall=True, labelMode=True)
            )
            self.deleteLabelBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.deleteLabelPositionSpinBox, self.deleteLabelBranchComboBox1,
                                        self.deleteLabelBranchComboBox2, changeSmall=True, labelMode=True,
                                        deleteLabel=True, buttom=self.deleteLabelDeleteButtom)
            )
            self.modifyBranchNameComboBox.currentTextChanged.connect(self.modifyBranchPositionFun)
            self.addSmallBrachPotionComboBox.currentTextChanged.connect(
                lambda: self.change_max(self.addSmallBrachPotionSpinBox, self.addSmallBrachPotionComboBox, None))
            self.deleteSmallBranchName.currentTextChanged.connect(
                lambda: self.change_max(None, self.deleteSmallBranchName, self.deleteSmallBranchName2,
                                        changeSmall=True, deleteSmallBranch=True)
            )
        else:
            ##增加块
            self.addBlockExampleButtom.clicked.connect(self.set_example)
            self.addBlockClearButtom.clicked.connect(self.clearAll)
            self.addBlockColorButtom.clicked.connect(lambda :self.showDialog(self.addBlockColorSpinBox))
            self.addBlockColorCheckBox.stateChanged.connect(
                lambda :self.checkChange(self.addBlockColorButtom, self.addBlockColorSpinBox, checkBox=self.addBlockColorCheckBox))
            self.addBlockPositionCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.addBlockPositionComboBox, self.addBlockPositionSpinBox,
                                         checkBox=self.addBlockPositionCheckBox))
            self.addBlockBackButtom.clicked.connect(self.revoke)
            self.addBlockGeneraButtom.clicked.connect(self.generate_Block)
            self.addBlockBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.addBlockPositionSpinBox, self.addBlockBranchComboBox1,
                                        self.addBlockBranchComboBox2, changeSmall=True))
            self.addBlockBranchComboBox2.currentTextChanged.connect(
                lambda: self.change_max(self.addBlockPositionSpinBox, self.addBlockBranchComboBox1, self.addBlockBranchComboBox2))

            ##增加分支
            self.addSmallBrachColorButtom.clicked.connect(lambda :self.showDialog(self.addSmallBrachColorSpinBox)) #增加小分支
            self.addSmallBrachGeneraButtom.clicked.connect(self.generate_smallBranch)
            self.addSmallBrachPotionComboBox.currentTextChanged.connect(
                lambda: self.change_max(self.addSmallBrachPotionSpinBox, self.addSmallBrachPotionComboBox, None))
            self.addBigBrachNameCheckBox.stateChanged.connect(lambda:self.checkChange(self.addBigBrachFileName, checkBox=self.addBigBrachNameCheckBox))#增加大分支
            self.addBigBrachColorButtom.clicked.connect(lambda :self.showDialog(self.addBigBrachColorSpinBox))#增加大分支
            self.addBigBrachNameButtom.clicked.connect(self.generate_bigBranch)#增加大分支
            self.addSmallBrachBackButtom.clicked.connect(self.revoke) #增加大分支
            self.addBigBrachPotionCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.addBigBrachPotionComboBox, self.addBigBrachPotionSpinBox,
                                         checkBox=self.addBigBrachPotionCheckBox)) #增加大分支
            #删除块
            self.deleteBlockBackButtom.clicked.connect(self.revoke)
            self.deleteBlockDeleteButtom.clicked.connect(self.delete_Block)
            self.deleteBlockBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.deleteBlockPositionSpinBox,
                                        self.deleteBlockBranchComboBox1, self.deleteBlockBranchComboBox2, changeSmall=True))
            self.deleteBlockBranchComboBox2.currentTextChanged.connect(
                lambda: self.change_max(self.deleteBlockPositionSpinBox, self.deleteBlockBranchComboBox1, self.deleteBlockBranchComboBox2))

            #删除小分支
            self.deleteSmallBranchButtom.clicked.connect(self.delete_smallBranch)
            # self.deleteSmallBranchName.currentTextChanged.connect(
            #     lambda :self.change_max(self.deleteSmallBranchPosition, self.deleteSmallBranchName, None,delete = True, buttom=self.deleteSmallBranchButtom)
            # )
            self.deleteSmallBranchName.currentTextChanged.connect(
                lambda: self.change_max(None, self.deleteSmallBranchName, self.deleteSmallBranchName2,
                                        changeSmall=True,deleteSmallBranch=True)
            )



            #增加标签
            self.addLabelBackButtom.clicked.connect(self.revoke)
            self.addLabelBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.addLabelPositionSpinBox, self.addLabelBranchComboBox1, self.addLabelComboBox2,
                                        changeSmall=True,labelMode=True)
            )
            self.addLabelButtom.clicked.connect(self.generate_label)
            self.addLabelComboBox2.currentTextChanged.connect(
                lambda: self.change_max(self.addLabelPositionSpinBox, self.addLabelBranchComboBox1, self.addLabelComboBox2,
                                        labelMode=True)
            )
            self.addLabelPositionCheckBox.stateChanged.connect(lambda:self.checkChange(self.addLabelPositionComboBox, self.addLabelPositionSpinBox, checkBox=self.addLabelPositionCheckBox))
            #删除标签
            self.deleteLabelDeleteButtom.clicked.connect(self.delete_label)
            self.deleteLabelBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.deleteLabelPositionSpinBox, self.deleteLabelBranchComboBox1,
                                        self.deleteLabelBranchComboBox2, changeSmall=True, labelMode=True, deleteLabel=True,buttom=self.deleteLabelDeleteButtom)
            )
            self.deleteLabelBranchComboBox2.currentTextChanged.connect(
                lambda: self.change_max(self.deleteLabelPositionSpinBox, self.deleteLabelBranchComboBox1,
                                        self.deleteLabelBranchComboBox2, changeSmall=False, labelMode=True, deleteLabel=True, buttom=self.deleteLabelDeleteButtom)
            )

            #删除大分支
            self.deleteBigBranchButtom.clicked.connect(self.delete_bigBranch)
            #导入/导出分支
            self.importBranchSelectButtom.clicked.connect(lambda :self.choose_file(self.importBranchFileUrl))
            self.exportBranchSelectButtom.clicked.connect(lambda: self.choose_file(self.exportBranchFileUrl))
            self.importBranchGerateButtom.clicked.connect(self.import_branch)
            self.exportBranchGeneraButtom.clicked.connect(self.export_branch)

            self.importBranchCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.importBranchPositionComboBox, self.importBranchPosition,
                                         checkBox=self.importBranchCheckBox))  # 增加大分支
            #修改块
            self.modifyBlockColorButtom.clicked.connect(lambda: self.showDialog(self.modifyBlockColorSpinBox))
            self.modifyBlockModifyButtom.clicked.connect(self.modify_block)
            self.modifyBlockBranchComboBox1.currentTextChanged.connect(
                lambda: self.change_max(self.modifyBlockPositionSpinBox, self.modifyBlockBranchComboBox1,
                                        self.modifyBlockBranchComboBox2, changeSmall=True))
            self.modifyBlockBranchComboBox2.currentTextChanged.connect(
                lambda: self.change_max(self.modifyBlockPositionSpinBox, self.modifyBlockBranchComboBox1,
                                        self.modifyBlockBranchComboBox2))
            self.modifyBlockLibCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.modifyBlockLibName, checkBox=self.modifyBlockLibCheckBox))
            self.modifyBlockClassCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.modifyBlockClassName, checkBox=self.modifyBlockClassCheckBox))
            self.modifyBlockColorCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.modifyBlockColorSpinBox, self.modifyBlockColorButtom,checkBox=self.modifyBlockColorCheckBox))
            self.modifyBlockCodeCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.modifyBlockCodeTextEdit, checkBox=self.modifyBlockCodeCheckBox))
            self.modifyBlockContentCheckBox.stateChanged.connect(
                lambda: self.checkChange(self.modifyBlockContentTextEdit, checkBox=self.modifyBlockContentCheckBox))
            #修改大分支位置
            self.modifyBranchNameComboBox.currentTextChanged.connect(self.modifyBranchPositionFun)
            self.modifyBranchPositionComboBox.currentTextChanged.connect(self.modifyBranchPositionFun)
            self.modifyBranchPositionButtom.clicked.connect(self.modify_BigBranch_Position)



    def choose_file(self,BranchFileUrl):
        BranchFileUrl.setText(QFileDialog.getExistingDirectory(QMainWindow(), "选择文件夹"))   # 选择目录，返回选中的路径


    def checkChange(self, *components, checkBox):
        for component in components:
            component.setEnabled(not checkBox.isChecked())

    def showDialog(self, colorNum):#选择颜色
        col = QColorDialog.getColor()
        colorNum.setValue(int(col.name()[1:], 16))

    def set_example(self):
        self.addBlockLibName.setText('control')
        self.addBlockClassName.setText('shijue1')
        self.addBlockCodeTextEdit.setPlainText('print(a, b, NUM1, NUM2, STR1, MODE1)')
        self.addBlockContentTextEdit.setPlainText('打印变量a和变量b和数字NUM1和数字NUM2和字符串STR1的值，选择的模式是{"模式一":"mode1", "模式二":"mode2"}')

    def clearAll(self):
        self.addBlockLibName.setText('')
        self.addBlockClassName.setText('')
        self.addBlockCodeTextEdit.setPlainText('')
        self.addBlockContentTextEdit.setPlainText('')

    def change_max(self, spinBox, BigcomboBox, SmallcomboBox, changeSmall=False, labelMode=False,delete = False, buttom=False,
                   deleteLabel = False,deleteSmallBranch = False): #把要删除块的序号的最大值跟其所在类的块的数量对应起来
        if deleteSmallBranch == False:
            if changeSmall == True:
                self.addSmallBranchName(BigcomboBox, SmallcomboBox)
            if SmallcomboBox != None:
                if self.bigBranchDict[BigcomboBox.currentText()][0] ==0:
                    spinBox.setMaximum(self.bigBranchDict[BigcomboBox.currentText()][1][1 if labelMode else 0])
                else:
                    for List in self.bigBranchDict[BigcomboBox.currentText()][1:]:
                        if List[0]==SmallcomboBox.currentText():
                            spinBox.setMaximum(List[1][1 if labelMode else 0])
                            break
            else:
                spinBox.setMaximum(self.bigBranchDict[BigcomboBox.currentText()][1 if labelMode else 0]+1)
            if delete:
                spinBox.setMaximum(spinBox.maximum()-1)
                if spinBox.maximum()==0:
                    spinBox.setEnabled(False)
                    buttom.setEnabled(False)
                else:
                    spinBox.setMinimum(1)
                    spinBox.setEnabled(True)
                    buttom.setEnabled(True)
            if deleteLabel:
                if self.bigBranchDict[BigcomboBox.currentText()][0]==0:
                    if self.bigBranchDict[BigcomboBox.currentText()][1][1]==0:
                        spinBox.setEnabled(False)
                        buttom.setEnabled(False)
                    else:
                        spinBox.setEnabled(True)
                        buttom.setEnabled(True)
                        spinBox.setMinimum(1)
                else:
                    for name in self.bigBranchDict[self.deleteLabelBranchComboBox1.currentText()][1:]:
                        if name[0]==SmallcomboBox.currentText():
                            if name[1][1]==0:
                                spinBox.setEnabled(False)
                                buttom.setEnabled(False)
                            else:
                                spinBox.setEnabled(True)
                                buttom.setEnabled(True)
                                spinBox.setMinimum(1)
                            break
        else:
            self.addSmallBranchName(BigcomboBox, SmallcomboBox)
            if SmallcomboBox.count()==1:
                self.deleteSmallBranchButtom.setEnabled(False)
            else:
                self.deleteSmallBranchButtom.setEnabled(True)

    def add_classname(self, *comboBoxs):
        self.classname_fileUrl_dict = classname_fileUrl()
        if isinstance(self.classname_fileUrl_dict, str): #如果有一个json文件里面有错误，不符合json格式，就会报错，比如多了或者少了个逗号
            QMessageBox.about(self, '错误', self.classname_fileUrl_dict+"文件有错误，去检查一下，可能是少了个逗号或者其他情况")
            exit()
        self.find_haveBranch()#查找哪个类有多个分支
        for comboBox in comboBoxs:
            comboBox.addItems(list(self.classname_fileUrl_dict.keys()))




    def addBigBranchName(self, *comboBoxs): #找出所有的大分支并赋予给下拉框
        self.bigBranchDict = {}
        for comboBox in comboBoxs:
            for bigBranchName in list(self.classname_fileUrl_dict.values()):
                self.bigBranchDict[bigBranchName[4]] = [0]
            for bigBranchName in list(self.classname_fileUrl_dict.values()):
                if bigBranchName[4] != bigBranchName[5]:
                    self.bigBranchDict[bigBranchName[4]][0] += 1
                    self.bigBranchDict[bigBranchName[4]].append([bigBranchName[5], bigBranchName[3]])
                else:
                    self.bigBranchDict[bigBranchName[4]].append(bigBranchName[3])
            comboBox.addItems(list(self.bigBranchDict.keys()))

    def addSmallBranchName(self, BigcomboBox, SmallcomboBox):
        SmallcomboBox.clear()
        if self.bigBranchDict[BigcomboBox.currentText()][0]==0:
            SmallcomboBox.addItems(["无小分支"])
            SmallcomboBox.setEnabled(False)
        else:
            SmallcomboBox.addItems([nameList[0] for nameList in self.bigBranchDict[BigcomboBox.currentText()][1:]])
            SmallcomboBox.setEnabled(True)

    def find_haveBranch(self): #查找哪个类有多个分支
        temp_dict = {} #一个中间字典，作为中间变量
        for key, value in self.classname_fileUrl_dict.items():
            if value[0] in temp_dict:
                temp_dict[value[0]].append(key)
            else:
                temp_dict[value[0]] = [key]
        self.have_branch = []
        for key, value in temp_dict.items():
            if len(value) > 1:
                self.have_branch.append(value)

    #用于修改大分支位置的一个特定的函数
    def modifyBranchPositionFun(self):
        value = 0
        for key, value in self.classname_fileUrl_dict.items():
            if value[4] == self.modifyBranchNameComboBox.currentText():
                break

        branch_currentPosition = int(value[2].split("/")[-1][:4])
        if self.modifyBranchPositionComboBox.currentText() == '上移':
            if branch_currentPosition == 1:
                self.modifyBranchPositionSpinBox.setMinimum(0)
                self.modifyBranchPositionSpinBox.setValue(0)
                self.modifyBranchPositionButtom.setEnabled(False)
                self.modifyBranchPositionSpinBox.setEnabled(False)
                self.modifyBranchPositionButtom.setText("无法上移")
            else:
                self.modifyBranchPositionSpinBox.setMinimum(1)
                self.modifyBranchPositionButtom.setEnabled(True)
                self.modifyBranchPositionSpinBox.setEnabled(True)
                self.modifyBranchPositionSpinBox.setMaximum(branch_currentPosition - 1)
                self.modifyBranchPositionButtom.setText("修改大分支位置")
        else:
            if branch_currentPosition == self.totalBigBranchLength:
                self.modifyBranchPositionSpinBox.setMinimum(0)
                self.modifyBranchPositionSpinBox.setValue(0)
                self.modifyBranchPositionButtom.setEnabled(False)
                self.modifyBranchPositionSpinBox.setEnabled(False)
                self.modifyBranchPositionButtom.setText("无法下移")
            else:
                self.modifyBranchPositionSpinBox.setMinimum(1)
                self.modifyBranchPositionButtom.setEnabled(True)
                self.modifyBranchPositionSpinBox.setEnabled(True)
                self.modifyBranchPositionSpinBox.setMaximum(self.totalBigBranchLength-branch_currentPosition)
                self.modifyBranchPositionButtom.setText("修改大分支位置")


    def generate_Block(self):
        if self.addBlockLibName.text()=='' and self.addBlockClassName.text() != '':
            QMessageBox.about(self, '警告',"引用库名称那里没写，但是引用类名称却有？")
            return
        reply = QMessageBox.question(self, '确认一下', '确定要增加这个块吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if (self.addBlockCodeTextEdit.toPlainText()) and (self.addBlockContentTextEdit.toPlainText()):
                content = self.addBlockContentTextEdit.toPlainText().split('\n') #块的内容
                demo = self.addBlockCodeTextEdit.toPlainText().split('\n') #代码的内容
                while '' in content:
                    content.remove('')
                while '' in demo:
                    demo.remove('')
                op = Operate(content, demo,  (self.addBlockBranchComboBox1.currentText(), self.addBlockBranchComboBox2.currentText()), self.addBlockLibName.text(), self.addBlockClassName.text(),
                        self.ui.addBlockConnectCheckBox.isChecked(), self.classname_fileUrl_dict, self.bigBranchDict,
                             (self.addBlockColorCheckBox.isChecked(), ("0"*6+hex(self.addBlockColorSpinBox.value())[2:])[-6:]),(self.addBlockPositionCheckBox.isChecked(),
                      (self.addBlockPositionSpinBox.maximum()) if self.addBlockPositionCheckBox.isChecked() else self.addBlockPositionSpinBox.value(),
                                                                    "之后" if self.addBlockPositionCheckBox.isChecked() else self.addBlockPositionComboBox.currentText()))
                if op.checkSame != True:
                    QMessageBox.about(self, '格式不对', op.checkSame+'不对称，请检查一下代码和块的内容')
                    return
                try:
                    op.generate()
                    QMessageBox.about(self, '成功', '添加成功')
                    self.update()
                except:
                    QMessageBox.about(self, '失败', '添加失败，已自动为您撤回本次操作')
                    revoke_operate() # 添加失败的话，就自动撤回本次操作

            elif not self.addBlockCodeTextEdit.toPlainText():
                QMessageBox.about(self, '错误', '代码内容不能为空')
            elif not self.addBlockContentTextEdit.toPlainText():
                QMessageBox.about(self, '错误', '块的内容不能为空')

    def delete_Block(self):
        try:
            reply =  QMessageBox.question(self,'注意', '确定要删除吗?', QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                DL = Delete((self.deleteBlockBranchComboBox1.currentText(), self.deleteBlockBranchComboBox2.currentText()),
                            int(self.deleteBlockPositionSpinBox.text()), self.classname_fileUrl_dict)
                result = DL.delete()
                if result!=True:
                    QMessageBox.about(self, result[0], result[1])
                else:
                    QMessageBox.about(self, '成功', '删除块成功')
                    self.update()
        except:
            QMessageBox.about(self, '错误', '发生未知错误')
            revoke_operate()  # 添加失败的话，就自动撤回本次操作

    def generate_bigBranch(self):
        reply = QMessageBox.question(self, '确认一下', '确定要增加这个大分支吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.addBigBrachName.text()=='':
                QMessageBox.about(self, '警告', "新分支名字不能为空")
            elif not self.addBigBrachNameCheckBox.isChecked() and self.addBigBrachFileName.text()=='':
                QMessageBox.about(self, '警告', "你如果不想取名，那就点击随机取名")
            elif self.addBigBrachFileName.text() in [name[4:-5] for name in os.listdir(path+"/jsons")] and not self.addBigBrachNameCheckBox.isChecked():
                QMessageBox.about(self, '警告', "这个名字已经存在，请换一个")
            else:
                Ab = Add_bigBranch(self.addBigBrachName.text(), self.addBigBrachColorSpinBox.text(), (self.addBigBrachPotionCheckBox.isChecked(),
                                                                                   self.addBigBrachPotionSpinBox.maximum() if self.addBigBrachPotionCheckBox.isChecked() else self.addBigBrachPotionSpinBox.value(),
                                                                         self.addBigBrachPotionComboBox.currentText()),(self.addBigBrachNameCheckBox.isChecked(),self.addBigBrachFileName.text()))
                try:
                    Ab.new_File()
                    QMessageBox.about(self, '成功', "生成新的大分支成功")
                    self.update(reflashBranch=True)
                except:
                    QMessageBox.about(self, '失败', "生成新的大分支失败")
                    revoke_operate()  # 添加失败的话，就自动撤回本次操作

    def generate_smallBranch(self):
        reply = QMessageBox.question(self, '确认一下', '确定要增加这个小分支吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            As = Add_smallBranch(self.addSmallBrachColorSpinBox.text(),
                                 (self.addSmallBrachPotionComboBox.currentText(), self.addSmallBrachPotionSpinBox.text()), self.addSmallBrachName.text(), self.classname_fileUrl_dict)
            try:
                As.generate_branch(lambda title,content:QMessageBox.question(self, title, content, QMessageBox.Yes, QMessageBox.No))
                QMessageBox.about(self, '成功', "生成新的小分支成功")
                self.update()
            except:
                QMessageBox.about(self, '失败', "生成新的小分支失败")
                revoke_operate()  # 添加失败的话，就自动撤回本次操作

    def delete_bigBranch(self):
        reply = QMessageBox.question(self, '确认一下', '确定要删除这个大分支吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            value = 0
            for key, value in self.classname_fileUrl_dict.items():
                if value[4] == self.deleteBigBranchComboBox.currentText():
                    break
            db = DeleteBranch((True, None, int(value[2].split("/")[-1][:4])), None)
            try:
                db.Delete()
                QMessageBox.about(self, '成功', "删除大分支成功")
                self.update(reflashBranch=True)
            except:
                QMessageBox.about(self, '失败', "删除大分支失败")
                revoke_operate()  # 添加失败的话，就自动撤回本次操作

    def delete_smallBranch(self):
        reply = QMessageBox.question(self, '确认一下', '确定要删除这个小分支吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            db = DeleteBranch((False, self.deleteSmallBranchName.currentText(),self.deleteSmallBranchName2.currentText()), self.classname_fileUrl_dict)
            try:
                db.Delete()
                QMessageBox.about(self, '成功', "删除小分支成功")
                self.update()
            except:
                QMessageBox.about(self, '失败', "删除小分支失败")
                revoke_operate()  # 添加失败的话，就自动撤回本次操作

    def generate_label(self):
        reply = QMessageBox.question(self, '确认一下', '确定要增加这个标签吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            al = Add_label((self.addLabelBranchComboBox1.currentText(), self.addLabelComboBox2.currentText()),
                           (self.addLabelPositionCheckBox.isChecked(),self.addLabelPositionSpinBox.value(), self.addLabelPositionComboBox.currentText()),
                           self.addLabelContent.text(), self.classname_fileUrl_dict)
            try:
                al.generateLabel()
                QMessageBox.about(self, '成功', "增加新标签成功")
                self.update()
            except:
                QMessageBox.about(self, '失败', "增加新标签失败")
                revoke_operate()  # 添加失败的话，就自动撤回本次操作

    def delete_label(self):
        reply = QMessageBox.question(self, '确认一下', '确定要删除这个小分支吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            dl = DeleteLabel((self.deleteLabelBranchComboBox1.currentText(), self.deleteLabelBranchComboBox2.currentText()), self.deleteLabelPositionSpinBox.value(), self.classname_fileUrl_dict)
            try:
                dl.deleteLabel()
                QMessageBox.about(self, '成功', "删除标签成功")
                self.update()
            except:
                QMessageBox.about(self, '失败', "删除标签失败")
                revoke_operate()  # 失败的话，就自动撤回本次操作

    def import_branch(self):
        if self.importBranchFileUrl.text()=='':
            QMessageBox.about(self, '错误', "文件位置不能为空" )
            return
        elif os.path.exists(self.importBranchFileUrl.text())==False:
            QMessageBox.about(self, '错误', "文件位置不存在")
            return
        reply = QMessageBox.question(self, '确认一下', '确定要导入这个分支吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            ib = importBranch(fileUrl = self.importBranchFileUrl.text(),
                                      positionTur = (self.importBranchPosition.value(),self.importBranchCheckBox.isChecked(),
                                                     self.importBranchPositionComboBox.currentText())
                              )
            try:
                formatCheck = ib.formatDetect()
                if formatCheck[0] != 0:
                    QMessageBox.about(self, '错误', formatCheck[1])
                else:
                    ib.Import()
                    QMessageBox.about(self, '成功', "导入分支成功")
                    self.update(reflashBranch=True)
            except:
                QMessageBox.about(self, '失败', "导入分支失败")
                revoke_operate()  # 失败的话，就自动撤回本次操作

    def export_branch(self):
        FolderPath = None
        if self.exportBranchFileUrl.text()=='':
            QMessageBox.about(self, '错误', "文件位置不能为空" )
            return
        if os.path.exists(self.exportBranchFileUrl.text())==False:
            QMessageBox.about(self, '错误', "文件位置不存在")
            return
        reply = QMessageBox.question(self, '确认一下', '确定要导出该分支吗?', QMessageBox.Yes, QMessageBox.No)
        if reply==QMessageBox.Yes:
            try:
                value=0
                for key,value in self.classname_fileUrl_dict.items():
                    if value[4]==self.exportBranchComboBox.currentText():
                        break
                eb = EmportBranch(self.exportBranchFileUrl.text(),
                                 int(value[2].split("/")[-1][:4]))
                FolderPath = eb.Emport()
                QMessageBox.about(self, '成功', "导出分支成功,分支位置为："+FolderPath)
            except:
                QMessageBox.about(self, '失败', "导出分支失败")
                if FolderPath != None:
                    if os.path.exists(FolderPath):
                        try:
                            eb.delete(FolderPath)
                        except:
                            QMessageBox.about(self, '奇怪', "发送了奇怪错误")
                            revoke_operate()  # 失败的话，就自动撤回本次操作

    def modify_block(self):
        reply = QMessageBox.question(self, '确认一下', '确定要修改这个块吗?', QMessageBox.Yes, QMessageBox.No)
        if reply==QMessageBox.Yes:
            try:
                mb = ModifyBlock((self.modifyBlockBranchComboBox1.currentText(),self.modifyBlockBranchComboBox2.currentText()),
                                 self.modifyBlockPositionSpinBox.value(),
                                 (self.modifyBlockLibName.text(),self.modifyBlockLibCheckBox.isChecked()),
                                 (self.modifyBlockClassName.text(),self.modifyBlockClassCheckBox.isChecked()),
                                 (self.modifyBlockColorSpinBox.text(),self.modifyBlockColorCheckBox.isChecked()),
                                 self.modifyBlockConnectCheckBox,
                                 (self.modifyBlockCodeTextEdit.toPlainText().split('\n'),self.modifyBlockCodeCheckBox.isChecked()),
                                 (self.modifyBlockContentTextEdit.toPlainText().split('\n'),self.modifyBlockContentCheckBox.isChecked()),
                                 self.classname_fileUrl_dict)
                mb.getInfo(lambda title,content:QMessageBox.about(self, title, content))
                QMessageBox.about(self, '成功', "修改块成功")
                self.update()
            except:
                QMessageBox.about(self, '失败', "修改块失败")
                revoke_operate()  # 失败的话，就自动撤回本次操作

    def reflashBigBranchName(self,*comboBoxs):
        for combo in comboBoxs:
            try:
                combo.currentTextChanged.disconnect()
            except:
                pass
            combo.clear()
            self.addBigBranchName(combo)
        self.init()
        self.bind(onlyComBoBox=True)

    def modify_BigBranch_Position(self):
        reply = QMessageBox.question(self, '确认一下', '确定要修改这个大分支的位置吗?', QMessageBox.Yes, QMessageBox.No)
        if reply==QMessageBox.Yes:
            try:
                mbp = ModifyBigBranchPosition(self.modifyBranchNameComboBox.currentText(),
                                                              self.modifyBranchPositionComboBox.currentText(),
                                                              self.modifyBranchPositionSpinBox.value(),
                                                            self.classname_fileUrl_dict
                                              )

                QMessageBox.about(self, '成功', "修改大分支位置成功")
                self.update(reflashBranch=True)
            except:
                QMessageBox.about(self, '失败', "修改大分支位置失败")
                revoke_operate()  # 失败的话，就自动撤回本次操作
                self.update(reflashBranch=True)

    def revoke(self):#撤销本次块的操作，删除或者生成块
        reply = QMessageBox.question(self, '确认一下', '确定要撤回吗?该操作不可逆！！', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if(revoke_operate()==False):
                QMessageBox.about(self, '错误', '最近无块的操作(删除或生成)，无法进行撤回操作')
            else:
                QMessageBox.about(self, '成功', '撤销成功')
                self.update()


if __name__ == '__main__':
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()