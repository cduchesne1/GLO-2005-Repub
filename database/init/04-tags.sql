DROP TABLE IF EXISTS Tags;

CREATE TABLE IF NOT EXISTS Tags (
	id INT NOT NULL,
	tag VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO Tags (id, tag) 
VALUES
	(1, 'JavaScript'),
	(2, 'HTML'),
	(3, 'CSS'),
	(4, 'SQL'),
	(5, 'Python'),
	(6, 'Java'),
	(7, 'Shell'),
	(8, 'C#'),
	(9, 'TypeScript'),
	(10, 'PHP'),
	(11, 'C++'),
	(12, 'C'),
	(13, 'Go'),
	(14, 'Kotlin'),
	(15, 'Ruby'),
	(16, 'VBA'),
	(17, 'Swift'),
	(18, 'R'),
	(19, 'Assembly'),
	(20, 'Rust'),
	(21, 'Objective-C'),
	(22, 'Scala'),
	(23, 'Dart'),
	(24, 'Flutter'),
	(25, 'React'),
	(26, 'React-Native'),
	(27, 'NodeJS');
