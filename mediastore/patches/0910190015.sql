alter table mediastore_audio add column `slug` varchar(255) not null after title;
alter table mediastore_video add column `slug` varchar(255) not null after title;
alter table mediastore_photo add column `slug` varchar(255) not null after title;
