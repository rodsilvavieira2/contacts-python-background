CREATE TABLE `users` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `avatar_url` varchar(255),
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE `contacts` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `email` varchar(255),
  `phone_type_id` INT NOT NULL,
  `birthday` date,
  `company` varchar(255),
  `job` varchar(255),
  `department` varchar(255),
  `avatar_url` varchar(255),
  `user_id` int NOT NULL,
  `is_favorite` BOOLEAN NOT NULL DEFAULT FALSE,
  `is_onTrash` BOOLEAN NOT NULL DEFAULT FALSE,
  `deleted_at` timestamp,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE `phone_types` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE `user_tokens` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `token` VARCHAR(255) NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
ALTER TABLE `contacts`
ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
ALTER TABLE `contacts`
ADD FOREIGN KEY (`phone_type_id`) REFERENCES `phone_types` (`id`);
ALTER TABLE `user_tokens`
ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;