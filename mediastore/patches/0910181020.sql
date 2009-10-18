alter table mediastore_photo add column catalog_id integer after `type`;
alter table mediastore_audio add column catalog_id integer after `type`;
alter table mediastore_video add column catalog_id integer after `type`;
CREATE INDEX `mediastore_photo_catalog_id` ON `mediastore_photo` (`catalog_id`);
CREATE INDEX `mediastore_video_catalog_id` ON `mediastore_video` (`catalog_id`);
CREATE INDEX `mediastore_audio_catalog_id` ON `mediastore_audio` (`catalog_id`);

