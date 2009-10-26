alter table mediastore_photo add column order_num integer default 1 after `type`;
alter table mediastore_video add column order_num integer default 1 after `type`;
alter table mediastore_audio add column order_num integer default 1 after `type`;

