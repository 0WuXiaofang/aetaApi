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

 Date: 12/04/2022 23:17:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for eta_user
-- ----------------------------
DROP TABLE IF EXISTS `eta_user`;
CREATE TABLE `eta_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `islogin` int NOT NULL,
  `isdeny` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of eta_user
-- ----------------------------
INSERT INTO `eta_user` VALUES (1, 'aFang', '1234', 0, 0);
INSERT INTO `eta_user` VALUES (2, 'laoji', '12345', 1, 0);
INSERT INTO `eta_user` VALUES (3, 'xinyu', '12345', 1, 0);
INSERT INTO `eta_user` VALUES (8, 'xiaohonghua', '12345', 1, 0);

SET FOREIGN_KEY_CHECKS = 1;
