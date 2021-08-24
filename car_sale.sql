/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : car_sale

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 09/03/2020 17:26:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for car
-- ----------------------------
DROP TABLE IF EXISTS `car`;
CREATE TABLE `car`  (
  `car_no` char(5) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `car_type` char(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `car_color` char(8) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `car_maner` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `car_date` date NOT NULL,
  `car_price` decimal(9, 2) NOT NULL,
  PRIMARY KEY (`car_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of car
-- ----------------------------
INSERT INTO `car` VALUES ('00010', '新朗逸', '白色', '上汽大众', '2018-02-12', 100000.00);
INSERT INTO `car` VALUES ('00011', '新朗逸', '黑色', '上汽大众', '2018-02-12', 99800.00);
INSERT INTO `car` VALUES ('00012', '新朗逸', '蓝色', '上汽大众', '2018-02-12', 129800.00);
INSERT INTO `car` VALUES ('00013', '新朗逸', '金色', '上汽大众', '2018-02-12', 161900.00);
INSERT INTO `car` VALUES ('00014', '新朗逸', '红色', '上汽大众', '2018-02-12', 143000.00);
INSERT INTO `car` VALUES ('00020', '轩逸', '白色', '东风日产', '2018-07-06', 99800.00);
INSERT INTO `car` VALUES ('00021', '轩逸', '橙色', '东风日产', '2018-07-06', 118600.00);
INSERT INTO `car` VALUES ('00022', '轩逸', '黑色', '东风日产', '2018-07-06', 101800.00);
INSERT INTO `car` VALUES ('00023', '轩逸', '蓝色', '东风日产', '2018-07-06', 139800.00);
INSERT INTO `car` VALUES ('00024', '轩逸', '红色', '东风日产', '2018-07-06', 139800.00);
INSERT INTO `car` VALUES ('00025', '轩逸', '金色', '东风日产', '2018-07-06', 14300.00);
INSERT INTO `car` VALUES ('00030', '卡罗拉', '红色', '一汽丰田', '2018-07-08', 130800.00);
INSERT INTO `car` VALUES ('00031', '卡罗拉', '白色', '一汽丰田', '2018-07-08', 119800.00);
INSERT INTO `car` VALUES ('00032', '卡罗拉', '黑色', '一汽丰田', '2018-07-08', 129800.00);
INSERT INTO `car` VALUES ('00033', '卡罗拉', '银色', '一汽丰田', '2018-07-08', 159800.00);
INSERT INTO `car` VALUES ('00040', '速腾', '白色', '一汽大众', '2018-06-09', 128900.00);
INSERT INTO `car` VALUES ('00041', '速腾', '黑色', '一汽大众', '2018-06-09', 130000.00);
INSERT INTO `car` VALUES ('00042', '速腾', '银色', '一汽大众', '2018-06-09', 138900.00);
INSERT INTO `car` VALUES ('00043', '速腾', '橙色', '一汽大众', '2018-06-09', 145900.00);
INSERT INTO `car` VALUES ('00050', '新宝来', '白色', '一汽大众', '2018-03-15', 98800.00);
INSERT INTO `car` VALUES ('00051', '新宝来', '黑色', '一汽大众', '2018-03-15', 108800.00);
INSERT INTO `car` VALUES ('00052', '新宝来', '棕色', '一汽大众', '2018-03-15', 113000.00);
INSERT INTO `car` VALUES ('00053', '新宝来', '橙色', '一汽大众', '2018-03-15', 120000.00);
INSERT INTO `car` VALUES ('00054', '新宝来', '金色', '一汽大众', '2018-03-15', 156000.00);
INSERT INTO `car` VALUES ('00060', '帕萨特', '黑色', '一汽大众 ', '2018-02-19', 184900.00);
INSERT INTO `car` VALUES ('00061', '帕萨特', '白色', '一汽大众 ', '2018-02-19', 184900.00);
INSERT INTO `car` VALUES ('00062', '帕萨特', '蓝色', '一汽大众 ', '2018-02-19', 206900.00);
INSERT INTO `car` VALUES ('00063', '帕萨特', '金色', '一汽大众 ', '2018-02-19', 237900.00);
INSERT INTO `car` VALUES ('00070', '英朗', '白色', '上汽通用', '2018-04-05', 115900.00);
INSERT INTO `car` VALUES ('00071', '英朗', '黑色', '上汽通用', '2018-04-05', 118900.00);
INSERT INTO `car` VALUES ('00072', '英朗', '金色', '上汽通用', '2018-04-05', 143900.00);
INSERT INTO `car` VALUES ('00080', '桑塔纳', '黑色', '上汽大众 ', '2018-07-31', 56500.00);
INSERT INTO `car` VALUES ('00090', '北汽EU', '白色', '北汽新能源 ', '2018-05-27', 129800.00);
INSERT INTO `car` VALUES ('00100', '雅阁', '黑色', '广汽本田 ', '2018-09-15', 144800.00);
INSERT INTO `car` VALUES ('00101', '雅阁', '白色', '广汽本田 ', '2018-09-15', 144800.00);
INSERT INTO `car` VALUES ('00102', '雅阁', '银色', '广汽本田 ', '2018-09-15', 179800.00);
INSERT INTO `car` VALUES ('00103', '雅阁', '蓝色', '广汽本田 ', '2018-09-15', 154800.00);
INSERT INTO `car` VALUES ('00104', '雅阁', '橙色', '广汽本田 ', '2018-09-15', 189800.00);
INSERT INTO `car` VALUES ('00105', '雅阁', '红色', '广汽本田 ', '2018-09-15', 209800.00);
INSERT INTO `car` VALUES ('00112', 'car', 'blue', 'uknow', '2020-03-04', 999999.00);
INSERT INTO `car` VALUES ('00113', 'car', 'pink', 'unknow', '2000-03-03', 3333333.00);
INSERT INTO `car` VALUES ('00114', 'car', 'pink', 'unknow', '2000-03-03', 3333333.00);

-- ----------------------------
-- Table structure for custom
-- ----------------------------
DROP TABLE IF EXISTS `custom`;
CREATE TABLE `custom`  (
  `cname` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cage` int(0) NULL DEFAULT NULL,
  `csex` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ctel` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Brecord` tinyint(0) NULL DEFAULT NULL,
  PRIMARY KEY (`cname`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of custom
-- ----------------------------
INSERT INTO `custom` VALUES ('wky', 20, '男', '123456', 0);
INSERT INTO `custom` VALUES ('丰星', 53, '男', '13605404466', 0);
INSERT INTO `custom` VALUES ('侯贞', 42, '女', '13202738457', 0);
INSERT INTO `custom` VALUES ('况诚伦', 46, '男', '15704541508', 1);
INSERT INTO `custom` VALUES ('包安', 45, '男', '13207385160', 0);
INSERT INTO `custom` VALUES ('单彪顺', 49, '男', '15704081212', 1);
INSERT INTO `custom` VALUES ('厍绍', 41, '男', '13000506666', 0);
INSERT INTO `custom` VALUES ('奚泰旭', 37, '男', '15303655609', 1);
INSERT INTO `custom` VALUES ('姜俊', 31, '男', '13804594050', 0);
INSERT INTO `custom` VALUES ('宗俊启', 56, '男', '13504217626', 1);
INSERT INTO `custom` VALUES ('寿羽', 35, '女', '13305126415', 0);
INSERT INTO `custom` VALUES ('帅眉凝', 36, '女', '13504882278', 0);
INSERT INTO `custom` VALUES ('平琰彩', 42, '女', '15905081963', 1);
INSERT INTO `custom` VALUES ('桑承良', 28, '男', '13700051161', 0);
INSERT INTO `custom` VALUES ('沃裕峰', 52, '男', '13702257875', 1);
INSERT INTO `custom` VALUES ('涂昭珊', 29, '女', '13705051777', 1);
INSERT INTO `custom` VALUES ('琴浩', 34, '男', '15203660790', 0);
INSERT INTO `custom` VALUES ('相聪春', 52, '女', '15705312114', 1);
INSERT INTO `custom` VALUES ('福娟', 38, '女', '13900278568', 0);
INSERT INTO `custom` VALUES ('郗东有', 41, '男', '13205815165', 0);
INSERT INTO `custom` VALUES ('雷建时', 50, '男', '13308510434', 1);

-- ----------------------------
-- Table structure for employ
-- ----------------------------
DROP TABLE IF EXISTS `employ`;
CREATE TABLE `employ`  (
  `eno` char(5) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ename` char(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `eage` int(0) NULL DEFAULT NULL,
  `esex` char(2) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ehome` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `edu` char(8) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`eno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employ
-- ----------------------------
INSERT INTO `employ` VALUES ('001', '隗梅娟', 31, '女', '贵州', '本科');
INSERT INTO `employ` VALUES ('002', '许达平', 21, '男', '辽宁', '本科');
INSERT INTO `employ` VALUES ('003', '诸利克', 27, '男', '浙江', '本科');
INSERT INTO `employ` VALUES ('004', '弓影', 21, '女', '云南', '本科');
INSERT INTO `employ` VALUES ('005', '贝谦', 23, '男', '上海', '本科');
INSERT INTO `employ` VALUES ('006', '赏秋洁', 25, '女', '河北', '本科');
INSERT INTO `employ` VALUES ('007', '闻佳雁', 24, '女', '广东', '本科');
INSERT INTO `employ` VALUES ('008', '奚咏丹', 30, '女', '上海', '本科');
INSERT INTO `employ` VALUES ('009', '汪蓓彩', 35, '女', '山西', '本科');
INSERT INTO `employ` VALUES ('010', '梁纨', 24, '女', '广东', '本科');

-- ----------------------------
-- Table structure for sale
-- ----------------------------
DROP TABLE IF EXISTS `sale`;
CREATE TABLE `sale`  (
  `sale_car` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sale_type` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sale_color` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sale_date` datetime(0) NOT NULL,
  `sale_num` int(0) NOT NULL,
  `sale_man` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`sale_car`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sale
-- ----------------------------
INSERT INTO `sale` VALUES ('00010', '新朗逸', '白色', '2019-05-15 10:35:35', 1, '闻佳雁');
INSERT INTO `sale` VALUES ('00011', '新朗逸', '黑色', '2019-06-25 08:12:06', 1, '贝谦');
INSERT INTO `sale` VALUES ('00023', '轩逸', '蓝色', '2019-03-08 12:36:21', 1, '许达平');
INSERT INTO `sale` VALUES ('00032', '卡罗拉', '黑色', '2019-04-26 09:07:05', 1, '隗梅娟');
INSERT INTO `sale` VALUES ('00041', '速腾', '黑色', '2019-04-28 15:35:39', 1, '隗梅娟');
INSERT INTO `sale` VALUES ('00052', '新宝来', '棕色', '2019-02-23 13:34:38', 1, '奚咏丹');
INSERT INTO `sale` VALUES ('00062', '帕萨特', '蓝色', '2019-05-02 13:19:26', 1, '弓影');
INSERT INTO `sale` VALUES ('00071', '英朗', '黑色', '2019-09-02 11:05:48', 1, '弓影');
INSERT INTO `sale` VALUES ('00080', '桑塔纳', '黑色', '2019-04-15 14:52:12', 1, '梁纨');
INSERT INTO `sale` VALUES ('00090', '北汽EU', '白色', '2019-07-26 11:15:14', 1, '诸利克');
INSERT INTO `sale` VALUES ('00104', '雅阁', '橙色', '2019-06-09 17:08:47', 1, '汪蓓彩');
INSERT INTO `sale` VALUES ('00112', 'car', 'blue', '2019-03-04 19:21:00', 1, '');
INSERT INTO `sale` VALUES ('00113', 'car', 'blue', '2019-03-04 19:21:00', 1, NULL);

SET FOREIGN_KEY_CHECKS = 1;
