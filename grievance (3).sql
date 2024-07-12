-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 31, 2023 at 07:48 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grievance`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add manage_collage', 7, 'add_manage_collage'),
(26, 'Can change manage_collage', 7, 'change_manage_collage'),
(27, 'Can delete manage_collage', 7, 'delete_manage_collage'),
(28, 'Can view manage_collage', 7, 'view_manage_collage'),
(29, 'Can add manage_complain data', 8, 'add_manage_complaindata'),
(30, 'Can change manage_complain data', 8, 'change_manage_complaindata'),
(31, 'Can delete manage_complain data', 8, 'delete_manage_complaindata'),
(32, 'Can view manage_complain data', 8, 'view_manage_complaindata'),
(33, 'Can add manage_department', 9, 'add_manage_department'),
(34, 'Can change manage_department', 9, 'change_manage_department'),
(35, 'Can delete manage_department', 9, 'delete_manage_department'),
(36, 'Can view manage_department', 9, 'view_manage_department'),
(37, 'Can add manage_designation', 10, 'add_manage_designation'),
(38, 'Can change manage_designation', 10, 'change_manage_designation'),
(39, 'Can delete manage_designation', 10, 'delete_manage_designation'),
(40, 'Can view manage_designation', 10, 'view_manage_designation'),
(41, 'Can add manage_grievance type', 11, 'add_manage_grievancetype'),
(42, 'Can change manage_grievance type', 11, 'change_manage_grievancetype'),
(43, 'Can delete manage_grievance type', 11, 'delete_manage_grievancetype'),
(44, 'Can view manage_grievance type', 11, 'view_manage_grievancetype'),
(45, 'Can add manage_registration', 12, 'add_manage_registration'),
(46, 'Can change manage_registration', 12, 'change_manage_registration'),
(47, 'Can delete manage_registration', 12, 'delete_manage_registration'),
(48, 'Can view manage_registration', 12, 'view_manage_registration'),
(49, 'Can add manage_user', 13, 'add_manage_user'),
(50, 'Can change manage_user', 13, 'change_manage_user'),
(51, 'Can delete manage_user', 13, 'delete_manage_user'),
(52, 'Can view manage_user', 13, 'view_manage_user');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'main', 'manage_collage'),
(8, 'main', 'manage_complaindata'),
(9, 'main', 'manage_department'),
(10, 'main', 'manage_designation'),
(11, 'main', 'manage_grievancetype'),
(12, 'main', 'manage_registration'),
(13, 'main', 'manage_user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-05-02 16:39:44.559389'),
(2, 'auth', '0001_initial', '2023-05-02 16:39:44.900127'),
(3, 'admin', '0001_initial', '2023-05-02 16:39:44.996274'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-05-02 16:39:45.005043'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-05-02 16:39:45.012575'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-05-02 16:39:45.060594'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-05-02 16:39:45.100863'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-05-02 16:39:45.132864'),
(9, 'auth', '0004_alter_user_username_opts', '2023-05-02 16:39:45.140939'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-05-02 16:39:45.180861'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-05-02 16:39:45.180861'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-05-02 16:39:45.188863'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-05-02 16:39:45.204863'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-05-02 16:39:45.228983'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-05-02 16:39:45.244862'),
(16, 'auth', '0011_update_proxy_permissions', '2023-05-02 16:39:45.252902'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-05-02 16:39:45.268936'),
(18, 'main', '0001_initial', '2023-05-02 16:39:45.647669'),
(19, 'main', '0002_rename_enrollment_registration_uniqueid_and_more', '2023-05-02 16:39:45.688329'),
(20, 'main', '0003_alter_complaindata_complaincode', '2023-05-02 16:39:45.688329'),
(21, 'main', '0004_alter_user_collage_alter_user_address_and_more', '2023-05-02 16:39:46.027604'),
(22, 'main', '0005_alter_user_collage_alter_user_address_and_more', '2023-05-02 16:39:46.359068'),
(23, 'main', '0006_complaindata_feedback', '2023-05-02 16:39:46.382834'),
(24, 'main', '0007_alter_complaindata_feedback', '2023-05-02 16:39:46.414842'),
(25, 'main', '0008_rename_designation_user_designation', '2023-05-02 16:39:46.510842'),
(26, 'main', '0009_rename_designation_user_designation', '2023-05-02 16:39:46.615339'),
(27, 'main', '0010_complaindata_to', '2023-05-02 16:39:46.663792'),
(28, 'main', '0011_alter_complaindata_solvingdate', '2023-05-02 16:39:46.671795'),
(29, 'main', '0012_collage_collagecity', '2023-05-02 16:39:46.687801'),
(30, 'main', '0013_alter_complaindata_to', '2023-05-02 16:39:46.775882'),
(31, 'main', '0014_rename_collage_manage_collage_and_more', '2023-05-02 16:39:47.553210'),
(32, 'sessions', '0001_initial', '2023-05-02 16:39:47.587165'),
(33, 'main', '0015_remove_manage_collage_collagecity', '2023-05-02 16:41:54.260790'),
(34, 'main', '0016_alter_manage_designation_designationname_and_more', '2023-05-03 00:57:26.735620');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5euvccstdihgu3101l0dvq9y5acdkjww', 'e30:1pu1uC:H-xdIsrI4Zn1lS-eJkOdsDJLhejcKYwFYab2QqWjclM', '2023-05-17 02:07:44.103667'),
('8q2tp5fuwyphf1dti3bnty11bx23hydb', '.eJyrVvIPCVCyMjQ2MDYz1FFyzU3MzFGyUsrMLU42MjAwsDBNykgsLcnMdsjJyi7VS00p1cvMU9JRckzJBdJWSqUlxYllZYnFiXmZxgYGpkAtxg7pIDP0kvNzgeqCS0pTUvNKgCqzE0syivJLMisToSYaGJgjKa0FAHSHLLM:1pyGWy:UcIwkaKsvBTzGHEBUA8_DsabcuXkvVA3nBVv_bgdMKw', '2023-05-28 18:33:16.342573'),
('cu9gb99i12c226kzqp30ockma5etz9v9', 'eyJPVFAiOjczNzQxOCwiRW1haWwiOiJpbXNjMjAwMDg3dXRzYXZAbGprdS5lZHUuaW4ifQ:1pu5L6:aUxTjHnaH2lTpDm64yW13dXdFf21FLH8-fk8G-lxtYA', '2023-05-17 05:47:44.708492'),
('fcjz9fegjc047q7jm81qr1crkff940fa', '.eJyrVgouKU1JzStRslLKTizJKMovyaxMTMpILC3JzDYwMHdIz03MzNFLzs9V0lEKLi1ILUpMyc3MA6ouhnOQ1NQCAJgsHQ0:1pyTeR:A0M3aZxN0giZPEm5d25Wfd05jvphYNYOZZ-XQqkSiSc', '2023-05-29 08:33:51.386859'),
('hpysm18yb7t4nfu1msliil4bnepsnfkv', 'eyJTdXBlcmFkbWluIjoic3VwZXJhZG1pbkBnbWFpbC5jb20ifQ:1qQMwx:XB8Zu-ASI-3dEmS9ru7dA6waJQULGJyVARDbrRGYJTI', '2023-08-14 07:04:15.948668'),
('pajljf169lsnsrzhwhfvgo58cr3q8339', 'eyJTdXBlcmFkbWluIjoic3VwZXJhZG1pbkBnbWFpbC5jb20ifQ:1q0hnE:5DoTonQg9LfiPjBIpSkFM_j4gFnzjb68dhnWptlx60w', '2023-06-04 12:04:08.265074'),
('qc32o7fi9nauyzcovtmtnmxqt2ggsp0q', 'eyJWaWNlLVByZXNpZGVudCI6InZ2a29sYWRpeWEyMDAzQGdtYWlsLmNvbSJ9:1pyPzA:urDpSLub6yiZU7gHJB3N-sKtig6Pkyk-rRiq9PRKmRI', '2023-05-29 04:39:00.798667'),
('rhf3to32wuiyfvo2804h9q2wnhywlxa9', 'eyJTdXBlcmFkbWluIjoic3VwZXJhZG1pbkBnbWFpbC5jb20ifQ:1qQN9c:jWyLolKUoJ0mSYvSnAVd5a0YQQA6y9Un_H0S1B_LZbc', '2023-08-14 07:17:20.018962'),
('ysoz55vchmgx4ofccc8ap1d0q7qure5i', 'eyJWaWNlLUNoYW5jZWxsb3IiOiJtZWV0bGltYmFzaXlhNjZAZ21haWwuY29tIn0:1pyOjF:LgFuptZC9XYmBL7LlUvJ7b9_Sx4BsLZRhQlA6F5zDAA', '2023-05-29 03:18:29.740244');

-- --------------------------------------------------------

--
-- Table structure for table `main_manage_collage`
--

CREATE TABLE `main_manage_collage` (
  `id` bigint(20) NOT NULL,
  `collageName` longtext NOT NULL,
  `collageAddress` longtext NOT NULL,
  `collageDescription` longtext NOT NULL,
  `collageImage` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_manage_collage`
--

INSERT INTO `main_manage_collage` (`id`, `collageName`, `collageAddress`, `collageDescription`, `collageImage`) VALUES
(1, 'LJ College of Computer Applications', 'LJ Campus', 'LJ College of Computer Application (affiliated to Gujarat University) is one of the premier institutes in Ahmedabad, imparting quality education and professional training for Bachelors in Computer Applications. LJ College of Computer Applications was founded by the Lok Jagruti Trust, a name held high up in esteem for providing quality education, in the year 1999 at its Vastrapur Campus.  We at LJCCA are committed to impart professional education with practical exposure, to groom young technocrats for facing the challenges and opportunities of the IT industry.', 'collage/logo2_j4Lbor9.png'),
(2, 'L.J. Institute of Engineering and Technology', 'LJ Campus', 'L.J. Institute of Engineering and Technology (L.J.I.E.T) is a sought-after institute in Gujarat that imparts quality education in the field of Engineering, IT & Software, Business & Management Studies. Established in 2007, it enjoys a good reputation for B.E. / B.Tech, M.E./M.Tech, MBA/PGDM and MCA. courses. Students can do full-time course from the Institute located in Gujarat. The Institute provides 18 UG and 11 PG Degree courses. It has decades of experience that has been built through its excellent, experienced faculty dedicated to imparting quality skills through a syllabus that is at par with industry trends.', 'collage/logo2_UimOG2P.png'),
(3, 'LJ College of Computer Applications and Web tech', 'LJ Campus', 'LJ College of Computer Application (affiliated to Gujarat University) is one of the premier institutes in Ahmedabad, imparting quality education and professional training for Bachelors in Computer Applications. LJ College of Computer Applications was founded by the Lok Jagruti Trust, a name held high up in esteem for providing quality education, in the year 1999 at its Vastrapur Campus.  We at LJCCA are committed to impart professional education with practical exposure, to groom young technocrats for facing the challenges and opportunities of the IT industry..', 'collage/logo2_gRfvZSv.png'),
(4, 'LJ College of Law', 'LJ Campus, sarkhej', 'law', 'collage/logo_1.png');

-- --------------------------------------------------------

--
-- Table structure for table `main_manage_complaindata`
--

CREATE TABLE `main_manage_complaindata` (
  `id` bigint(20) NOT NULL,
  `complainCode` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `remark` longtext DEFAULT NULL,
  `grievanceDate` date NOT NULL,
  `solvingDate` date DEFAULT NULL,
  `status` int(11) NOT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `nameOfComplainant_id` bigint(20) DEFAULT NULL,
  `nameOfSolver_id` bigint(20) DEFAULT NULL,
  `feedback` longtext DEFAULT NULL,
  `to_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_manage_complaindata`
--

INSERT INTO `main_manage_complaindata` (`id`, `complainCode`, `image`, `description`, `remark`, `grievanceDate`, `solvingDate`, `status`, `category_id`, `nameOfComplainant_id`, `nameOfSolver_id`, `feedback`, `to_id`) VALUES
(6, 'LJKU_COMPLAIN_J5KGSs', 'GrievanceImages/book-img3.jpg', 'upload photo', NULL, '2023-05-03', '2023-05-03', 0, 2, 3, NULL, NULL, 8),
(7, 'LJKU_COMPLAIN_J5KGSs', '', 'upload photo', NULL, '2023-05-03', '2023-05-03', 0, 2, 3, NULL, NULL, 8),
(8, 'LJKU_COMPLAIN_it7Kzt', 'GrievanceImages/main.pdf', 'huu', '.', '2023-05-03', '2023-05-15', 2, 1, 3, 4, NULL, 3),
(9, 'LJKU_COMPLAIN_it7Kzt', '', 'huu', '.', '2023-05-03', '2023-05-15', 1, 1, 3, 4, NULL, 3),
(10, 'LJKU_COMPLAIN_DWZ8gS', 'GrievanceImages/product-img8.jpg', 'uuuu', '.', '2023-05-03', '2023-05-15', 2, 1, 3, 4, NULL, 3),
(11, 'LJKU_COMPLAIN_DWZ8gS', '', 'uuuu', 'not possible', '2023-05-03', '2023-05-14', 1, 1, 3, 4, NULL, 3),
(12, 'LJKU_COMPLAIN_74B4xa', '', 'bad roads', NULL, '2023-05-14', '2023-05-14', 0, 6, 4, NULL, NULL, 8);

-- --------------------------------------------------------

--
-- Table structure for table `main_manage_department`
--

CREATE TABLE `main_manage_department` (
  `id` bigint(20) NOT NULL,
  `departmentname` varchar(200) NOT NULL,
  `semester` int(11) NOT NULL,
  `collageId_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_manage_department`
--

INSERT INTO `main_manage_department` (`id`, `departmentname`, `semester`, `collageId_id`) VALUES
(1, 'Msc.IT.(integrated)', 6, 1),
(2, 'MCA', 6, 1),
(3, 'Mechanical Engineering ', 8, 2),
(4, 'Civil Engineering ', 8, 2),
(6, 'law1', 6, 4);

-- --------------------------------------------------------

--
-- Table structure for table `main_manage_designation`
--

CREATE TABLE `main_manage_designation` (
  `id` bigint(20) NOT NULL,
  `designationName` longtext NOT NULL,
  `power` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_manage_designation`
--

INSERT INTO `main_manage_designation` (`id`, `designationName`, `power`) VALUES
(1, 'Superadmin', 1),
(2, 'Founder and Managing Trustee', 2),
(3, 'Vice-Chancellor', 3),
(4, 'Vice-President', 4),
(5, 'Director', 5),
(6, 'Admin', 6),
(7, 'Head Of Department', 7),
(8, 'Teacher', 8),
(10, 'Student', 9);

-- --------------------------------------------------------

--
-- Table structure for table `main_manage_grievancetype`
--

CREATE TABLE `main_manage_grievancetype` (
  `id` bigint(20) NOT NULL,
  `typeName` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_manage_grievancetype`
--

INSERT INTO `main_manage_grievancetype` (`id`, `typeName`) VALUES
(1, 'Academic'),
(2, 'Administrative'),
(3, 'Discrimination and harassment'),
(4, 'Campus safety and security'),
(5, 'Employment'),
(6, 'Other ');

-- --------------------------------------------------------

--
-- Table structure for table `main_manage_registration`
--

CREATE TABLE `main_manage_registration` (
  `id` bigint(20) NOT NULL,
  `uniqueId` longtext NOT NULL,
  `email` varchar(254) NOT NULL,
  `username` longtext NOT NULL,
  `password` longtext NOT NULL,
  `typeId_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_manage_registration`
--

INSERT INTO `main_manage_registration` (`id`, `uniqueId`, `email`, `username`, `password`, `typeId_id`) VALUES
(1, '2020004500210000', 'superadmin@gmail.com', 'superadmin', 'password@123', 1),
(3, 'TElT3b9ckwU2N7OLd', 'imsc200100meet@ljku.edu.in', 'Ankur', 'password@123', 8),
(4, '2kSNPffiffVvbaedm', 'imsc200085bhautik@ljku.edu.in', 'jignesh', 'Bhautik@1234', 7),
(5, 'nizbuMVZtFlUd6Kmf', 'utsavvasani2003@gmail.com', 'Bhavesh', 'password@123', 2),
(6, 'dUT8WxjPWLRQaoKSA', 'meetlimbasiya66@gmail.com', 'Magan', 'password@123', 3),
(7, 'KYTXm5nEyoleXuQlp', 'vvkoladiya2003@gmail.com', 'Manish Shah', 'password@123', 4),
(8, 'BvurE96jL792dSIcE', 'shreydhanani47@gmail.com', 'Alok', 'password@123', 5),
(9, 'slEnfLXJuMst1ZYXN', 'utsavvasani30052003@gmail.com', 'alpaben', 'password@123', 6),
(10, 'IIY9uYyhqfuSRY54C', 'hepinviradiya7136@gmail.com', 'bhautik', 'password@123', 10),
(14, 'CkSCHPQUbebhVGJmG', 'kathrotiyabhautik007@gmail.com', 'Bhautik', 'password@123', 10);

-- --------------------------------------------------------

--
-- Table structure for table `main_manage_user`
--

CREATE TABLE `main_manage_user` (
  `id` bigint(20) NOT NULL,
  `uniqueId` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `userName` longtext NOT NULL,
  `surName` longtext NOT NULL,
  `fatherName` longtext NOT NULL,
  `semester` int(11) DEFAULT NULL,
  `phoneNumber` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(100) NOT NULL,
  `Collage_id` bigint(20) DEFAULT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_manage_user`
--

INSERT INTO `main_manage_user` (`id`, `uniqueId`, `image`, `userName`, `surName`, `fatherName`, `semester`, `phoneNumber`, `email`, `address`, `Collage_id`, `department_id`, `designation_id`) VALUES
(2, 'TElT3b9ckwU2N7OLd', 'users/Pngtreeuser_vector_avatar_4830521_knuITxd.png', 'Meet', 'Limbasiya', 'Sureshbhai', NULL, '8849979485', 'imsc200100meet@ljku.edu.in', 'Anand Dhara Soc., mota Varachha Surat', 1, 1, 8),
(3, '2kSNPffiffVvbaedm', 'users/Pngtreeuser_vector_avatar_4830521_9E8Mc1G.png', 'jignesh', 'doshi', 'C.', NULL, '8849979485', 'imsc200085bhautik@ljku.edu.in', 'Ahmedabad ', 1, 1, 7),
(5, 'nizbuMVZtFlUd6Kmf', 'users/Pngtreeuser_vector_avatar_4830521_Rzadgok.png', 'Bhavesh', 'Patel', 'j', NULL, '9313219082', 'utsavvasani2003@gmail.com', 'punitdham', NULL, NULL, 2),
(6, 'dUT8WxjPWLRQaoKSA', 'users/Pngtreeuser_vector_avatar_4830521_WSDqaLX.png', 'Magan', 'Savaliya', 'c', NULL, '8849979485', 'meetlimbasiya66@gmail.com', 'Surat', NULL, NULL, 3),
(7, 'KYTXm5nEyoleXuQlp', 'users/Pngtreeuser_vector_avatar_4830521_NHeln2i.png', 'vinit', 'koladiya', 'v', NULL, '9313795703', 'vvkoladiya2003@gmail.com', 'Nikol', NULL, NULL, 4),
(8, 'BvurE96jL792dSIcE', 'users/Pngtreeuser_vector_avatar_4830521_o00kRRB.png', 'shreyansh ', 'dhanani', 'h.', NULL, '9313219082', 'shreydhanani47@gmail.com', 'Surat', 1, NULL, 5),
(10, 'slEnfLXJuMst1ZYXN', 'users/Pngtreeuser_vector_avatar_4830521_bFIywNE.png', 'alpaben', 'bhatt', 'hiteshbhai', NULL, '0990952053', 'utsavvasani30052003@gmail.com', 'punitdham', 1, NULL, 6),
(15, 'eYeEv5XeVc2tZN9rC', 'users/face18.jpg', 'dipesh', 'agrawal', 'ashokbhai', 6, '9409913872', 'dipeshagrawal43@gmail.com', 'ahmedabad', 1, 1, 10),
(18, 'dFvOAbofWE4GIR3XB', 'users/face27.jpg', 'dipeshh', 'agrawaal', 'ashokbhaii', 6, '9595959595', 'abc719206@gmail.com', 'Ahmedabad ', 1, 1, 10),
(19, 'CkSCHPQUbebhVGJmG', 'image\r', 'Bhautik', 'Kathrotiya', 'c', 6, '9537028184', 'kathrotiyabhautik007@gmail.com', 'amreli', 1, 2, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `main_manage_collage`
--
ALTER TABLE `main_manage_collage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_manage_complaindata`
--
ALTER TABLE `main_manage_complaindata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_manage_complain_category_id_e8addb1a_fk_main_mana` (`category_id`),
  ADD KEY `main_manage_complain_nameOfComplainant_id_b16a2228_fk_main_mana` (`nameOfComplainant_id`),
  ADD KEY `main_manage_complain_nameOfSolver_id_37ee5ee5_fk_main_mana` (`nameOfSolver_id`),
  ADD KEY `main_manage_complaindata_to_id_5cb31c1c_fk_main_manage_user_id` (`to_id`);

--
-- Indexes for table `main_manage_department`
--
ALTER TABLE `main_manage_department`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_department_collageId_id_99480503_fk_main_manage_collage_id` (`collageId_id`);

--
-- Indexes for table `main_manage_designation`
--
ALTER TABLE `main_manage_designation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_manage_grievancetype`
--
ALTER TABLE `main_manage_grievancetype`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `typeName` (`typeName`) USING HASH;

--
-- Indexes for table `main_manage_registration`
--
ALTER TABLE `main_manage_registration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `main_registration_typeId_id_10d342db_fk_main_mana` (`typeId_id`);

--
-- Indexes for table `main_manage_user`
--
ALTER TABLE `main_manage_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `main_user_Collage_id_2dc05164_fk_main_manage_collage_id` (`Collage_id`),
  ADD KEY `main_user_department_id_cfec3532_fk_main_manage_department_id` (`department_id`),
  ADD KEY `main_user_designation_id_e1da166b_fk_main_manage_designation_id` (`designation_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `main_manage_collage`
--
ALTER TABLE `main_manage_collage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `main_manage_complaindata`
--
ALTER TABLE `main_manage_complaindata`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `main_manage_department`
--
ALTER TABLE `main_manage_department`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `main_manage_designation`
--
ALTER TABLE `main_manage_designation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `main_manage_grievancetype`
--
ALTER TABLE `main_manage_grievancetype`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `main_manage_registration`
--
ALTER TABLE `main_manage_registration`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `main_manage_user`
--
ALTER TABLE `main_manage_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `main_manage_complaindata`
--
ALTER TABLE `main_manage_complaindata`
  ADD CONSTRAINT `main_manage_complain_category_id_e8addb1a_fk_main_mana` FOREIGN KEY (`category_id`) REFERENCES `main_manage_grievancetype` (`id`),
  ADD CONSTRAINT `main_manage_complain_nameOfComplainant_id_b16a2228_fk_main_mana` FOREIGN KEY (`nameOfComplainant_id`) REFERENCES `main_manage_registration` (`id`),
  ADD CONSTRAINT `main_manage_complain_nameOfSolver_id_37ee5ee5_fk_main_mana` FOREIGN KEY (`nameOfSolver_id`) REFERENCES `main_manage_registration` (`id`),
  ADD CONSTRAINT `main_manage_complaindata_to_id_5cb31c1c_fk_main_manage_user_id` FOREIGN KEY (`to_id`) REFERENCES `main_manage_user` (`id`);

--
-- Constraints for table `main_manage_department`
--
ALTER TABLE `main_manage_department`
  ADD CONSTRAINT `main_department_collageId_id_99480503_fk_main_manage_collage_id` FOREIGN KEY (`collageId_id`) REFERENCES `main_manage_collage` (`id`);

--
-- Constraints for table `main_manage_registration`
--
ALTER TABLE `main_manage_registration`
  ADD CONSTRAINT `main_registration_typeId_id_10d342db_fk_main_mana` FOREIGN KEY (`typeId_id`) REFERENCES `main_manage_designation` (`id`);

--
-- Constraints for table `main_manage_user`
--
ALTER TABLE `main_manage_user`
  ADD CONSTRAINT `main_user_Collage_id_2dc05164_fk_main_manage_collage_id` FOREIGN KEY (`Collage_id`) REFERENCES `main_manage_collage` (`id`),
  ADD CONSTRAINT `main_user_department_id_cfec3532_fk_main_manage_department_id` FOREIGN KEY (`department_id`) REFERENCES `main_manage_department` (`id`),
  ADD CONSTRAINT `main_user_designation_id_e1da166b_fk_main_manage_designation_id` FOREIGN KEY (`designation_id`) REFERENCES `main_manage_designation` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
