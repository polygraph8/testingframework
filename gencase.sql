use test;
CREATE TABLE `proxyed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` char(100) NOT NULL,
  `url` varchar(512) NOT NULL,
  `method` char(20) NOT NULL,
  `cookie` text NOT NULL,
  `headers` text NOT NULL,
  `data` text NOT NULL,
  `datamd5` char(100) NOT NULL,
  `response_header` text NOT NULL,
  `response_cookie` text NOT NULL,
  `response_text` text NOT NULL,
  `response_status_code` char(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `datamd5` (`datamd5`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8

CREATE TABLE `gencase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` char(100) NOT NULL,
  `url` varchar(512) NOT NULL,
  `method` char(20) NOT NULL,
  `cookie` text NOT NULL,
  `headers` text NOT NULL,
  `data` text NOT NULL,
  `datamd5` char(100) NOT NULL,
  `response_header` text NOT NULL,
  `response_cookie` text NOT NULL,
  `response_text` text NOT NULL,
  `response_status_code` char(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `datamd5` (`datamd5`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;