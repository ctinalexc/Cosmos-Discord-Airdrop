-- phpMyAdmin SQL Dump
-- version 4.8.5
-- localhost
--
-- Host: localhost
-- Generation Time: Nov 20, 2022 at 10:07 AM
-- Server version: 10.5.12-MariaDB-log
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `YOUR_DB_NAME`
--

-- --------------------------------------------------------

--
-- Table structure for table `wallet_addresses`
--

CREATE TABLE `wallet_addresses` (
  `id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `redeem_count` int(11) NOT NULL DEFAULT 0,
  `prizes_amount` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `wallet_addresses`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `address` (`address`);
  
  
ALTER TABLE `wallet_addresses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
