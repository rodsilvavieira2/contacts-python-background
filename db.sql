CREATE TABLE `users` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `avatart_url` varchar(255),
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE `contacts` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `birthday` date,
  `company` varchar(255),
  `workload` varchar(255),
  `department` varchar(255),
  `user_id` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE `emails` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `contact_id` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE `phones` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `contact_id` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
ALTER TABLE `contacts`
ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
ALTER TABLE `emails`
ADD FOREIGN KEY (`contact_id`) REFERENCES `contacts` (`id`);
ALTER TABLE `phones`
ADD FOREIGN KEY (`contact_id`) REFERENCES `contacts` (`id`);