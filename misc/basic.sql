INSERT INTO `user` (`created_at`, `id`, `name`, `email`, `password`, `is_admin`) VALUES
('2015-02-11 22:37:44', 1, 'sajam', 'd.sajam@gmail.com', 'bc301194525501d15e6281868d75ec37', 1);

INSERT INTO `category` (`created_at`, `id`, `name`, `parent`) VALUES
(NULL, 1, 'Main 1', NULL),
(NULL, 2, 'Main 2', NULL),
(NULL, 3, 'Main 1.1', 1),
(NULL, 4, 'Main 1.1.1', 3),
(NULL, 5, 'Main 1.1.2', 3),
(NULL, 6, 'Main 1.2', 1),
(NULL, 7, 'Main 2.1', 2);