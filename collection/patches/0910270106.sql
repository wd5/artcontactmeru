alter table collection_person add column order_num integer default 1 after `last_modification`;
alter table collection_band add column order_num integer default 1 after `last_modification`;
alter table collection_event add column order_num integer default 1 after `last_modification`;
