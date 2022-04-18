DROP TABLE IF EXISTS Collaborators;

CREATE TABLE IF NOT EXISTS Collaborators (
	user INT,
	repository INT,
	PRIMARY KEY (user, repository),
	FOREIGN KEY (user) REFERENCES users(id) ON DELETE CASCADE,
	FOREIGN KEY (repository) REFERENCES repositories(id) ON DELETE CASCADE
);

INSERT INTO Collaborators (user, repository) 
VALUES
	(85, 45),
	(3, 107),
	(56, 141),
	(70, 111),
	(15, 132),
	(49, 196),
	(36, 178),
	(7, 10),
	(84, 5),
	(34, 155),
	(26, 132),
	(16, 88),
	(56, 128),
	(16, 59),
	(9, 110),
	(54, 111),
	(70, 117),
	(88, 164),
	(32, 169),
	(11, 7),
	(40, 104),
	(15, 157),
	(51, 180),
	(90, 35),
	(100, 13),
	(38, 80),
	(27, 13),
	(63, 199),
	(10, 105),
	(7, 155),
	(53, 101),
	(33, 95),
	(45, 11),
	(89, 108),
	(78, 53),
	(54, 107),
	(52, 99),
	(61, 107),
	(59, 132),
	(91, 131),
	(17, 67),
	(81, 73),
	(100, 140),
	(69, 82),
	(22, 135),
	(73, 39),
	(57, 58),
	(13, 73),
	(48, 97),
	(53, 137),
	(6, 93),
	(58, 133),
	(19, 91),
	(89, 183),
	(41, 199),
	(74, 105),
	(76, 6),
	(32, 109),
	(87, 155),
	(62, 125),
	(75, 193),
	(68, 94),
	(12, 178),
	(54, 45),
	(86, 88),
	(67, 161),
	(19, 52),
	(3, 57),
	(48, 102),
	(73, 149),
	(6, 71),
	(1, 136),
	(63, 90),
	(20, 5),
	(91, 151),
	(35, 132),
	(4, 123),
	(28, 115),
	(96, 180),
	(30, 41),
	(4, 161),
	(41, 179),
	(75, 185),
	(11, 189),
	(73, 5),
	(3, 142),
	(57, 120),
	(83, 194),
	(69, 98),
	(56, 132),
	(49, 119),
	(53, 44),
	(20, 196),
	(30, 69),
	(99, 103),
	(7, 35),
	(95, 95),
	(56, 76),
	(34, 183),
	(37, 170);