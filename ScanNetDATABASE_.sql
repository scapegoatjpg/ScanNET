-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 10, 2021 at 05:26 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scannet`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--
CREATE DATABASE IF NOT EXISTS `scannet`;
USE `scannet`;

CREATE TABLE `customer` (
  `userID` int(12) NOT NULL,
  `firstName` varchar(40) NOT NULL,
  `lastName` varchar(40) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `IPAddress` varchar(40) NOT NULL,
  `loginName` varchar(40) NOT NULL,
  `invalidLogin` int(200) NOT NULL,
  `bandwith` int(255) NOT NULL,
  `active` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`userID`, `firstName`, `lastName`, `username`, `password`, `IPAddress`, `loginName`, `invalidLogin`, `bandwith`, `active`) VALUES
(1, '', '', 'laura115', 'pass5', '', '', 0, 0, ''),
(2, '', '', 'shani2017', 'murphy2017', '', '', 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `device`
--

CREATE TABLE `device` (
  `IPAddress` varchar(40) NOT NULL,
  `MACAddress` varchar(40) NOT NULL,
  `activityReportID` int(14) NOT NULL,
  `deviceName` varchar(40) NOT NULL,
  `customerName` varchar(80) NOT NULL,
  `serviceProvider` varchar(40) NOT NULL,
  `networkCard` varchar(80) NOT NULL,
  `firstDetection` datetime NOT NULL,
  `lastDetection` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `networkactivity`
--

CREATE TABLE `networkactivity` (
  `activityReportID` int(14) NOT NULL,
  `IPAddress` int(200) NOT NULL,
  `networkNameSSID` int(40) NOT NULL,
  `packetNum` int(100) NOT NULL,
  `timeStamp` datetime NOT NULL,
  `source` varchar(200) NOT NULL,
  `destination` varchar(200) NOT NULL,
  `maliciousDevices` int(200) NOT NULL,
  `activitySummary` varchar(255) NOT NULL,
  `totalDevices` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `networkinfo`
--

CREATE TABLE `networkinfo` (
  `networkNameSSID` int(40) NOT NULL,
  `activityReportID` int(14) NOT NULL,
  `IPAddress` varchar(40) NOT NULL,
  `PHYType` varchar(255) NOT NULL,
  `channelNum` varchar(255) NOT NULL,
  `maxSpeed` varchar(255) NOT NULL,
  `connectedDevices` int(200) NOT NULL,
  `activeDevices` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`userID`);

--
-- Indexes for table `device`
--
ALTER TABLE `device`
  ADD PRIMARY KEY (`IPAddress`);

--
-- Indexes for table `networkactivity`
--
ALTER TABLE `networkactivity`
  ADD PRIMARY KEY (`activityReportID`);

--
-- Indexes for table `networkinfo`
--
ALTER TABLE `networkinfo`
  ADD PRIMARY KEY (`networkNameSSID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `userID` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
