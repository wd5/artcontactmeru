alter table mediastore_video drop column file;
alter table mediastore_video add column `youtube` varchar(20) not null;
