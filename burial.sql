-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 13, 2023 at 06:02 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `burial_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `burial`
--

CREATE TABLE `burial` (
  `APPLICANTID` int(11) NOT NULL,
  `APPLICANTNAME` varchar(255) NOT NULL,
  `APPLICANTAGE` varchar(255) NOT NULL,
  `APPLICANTADDRESS` varchar(255) NOT NULL,
  `DECEASEDNAME` varchar(255) NOT NULL,
  `CAUSEOFDEATH` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `burial`
--

INSERT INTO `burial` (`Field_name`, `Min_value`, `Max_value`, `Min_length`, `Max_length`, `Empties_or_zeros`, `Nulls`, `Avg_value_or_avg_length`, `Std`, `Optimal_fieldtype`) VALUES
(0x62757269616c5f64622e62757269616c2e4150504c4943414e544944, 0x32, 0x33, 1, 1, 0, 0, 0x322e35303030, 0x302e35303030, 0x454e554d282732272c27332729204e4f54204e554c4c),
(0x62757269616c5f64622e62757269616c2e4150504c4943414e544e414d45, 0x646e, 0x79, 1, 2, 0, 0, 0x312e35303030, NULL, 0x454e554d2827646e272c27792729204e4f54204e554c4c),
(0x62757269616c5f64622e62757269616c2e4150504c4943414e54414745, '', '', 0, 0, 2, 0, 0x302e30303030, NULL, 0x43484152283029204e4f54204e554c4c),
(0x62757269616c5f64622e62757269616c2e4150504c4943414e5441444452455353, 0x64, 0x79, 1, 1, 0, 0, 0x312e30303030, NULL, 0x454e554d282764272c27792729204e4f54204e554c4c),
(0x62757269616c5f64622e62757269616c2e44454345415345444e414d45, 0x64, 0x78, 1, 1, 0, 0, 0x312e30303030, NULL, 0x454e554d282764272c27782729204e4f54204e554c4c),
(0x62757269616c5f64622e62757269616c2e43415553454f464445415448, 0x6364, 0x64, 1, 2, 0, 0, 0x312e35303030, NULL, 0x454e554d28276364272c27642729204e4f54204e554c4c);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `burial`
--
ALTER TABLE `burial`
  ADD PRIMARY KEY (`APPLICANTID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `burial`
--
ALTER TABLE `burial`
  MODIFY `APPLICANTID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
