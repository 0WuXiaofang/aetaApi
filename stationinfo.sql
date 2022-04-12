/*
 Navicat MySQL Data Transfer

 Source Server         : aeta
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : gasound

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 12/04/2022 23:17:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stationinfo
-- ----------------------------
DROP TABLE IF EXISTS `stationinfo`;
CREATE TABLE `stationinfo`  (
  `Title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `StationID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Longitude` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Latitude` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `MagnData` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `MagnUpdate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `SoundData` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `SoundUpdate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`StationID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stationinfo
-- ----------------------------
INSERT INTO `stationinfo` VALUES ('木里县防震减灾局', '101', '101.27', '27.93', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('峨眉山防震减灾局', '105', '103.5', '29.59', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('石屏', '106', '102.52', '23.73', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('小金县防震减灾局', '107', '102.36', '31.0', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马兰山地震台', '109', '101.73', '26.6', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('德宏州防震减灾局', '113', '98.59', '24.44', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('广元市朝天区东溪河台', '115', '105.75', '32.63', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('平武县防震减灾局', '116', '104.55', '32.41', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('巴塘县防灾减灾局', '119', '99.11', '30.0', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('永善县大瀑沟地震观测站', '120', '103.64', '28.23', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('九寨沟防震减灾局', '121', '104.25', '33.26', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('炉霍县防灾减灾局', '122', '100.67', '31.39', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('名山区安吉村', '124', '103.15', '30.19', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('金川防震减灾局', '125', '102.07', '31.47', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('德格县防灾减灾局', '127', '98.57', '31.71', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('道孚县防灾减灾局', '128', '101.12', '30.98', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('松潘地震台', '129', '103.6', '32.65', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('九龙县乃渠乡政府', '130', '101.68', '28.76', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('得荣县防灾减灾局', '131', '99.29', '28.72', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('西昌小庙山洞', '132', '102.23', '27.91', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('甘孜县防震减灾局', '133', '99.99', '31.62', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('大理蝴蝶泉', '137', '100.09', '25.9', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('大理双廊镇中学', '138', '100.19', '25.92', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('云龙地震台', '140', '99.37', '25.89', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('青川县姚渡观测站', '141', '105.42', '32.78', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('元谋地震台', '142', '101.86', '25.69', 'True', 'False', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('个旧地震台', '146', '103.16', '23.38', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('昭通地震台', '147', '103.72', '27.32', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('沐川防震减灾局', '148', '103.9', '28.96', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('冕宁回龙乡', '149', '102.18', '28.62', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('青川房石镇', '150', '104.96', '32.37', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('鲁甸地震台', '151', '103.55', '27.24', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('金牛镇第二小学', '152', '100.59', '25.83', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('冕宁复兴镇', '153', '102.17', '28.42', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('玉溪黄草坝', '155', '102.62', '24.47', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('云南昆明台', '156', '102.74', '25.14', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('崇州市三郎地震台', '159', '103.54', '30.79', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('保山地震台', '161', '99.12', '25.11', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('丽江永胜县地震局', '164', '100.75', '26.68', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('丽江玉龙县南溪台', '165', '100.16', '26.77', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('平武县虎牙乡', '166', '104.03', '32.33', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('松潘岷江乡', '167', '103.72', '32.4', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('平武白马藏族乡', '169', '104.19', '32.84', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('金川安宁镇镇政府', '170', '102.06', '31.29', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('鸡足山初级中学', '171', '100.47', '25.88', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('文县地震局', '172', '104.69', '32.93', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('丽江古城', '174', '100.23', '26.87', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('丽江流动1号', '175', '100.236072', '26.830704', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('荥经县严道一中', '177', '102.84', '29.8', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('四川冕宁漫水湾', '181', '102.167771', '28.208206', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('红原县', '182', '102.55', '32.8', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('青川茶坝乡', '183', '105.35', '32.44', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('黑水', '184', '102.99', '32.06', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('腾冲地震台', '186', '98.52', '25.03', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('茂县叠溪镇政府', '188', '103.68', '32.04', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('九寨沟黄龙机场', '189', '103.69', '32.85', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('都江堰中学', '19', '103.65', '30.98', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('九寨沟甘海子', '191', '103.77', '33.25', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('冕宁大桥镇', '193', '102.19', '28.65', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('九寨沟漳扎', '197', '103.88', '33.29', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('平武南埧镇', '198', '104.83', '32.2', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('冕宁里庄乡', '200', '101.86', '28.22', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('理县米亚镇镇政府', '201', '102.8', '31.66', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('九寨沟永和', '202', '104.2', '33.15', 'True', 'True', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('彭州银厂沟地震台', '204', '103.81', '31.26', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('丽江大东林工站', '206', '100.39', '27.15', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('文县中寨', '212', '104.42', '33.18', 'True', 'False', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('剑门关地震台', '214', '105.57', '32.2', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('腾冲马站', '220', '98.49', '25.21', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('芦山县中坝村', '221', '103.06', '30.34', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('天全县防震减灾局', '223', '102.76', '30.04', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('丽江华坪县地震局办公楼', '225', '101.26', '26.63', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('腾冲热海', '226', '98.43', '24.95', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('青川桥楼', '228', '104.929167', '32.48777800000001', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('洪雅县防震减灾局', '229', '103.37', '29.91', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('丽江宁蒗地震局', '231', '100.84', '27.29', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('大录乡', '235', '103.67', '33.56', 'True', 'True', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('阿坝县', '236', '101.7', '32.91', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('碧口', '238', '105.29', '32.73', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('通海山洞', '24', '102.75', '24.12', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('青神县防震减灾局', '240', '103.85', '29.84', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('盐源泸沽湖', '243', '100.86', '27.72', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('壤塘县', '246', '100.98', '32.26', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('汉源县联络村', '247', '102.53', '29.53', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('汶川映秀', '250', '103.48', '31.05', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('川陕交界黄坝驿台', '251', '106.14', '32.76', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('若尔盖', '252', '102.96', '33.58', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('永善县桧溪地震综合观测站', '254', '103.85', '28.3', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('峨眉山市高桥镇政府', '255', '103.43', '29.52', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('峨眉山市黄湾镇政府', '256', '103.43', '29.58', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('康定姑咱山洞B', '26', '102.17', '30.12', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('楚雄山洞', '29', '101.54', '25.03', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边永红', '302', '103.4', '28.55', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('乡城地震台', '303', '99.79', '28.94', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边荍坝', '304', '103.73', '28.83', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边民主', '305', '103.64', '28.71', 'True', 'True', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('大理海东中学', '306', '100.26', '25.72', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边彝族自治县烟峰镇政府畜牧站', '307', '103.46', '28.71', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('德钦台', '308', '98.92', '28.47', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('冕宁泸沽镇小学', '309', '102.189548', '28.299008', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('雅安芦山大川', '310', '103.101139', '30.487948', 'False', 'False', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('稻城城关小学', '313', '100.3', '29.04', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边县三口河乡政府', '314', '103.35', '28.88', 'True', 'True', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('马边梅子坝', '315', '103.32', '28.8', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('马边大竹堡', '316', '103.47', '28.99', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边荣丁', '317', '103.59', '28.99', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('香格里拉台', '318', '99.7', '27.82', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边建设', '319', '103.59', '28.78', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('西昌气象局', '32', '102.27', '27.9', 'True', 'False', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边袁家溪', '320', '103.52', '28.7', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('宜宾屏山富荣', '321', '104.15', '28.71', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('五通桥防震减灾局', '322', '103.81', '29.4', 'True', 'True', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('内江威远严陵镇', '324', '104.71', '29.54', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('宜宾永兴', '326', '104.56', '29.03', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('绿春县地震观测台', '327', '102.41', '23.0', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('井研住建局', '328', '104.06', '29.65', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('乐山沙湾应急管理局', '329', '103.55', '29.42', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('石棉挖角乡', '33', '102.28', '29.31', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('荣县长山', '331', '104.23', '29.45', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('红河县地震观测台', '332', '102.38', '23.37', 'True', 'True', 'False', 'False');
INSERT INTO `stationinfo` VALUES ('乐山市防震减灾局', '333', '103.75', '29.58', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('乐山夹江人民政府', '334', '103.57', '29.74', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('自贡大安', '335', '104.78', '29.38', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('宜宾天池公园', '339', '104.56', '28.71', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('石棉山洞B', '35', '102.35', '29.23', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('宜宾长宁气象局', '352', '104.92', '28.58', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('宜宾兴文三合村', '355', '105.18', '28.24', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('永胜期纳镇', '36', '100.62', '26.33', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('冕宁防震减灾局', '38', '102.17', '28.55', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('巧家地震台', '39', '102.94', '26.9', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('凉山喜德冕山', '40047', '102.32', '28.35', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('德昌防震减灾局', '41', '102.17', '27.4', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('青川县防震减灾局', '43', '105.23', '32.59', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('筠连县地震台', '47', '104.51', '28.15', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('珙县气象局', '48', '104.79', '28.38', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('云南元阳地震局', '50117', '102.84', '23.23', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('洱源山洞B', '51', '99.95', '26.1', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('丽江山洞C', '55', '100.17', '26.97', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('白玉县河坡乡政府', '59', '98.96', '31.38', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('迪庆维西', '60139', '99.35159', '27.12313', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('大理古城月溪井', '60157', '100.18', '25.7', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('冕宁灵山', '60195', '102.214539', '28.563093', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('绵阳北川', '60241', '104.44', '31.79', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('石棉县安顺彝族乡政府', '60251', '102.27', '29.16', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马边地震局', '73', '103.54', '28.83', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('犍为县防震减灾局', '75', '103.94', '29.21', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('高县气象局', '77', '104.51', '28.44', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('盐源县盐塘乡', '78', '101.17', '27.35', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('理塘县防震减灾局', '82', '100.27', '29.99', 'True', 'False', 'True', 'False');
INSERT INTO `stationinfo` VALUES ('雷波县地震台(山洞)', '84', '103.58', '28.27', 'True', 'False', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('金口河防震减灾局', '87', '103.08', '29.22', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('理县上孟乡政府', '88', '103.14', '31.68', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('茂县测点', '90', '103.85', '31.69', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('汶川防震减灾局', '91', '103.59', '31.48', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('宝兴县灵关中学', '93', '102.82', '30.25', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('甘孜雅江', '94', '101.01', '30.03', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('峨边中学', '96', '103.25', '29.23', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('马尔康市防震减灾局', '98', '102.22', '31.9', 'True', 'True', 'True', 'True');
INSERT INTO `stationinfo` VALUES ('什邡市防震减灾局', '99', '104.16', '31.13', 'True', 'True', 'True', 'True');

SET FOREIGN_KEY_CHECKS = 1;
