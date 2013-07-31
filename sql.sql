DROP TABLE IF EXISTS `rss_urls`;

CREATE TABLE `rss_urls` (
  `id` INT NULL AUTO_INCREMENT DEFAULT NULL,
  `tags_id` INT NULL DEFAULT 0,
  `link` VARCHAR(150) NULL DEFAULT NULL,
  `url_name` VARCHAR(200) NULL DEFAULT NULL,
  `lang` VARCHAR(20) NULL DEFAULT NULL,
  `add_time` DATETIME NULL DEFAULT NULL,
  `is_show` TINYINT NULL DEFAULT 1,
  `is_delete` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `rss_items`;

CREATE TABLE `rss_items` (
  `id` INT NULL AUTO_INCREMENT DEFAULT NULL,
  `rss_urls_id` INT NULL DEFAULT NULL,
  `link` VARCHAR(150) NULL DEFAULT NULL,
  `title` VARCHAR(150) NULL DEFAULT NULL,
  `description` MEDIUMTEXT NULL DEFAULT NULL,
  `pubDate` VARCHAR(50) NULL DEFAULT NULL,
  `category` VARCHAR(50) NULL DEFAULT NULL,
  `source` VARCHAR(100) NULL DEFAULT NULL,
  `summary` VARCHAR(200) NULL DEFAULT NULL,
  `content` MEDIUMTEXT NULL DEFAULT NULL,
  `add_time` DATETIME NULL DEFAULT NULL,
  `add_date` DATE NULL DEFAULT NULL,
  `is_show` TINYINT NULL DEFAULT 0,
  `is_delete` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
);

CREATE TABLE `tags` (
  `id` INT NULL AUTO_INCREMENT DEFAULT NULL,
  `tag_name` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE `rss_urls` ADD FOREIGN KEY (tags_id) REFERENCES `tags` (`id`);
ALTER TABLE `rss_items` ADD FOREIGN KEY (rss_urls_id) REFERENCES `rss_urls` (`id`);


ALTER TABLE `rss_urls` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `rss_items` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `tags` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


insert into tags(tag_name) values("新闻&咨询");
insert into tags(tag_name) values("科技&互联网");
insert into tags(tag_name) values("博客&名人");
insert into tags(tag_name) values("经济&房车");
insert into tags(tag_name) values("科学&地理");
insert into tags(tag_name) values("生活&乐趣");
insert into tags(tag_name) values("读书&文娱");
insert into tags(tag_name) values("英语&教育");
insert into tags(tag_name) values("设计&创意");
insert into tags(tag_name) values("摄影&视听");
insert into tags(tag_name) values("流行&时尚");
insert into tags(tag_name) values("娱乐&八卦");
insert into tags(tag_name) values("手机&APP");
insert into tags(tag_name) values("编程&技术");
insert into tags(tag_name) values("行业&领域");
insert into tags(tag_name) values("动漫&游戏");
insert into tags(tag_name) values("体育&运动");
insert into tags(tag_name) values("电影&电视");
insert into tags(tag_name) values("军事&战争");
insert into tags(tag_name) values("女性&两性话题");
