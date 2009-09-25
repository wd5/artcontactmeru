-- патч для добавления поля is_main
alter table mediastore_photo add column `is_main` bool not null after `last_modification`;
alter table mediastore_video add column `is_main` bool not null after `last_modification`;
alter table mediastore_audio add column `is_main` bool not null after `last_modification`;
