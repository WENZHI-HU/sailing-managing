before start the code, u should download git in your computer, and then use the following command to clone the code to your computer:

git clone https://github.com/WENZHI-HU/sailing-managing.git 
  
it will create a folder named "sailing-managing" in your computer, and then you can use the following command to update the code:

git checkout master


before you update the code, you should use the following command to check if there is any update and swithch to the master branch(where i set code as the latest version):

then, create ur own branch to update the code, it can ensure all changes by u can be recorded,


DON'T USE THE MASTER BRANCH TO UPDATE THE CODE!!!


git checkout -b your_branch_name



these command create a new branch and switch to it, then u can use the following command to update the code:

don't be silly, no body use terminal to update the code :) 
listen what i said in lecture.

to whom forget what i said, use the following command to update the code:
git add .
git commit -m "type sth"
git push origin your_branch_name
then, go to the github website, and create a pull request, and then i will check the code and merge it to the master branch.









before run the code, you need to install the following packages:

pip install PyQt5

small example for PyQt5:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle('my PyQt5')
main_window.setGeometry(100, 100, 800, 600)
main_window.show()
sys.exit(app.exec_())


pip install qtawesome
pip install pandas
pip install pymysql
pip install hashlib (i think that is all, if not, please remind me to check what i missed)

for sql part

firstly, download mysql from oracle, that is free with the students email account

then, sql tools such as navicat, datadrip or mysql workbench as u like, but not compulsive, cmd is fine.

after setting the mysql username and password, try if u can linked to your database. enter " mysql -u username(ur username) -p
enter password
show databases; " to check if u can see the database u created.
in this program, create database student_management(or whatever u like, but u need to change the code in the program)

remember to change the information in the config.py file, such as username, password, database name, host, port, charset, etc.

then, run the sql file in the database, which is 

"SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `a_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1.超级管理员 其他.班级管理员',
  `a_username` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `a_password` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '密码 长度6-18 (MD5加密)',
  `a_mark` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '备注',
  `a_classid` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '可管理班级（id）多个班级id可用,隔开',
  PRIMARY KEY (`a_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '管理员表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'admin', 'e10adc3949ba59abbe56e057f20f883e', 'admin', '0');
INSERT INTO `admin` VALUES (2, 'ten hag', 'e10adc3949ba59abbe56e057f20f883e', 'ten hag', '1');
INSERT INTO `admin` VALUES (3, 'pep', 'e10adc3949ba59abbe56e057f20f883e', 'pep', '2');
INSERT INTO `admin` VALUES (4, 'james', 'e10adc3949ba59abbe56e057f20f883e', 'james', '1,2');

-- ----------------------------
-- Table structure for class_
-- ----------------------------
DROP TABLE IF EXISTS `class_`;
CREATE TABLE `class_`  (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '班级名称',
  PRIMARY KEY (`c_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '班级表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class_
-- ----------------------------
INSERT INTO `class_` VALUES (1, 'manchester united');
INSERT INTO `class_` VALUES (2, 'manchester city');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_realname` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT 'NAME',
  `s_number` int(11) NULL DEFAULT NULL COMMENT 'ID',
  `s_sex` int(11) NOT NULL DEFAULT 0 COMMENT 'GENDER	1.男，2.女',
  `s_class` int(11) NOT NULL DEFAULT 0 COMMENT 'TEAM id',
  `s_chinese` int(11) NOT NULL DEFAULT 0 COMMENT '语文成绩',
  `s_math` int(11) NOT NULL DEFAULT 0 COMMENT '数学成绩',
  `s_english` int(11) NOT NULL DEFAULT 0 COMMENT '外语成绩',
  PRIMARY KEY (`s_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 529 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '学生信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (4, 'kobe', 1004, 1, 2, 0, 0, 0);
INSERT INTO `student` VALUES (3, 'd.b', 1003, 2, 1, 0, 0, 0);
INSERT INTO `student` VALUES (2, 'CR7', 1002, 1, 2, 0, 0, 0);
INSERT INTO `student` VALUES (1, 'E.H', 1001, 1, 1, 99, 99, 60);

SET FOREIGN_KEY_CHECKS = 1;









!!!all Chinese can be replaced as u like, just remind to change the code in the program.(i use because the database gonna be easier for me to read)



