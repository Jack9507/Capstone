-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 28, 2021 at 11:31 PM
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
-- Database: `capstone`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogcontact`
--

CREATE TABLE `blogcontact` (
  `sno` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` bigint(50) NOT NULL,
  `msg` varchar(255) NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blogcontact`
--

INSERT INTO `blogcontact` (`sno`, `name`, `phone`, `msg`, `date`, `email`) VALUES
(1, 'test', 9781639191, 'testmsg', '2021-04-28 06:57:22', 'test@gmail.com'),
(2, 'Jatin', 9781639191, 'First Msg', '2021-04-28 07:05:30', 'jatin998kk@gmail.com'),
(3, 'Jerry', 9781639191, 'second message', '2021-04-28 07:07:23', 'Jerry@gmail.com'),
(6, 'Harry', 5847956485, 'Coding thunder', '2021-04-28 07:12:08', 'codewithharry@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `blogpost`
--

CREATE TABLE `blogpost` (
  `sno` int(50) NOT NULL,
  `title` varchar(255) NOT NULL,
  `tagline` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` mediumtext NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blogpost`
--

INSERT INTO `blogpost` (`sno`, `title`, `tagline`, `slug`, `content`, `date`) VALUES
(1, 'Test Title', 'Test Tagline.', 'first-slug', 'This is test content.', '2021-04-29 02:08:31'),
(2, 'Let\'s learn about Amazon Web Services.', 'The biggest cloud computing platform.', 'aws-info', 'Amazon Web Services (AWS) is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis. These cloud computing web services provide a variety of basic abstract technical infrastructure and distributed computing building blocks and tools. One of these services is Amazon Elastic Compute Cloud (EC2), which allows users to have at their disposal a virtual cluster of computers, available all the time, through the Internet. AWS\'s version of virtual computers emulates most of the attributes of a real computer, including hardware central processing units (CPUs) and graphics processing units (GPUs) for processing; local/RAM memory; hard-disk/SSD storage; a choice of operating systems; networking; and pre-loaded application software such as web servers, databases, and customer relationship management (CRM).\r\n\r\nThe AWS technology is implemented at server farms throughout the world, and maintained by the Amazon subsidiary. Fees are based on a combination of usage (known as a \"Pay-as-you-go\" model), hardware, operating system, software, or networking features chosen by the subscriber required availability, redundancy, security, and service options. Subscribers can pay for a single virtual AWS computer, a dedicated physical computer, or clusters of either. As part of the subscription agreement,[10] Amazon provides security for subscribers\' systems. AWS operates from many global geographical regions including 6 in North America.[11]\r\n\r\nAmazon markets AWS to subscribers as a way of obtaining large scale computing capacity more quickly and cheaply than building an actual physical server farm.[12] All services are billed based on usage, but each service measures usage in varying ways. As of 2017, AWS owns a dominant 33% of all cloud (IaaS, PaaS) while the next two competitors Microsoft Azure and Google Cloud have 18%, 9% respectively according to Synergy Group.', '2021-04-28 09:23:10'),
(3, 'Python Flask a microframework for Web development.', 'Super simple and easy for beginners.', 'flask-info', 'Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[2] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.\r\n\r\nComponents\r\n\r\nThe microframework Flask is based on the Pocoo projects, Werkzeug and Jinja2.\r\n\r\nHistory\r\n\r\nFlask was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004.[6] According to Ronacher, the idea was originally an April Fool\'s joke that was popular enough to make into a serious application.[7][8][9]\r\n\r\nWhen Ronacher and Georg Brandl created[when?] a bulletin board system written in Python, the Pocoo projects Werkzeug and Jinja were developed.[10]\r\n\r\nFlask has become popular among Python enthusiasts. As of October 2020, it has second most stars on GitHub among Python web-development frameworks, only slightly behind Django,[11] and was voted the most popular web framework in the Python Developers Survey 2018.\r\nWerkzeug\r\nWerkzeug is a utility library for the Python programming language, in other words a toolkit for Web Server Gateway Interface (WSGI) applications, and is licensed under a BSD License. Werkzeug can realize software objects for request, response, and utility functions. It can be used to build a custom software framework on top of it and supports Python 2.7 and 3.5 and later.', '2021-04-28 11:14:43'),
(4, 'How Cloudflare provides security, CDN, domain name server services, etc.', 'Cloudflare, Inc. is an American web infrastructure and website security company.', 'cloudflare-info', 'Cloudflare, Inc. is an American web infrastructure and website security company that provides content delivery network services, DDoS mitigation, Internet security, and distributed domain name server services.[2] Cloudflare\'s services sit between a website\'s visitor and the Cloudflare user\'s hosting provider, acting as a reverse proxy for websites.[3][4] Cloudflare\'s headquarters are in San Francisco.\r\nCloudflare acts as a reverse proxy for web traffic. Cloudflare supports web protocols, including SPDY and HTTP/2. In addition to this, Cloudflare offers support for HTTP/2 Server Push.[21]\r\n\r\nDDoS Protection\r\nCloudflare provides DDoS mitigation services which protect customers from distributed denial of service (DDoS) attacks. As of September 2020, the company claims to block \"an average of 72 billion threats per day, including some of the largest DDoS attacks in history.\"[22]\r\n\r\nOn September 6, 2019, Wikipedia became the victim of a DDoS attack. European users were unable to access Wikipedia for several hours.[23] The attack was mitigated after Wikimedia network engineers used Cloudflare\'s network and DDoS protection services to re-route and filter internet traffic.[24] The specific Cloudflare product used was Magic Transit.[25]\r\n\r\nContent Distribution Network\r\nCloudflare offers a popular Content Distribution Network (CDN) service. The company launched in 2010 and TechCrunch wrote that its goal was to be \"a CDN for the masses\".[26] Ten years later, the company claimed to support over 25 million internet websites.[27]\r\n\r\nTeams\r\nCloudflare for Teams is a suite of authentication and security products aimed at business clients. Teams consists of two parts: Gateway, a highly-customizable dns resolver, and Access, a zero-trust authentication service.[28]\r\n\r\nWorkers\r\nIn 2017 Cloudflare launched Cloudflare Workers, a serverless computing platform that allows one to create entirely new applications or augment existing ones without configuring or maintaining infrastructure. Since then, the product has expanded to include Workers KV, a low-latency key-value data store, Cron Triggers for scheduling cron jobs, and additional tooling for developers to deploy and scale their code across the globe.\r\n\r\nPages\r\nAfter being leaked to the press,[29] Cloudflare Pages was launched as a beta in December 2020. The product is a Jamstack platform for front end developers to collaborate and deploy websites on Cloudflare\'s infrastructure of 200+ data centers worldwide.\r\n\r\nAcquisitions\r\nThe following is a list of acquisitions by Cloudflare:\r\n\r\nStopTheHacker (Feb 2014)[30]\r\nCryptoSeal (June 2014)[31]\r\nEager Platform Co. (December 2016)[32]\r\nNeumob (November 2017)[33]\r\nS2 Systems (January 2020)[34][35]\r\nLinc (December 2020)[36]\r\nSecurity and privacy issues\r\nThe hacker group UGNazi attacked Cloudflare partially by exploiting flaws in Google\'s authentication systems in June 2012, gaining administrative access to Cloudflare and using it to deface 4chan.[37][38] From September 2016 until February 2017, a major Cloudflare bug (nicknamed Cloudbleed) leaked sensitive data, including passwords and authentication tokens, from customer websites by sending extra data in response to web requests.[39] The leaks resulted from a buffer overflow which occurred, according to analysis by Cloudflare, on approximately 1 in every 3,300,000 HTTP requests.[40][41]\r\n\r\nIn May 2017, ProPublica reported that Cloudflare as a matter of policy relays the names and email addresses of persons complaining about hate sites to the sites in question, which has led to the complainants being harassed. Cloudflare\'s general counsel defended the company\'s policies by saying it is \"base constitutional law that people can face their accusers\".[42] In response to the report, Cloudflare updated their abuse reporting process to provide greater control over who is notified of the complaining party.[43]\r\n\r\nCloudflare is cited in reports by The Spamhaus Project, an international spam tracking organization, due to high numbers of cybercriminal botnet operations \'hosted\' on Cloudflare services.[44] [45] [46] An October 2015 report found that Cloudflare provisioned 40% of SSL certificates used by phishing sites with deceptive domain names resembling those of banks and payment processors.[47]\r\n\r\nCloudflare suffered a major outage on July 2, 2019,[48] which rendered more than 12 million websites (80% of all customers) unreachable for 27 minutes.[49] A similar outage occurred on July 17, 2020, causing a similar effect and impacting approximately the same number of sites.[50][51]\r\n\r\nOn March 9, 2021, Tillie Kottmann from the hacking collective \"Advanced Persistent Threat 69420\" revealed to Bloomberg News that the group had gotten root shell access to Cloudflare headquarters\' internal network due to a security failure in the company\'s camera system.[52] This meant that they had complete access to run any commands on the network. The group also accessed video feeds from company cameras monitoring entry points and thoroughfares. Cloudflare confirmed these claims in a blog post, but disputed that the hackers would have been able to access the company\'s data centers from the corporate network. They also denied Kottmann\'s claims that they would have been able to access CEO Matthew Prince\'s laptop from the compromised network, stating that he was out of the office at the time.', '2021-04-28 11:19:14'),
(5, 'What are Virtual Private Servers and how they work?', 'A VPS is a virtual machine sold as a service by an Internet hosting service. ', 'vps-info', 'A virtual private server (VPS) is a virtual machine sold as a service by an Internet hosting service. The virtual dedicated server (VDS) also has a similar meaning.\r\n\r\nA virtual private server runs its own copy of an operating system (OS), and customers may have superuser-level access to that operating system instance, so they can install almost any software that runs on that OS. For many purposes it is functionally equivalent to a dedicated physical server and, being software-defined, can much more easily be created and configured. A virtual server costs much less than an equivalent physical server. However, as virtual servers share the underlying physical hardware with other VPSes, performance may be lower, depending on the workload of any other executing virtual machines.\r\nVirtualization\r\nThe force driving server virtualization is similar to that which led to the development of time-sharing and multiprogramming in the past. Although the resources are still shared, as under the time-sharing model, virtualization provides a higher level of security, dependent on the type of virtualization used, as the individual virtual servers are mostly isolated from each other and may run their own full-fledged operating system which can be independently rebooted as a virtual instance.\r\n\r\nPartitioning a single server to appear as multiple servers has been increasingly common on microcomputers since the launch of VMware ESX Server in 2001. The physical server typically runs a hypervisor which is tasked with creating, releasing, and managing the resources of \"guest\" operating systems, or virtual machines. These guest operating systems are allocated a share of resources of the physical server, typically in a manner in which the guest is not aware of any other physical resources save for those allocated to it by the hypervisor. As a VPS runs its own copy of its operating system, customers have superuser-level access to that operating system instance, and can install almost any software that runs on the OS; however, due to the number of virtualization clients typically running on a single machine, a VPS generally has limited processor time, RAM, and disk space.[2]\r\n\r\nMotivation\r\nUltimately, it is used to decrease hardware costs by condensing a failover cluster to a single machine, thus decreasing costs dramatically while providing the same services. Server roles and features are generally designed to operate in isolation. For example, Windows Server 2019 requires a certificate authority and a domain controller to exist on independent servers with independent instances of Windows Server. This is because additional roles and features adds areas of potential failure as well as adding visible security risks (placing a certificate authority on a domain controller poses the potential for root access to the root certificate). This directly motivates demand for virtual private servers in order to retain conflicting server roles and features on a single hosting machine. Also, the advent of virtual machine encrypted networks decreases pass-through risks that might have otherwise discouraged VPS usage as a legitimate hosting server.\r\n\r\nHosting\r\nMany companies offer virtual private server hosting or virtual dedicated server hosting as an extension for web hosting services. There are several challenges to consider when licensing proprietary software in multi-tenant virtual environments.\r\n\r\nWith unmanaged or self-managed hosting, the customer is left to administer their own server instance.\r\n\r\nUnmetered hosting is generally offered with no limit on the amount of data transferred on a fixed bandwidth line. Usually, unmetered hosting is offered with 10 Mbit/s, 100 Mbit/s, or 1000 Mbit/s (with some as high as 10Gbit/s). This means that the customer is theoretically able to use ~3 TB on 10 Mbit/s or up to ~300 TB on a 1000 Mbit/s line per month, although in practice the values will be significantly less. In a virtual private server, this will be shared bandwidth and a fair usage policy should be involved. Unlimited hosting is also commonly marketed but generally limited by acceptable usage policies and terms of service. Offers of unlimited disk space and bandwidth are always false due to cost, carrier capacities, and technological boundaries.', '2021-04-29 02:09:16'),
(11, 'Nissan Gtr V-12', 'fast cars future', 'p1-car', 'Slays on and off the track.', '2021-04-29 02:41:49');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `id` int(10) NOT NULL,
  `Name` text NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Subject` varchar(100) NOT NULL,
  `Message` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`id`, `Name`, `Email`, `Subject`, `Message`) VALUES
(1, 'Jerry', 'Jerrybusiness55@gmail.com', 'First subject', 'Anyways this is the first message into the contacts table in the database.'),
(2, 'Jatin Kumar', 'jatin998kk@gmail.com', 'Computer Science', 'I love CSE.'),
(3, 'Honey', 'Honey123@gmail.com', 'Cold Weather', 'That was Epic.'),
(18, 'Jatin Kumar', 'jatin99kjjjjkj8kk@gmail.com', 'kjkjkk', 'Hello'),
(19, 'vishal', 'vishal@gmail.com', 'f122', 'racer'),
(20, 'Virat Kohli', 'virat@gmail.com', 'cricket', 'I am the best player in the world.');

-- --------------------------------------------------------

--
-- Table structure for table `newsletter`
--

CREATE TABLE `newsletter` (
  `id` int(11) NOT NULL,
  `Email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `newsletter`
--

INSERT INTO `newsletter` (`id`, `Email`) VALUES
(1, 'jerrybusiness55@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `userid` int(10) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `designation` varchar(255) DEFAULT NULL,
  `phone` bigint(150) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`userid`, `name`, `email`, `designation`, `phone`, `password`) VALUES
(1, 'First Person', 'first@gmail.com', NULL, 8741256478, 'Thisismypassword'),
(2, 'Trever Phillips', 'trever@gmail.com', 'GTA5 Character', 8604600626, '$pbkdf2-sha256$29000$9r53DqHU.j.nVIrx3tsbYw$/lgyrhFSOcBFQzdh/Yslvf9YStL2BAC2pnz8v4y8YLc'),
(3, 'Jatin Kumar', 'jatin998kk@gmail.com', NULL, 9781639191, '$pbkdf2-sha256$29000$vxci5Pzfe49RKsW419obQw$2sRe0JQk9GSkHBgFYR6REuqL4Vx.E/jJWsIYZtrmFLw'),
(4, 'prakhar', 'raizada@gmail.com', NULL, 8745126589, '$pbkdf2-sha256$29000$GwMAgDCGEGKMMYawttaa8w$YSjMP/GgEvwpN5YnyGFZofL545huW86FAl2lZFVWxhE'),
(5, 'Abhishek', 'rishu@gmail.com', NULL, 9781639191, '$pbkdf2-sha256$29000$tFYKYezdG4OwFsIYQ6g1Zg$B79rngyE5M4sQpxba90jm6kc8g24xdqP5xg6Tx7k57k'),
(6, 'Bittu', 'bittu@gmail.com', NULL, 9781639191, '$pbkdf2-sha256$29000$GGPM2dt7LwWAsNbaO8f4nw$JkSKddBTQHzblaFww3fMnpoZPMNR5vgzyNBuIHv9eXc'),
(7, 'new', 'new@gmail.com', NULL, 8547456985, '$pbkdf2-sha256$29000$wFgrhbDWOsdYi1EKQUgJgQ$5iZe.6JtlIHcy6vI7INk5zJ1zWGhpdKLbeTkKkoXe5o'),
(8, 'maxwell', 'max@gmail.com', NULL, 8745124578, '$pbkdf2-sha256$29000$W0vpPYdwbg1hDAFACEHo3Q$ArXeHy4Bf0x7xU0vpw.cNRoFqdvhZ/I7M4TBGkc8pJ0'),
(10, 'Prakhar Raizada', 'prakhar@gmail.com', 'BCA Student', 8564745254, '$pbkdf2-sha256$29000$hLDWuheiNIbwnhPCGCPkPA$C6mQLNGlM0yxdPjuqNFSB/bg6Tra4vOI2thJQoZrB1g');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogcontact`
--
ALTER TABLE `blogcontact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `blogpost`
--
ALTER TABLE `blogpost`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newsletter`
--
ALTER TABLE `newsletter`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `signup`
--
ALTER TABLE `signup`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogcontact`
--
ALTER TABLE `blogcontact`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `blogpost`
--
ALTER TABLE `blogpost`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `newsletter`
--
ALTER TABLE `newsletter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `signup`
--
ALTER TABLE `signup`
  MODIFY `userid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
